from connectors.scylladb import scylla_db_connection
from statements import tournament_targets as tournament_targets_statements


def get_user_tournament_targets(user_id: str) -> list[dict]:
    prepared_statement_query = tournament_targets_statements.find_all_by_user_id()
    prepared_statement = scylla_db_connection.get_prepared_statement(
        prepared_statement_query
    )

    return scylla_db_connection.execute_read_prepared_statement(
        prepared_statement, [user_id]
    )
