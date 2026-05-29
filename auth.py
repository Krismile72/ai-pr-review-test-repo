def login(user_id):

    query = f"SELECT * FROM users WHERE id = {user_id}"

    password = "123456"

    return query