import datetime
from connectors.scylladb import scylla_db_connection
from statements import user_challenges as user_challenge_statements


def get_user_challenges(
    user_id: str, tournament_id: str, challenge_date: datetime.datetime
) -> list[dict]:
    prepared_statement_query = (
        user_challenge_statements.find_all_by_user_id_and_tournament_id_and_challenge_date()
    )
    prepared_statement = scylla_db_connection.get_prepared_statement(
        prepared_statement_query
    )

    return scylla_db_connection.execute_read_prepared_statement(
        prepared_statement, [user_id, tournament_id, challenge_date]
    )
