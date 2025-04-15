from connectors.scylladb import scylla_db_connection
from statements import user_tournament_rewards as user_tournament_rewards_statements


def get_user_tournament_rewards(user_id: str, reward_sources: tuple[str]) -> list[dict]:
    prepared_statement_query = (
        user_tournament_rewards_statements.find_all_by_user_id_and_reward_source_in()
    )
    prepared_statement = scylla_db_connection.get_prepared_statement(
        prepared_statement_query
    )

    return scylla_db_connection.execute_read_prepared_statement(
        prepared_statement, [user_id, reward_sources]
    )
