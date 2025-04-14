from cassandra.cluster import Cluster
from cassandra.query import PreparedStatement
from cassandra.auth import PlainTextAuthProvider


class ScyllaDBConnection:
    def __init__(
        self, contact_points: list[str], username: str, password: str, keyspace: str
    ):
        self.username = username
        self.__contact_points = contact_points
        self.__password = password
        self.__connection = None
        self.__session = None

        self.__connect()
        if not self.__is_connection_valid():
            return
        self.set_current_keyspace(keyspace)

    def __connect(self) -> None:
        auth_provider = PlainTextAuthProvider(
            username=self.username, password=self.__password
        )
        self.__connection = Cluster(
            contact_points=self.__contact_points, auth_provider=auth_provider
        )
        self.__session = self.__connection.connect()

    def __is_connection_valid(self) -> bool:
        return self.__connection is not None and self.__session is not None

    def __execute(self, query):
        return self.__session.execute(query)

    def get_current_keyspace(self) -> str:
        return self.__session.keyspace

    def set_current_keyspace(self, keyspace: str) -> str:
        self.__session.set_keyspace(keyspace)
        return self.get_current_keyspace()

    def get_prepared_statement(self, query: str) -> PreparedStatement:
        return self.__session.prepare(query)

    def execute_read_prepared_statement(
        self, prepared_statement: PreparedStatement, parameters: list
    ) -> list[dict]:
        rows = self.__execute(prepared_statement.bind(parameters))
        return list(rows)

    def execute_insert_prepared_statement(
        self, prepared_statement: PreparedStatement, parameters: list
    ) -> None:
        rows = self.__execute(prepared_statement.bind(parameters))

    def execute_update_prepared_statement(
        self, prepared_statement: PreparedStatement, parameters: list
    ) -> None:
        rows = self.__execute(prepared_statement.bind(parameters))

    def execute_delete_prepared_statement(
        self, prepared_statement: PreparedStatement, parameters: list
    ) -> None:
        rows = self.__execute(prepared_statement.bind(parameters))


scylla_db_connection = ScyllaDBConnection(
    ["172.31.82.29", "172.31.82.67."], "cassandra", "cassandra", "changejar"
)
