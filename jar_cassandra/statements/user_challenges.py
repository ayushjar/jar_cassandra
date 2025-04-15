def find_all_by_user_id_and_tournament_id_and_challenge_date():
    return """SELECT challenge_type, challenge_task_type, created_at, completed_at, claimed_at, 
           user_id, priority, challenge_date, tournament_id FROM user_challenges WHERE user_id=? AND tournament_id=? AND challenge_date=?"""
