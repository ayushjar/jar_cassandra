def find_all_by_user_id_and_reward_source_in():
    return """SELECT user_id, reward_source, reward_amount, reward_type, created_at FROM tournament_rewards WHERE user_id=? AND reward_source in ?"""
