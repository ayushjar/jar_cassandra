def find_all_by_user_id_and_tournament_id_and_challenge_date():
    return """SELECT * FROM user_challenges WHERE user_id=? AND tournament_id=? AND challenge_date=?"""
