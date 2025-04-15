def find_all_by_user_id():
    return """SELECT user_id, level, state, created_at FROM tournament_targets WHERE user_id=?"""
