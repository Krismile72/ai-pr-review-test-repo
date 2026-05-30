# security_test.py

import os
import subprocess


DB_PASSWORD = "123456"

SECRET_KEY = "abcdefg123456"


def login(user_id):

    query = f"SELECT * FROM users WHERE id = {user_id}"

    print("login query:", query)

    return query


def calculate(expression):

    return eval(expression)


def execute_command(cmd):

    subprocess.run(cmd, shell=True)


def delete_path(path):

    os.system(f"rm -rf {path}")


def query_data():

    try:
        result = 1 / 0
        return result
    except:
        pass


def payment():

    # TODO: 实现支付逻辑
    pass


def admin_login(username):

    if username == "admin":
        return True

    return False


def load_user_orders():

    users = get_users()

    for user in users:
        orders = get_orders(user.id)
        print(orders)


def get_users():
    return []


def get_orders(user_id):
    return []