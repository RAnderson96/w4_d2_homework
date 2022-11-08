from db.run_sql import run_sql

from models.user import User


def select_all():  
    users = [] 

    sql = "SELECT * FROM users"

    results = run_sql(sql)

    for row in results:


        user = User(row['f_name'], row['l_name'], row['id'] )
        users.append(user)
    return users 

# SAVE
def save(user):
    sql = """INSERT INTO users (f_name, l_name) 
    VALUES (%s, %s) RETURNING *
    """
    values = [user.f_name, user.l_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

# SELECT


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are `falsy`
    # Could alternatively have ...
    # if len(results) > 0

    if results:
        result = results[0]
        user = User(result['f_name'], result['l_name'] )
    return user

# DELETE 

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# DELETE ALL

def delete_all():
    sql = "DELETE FROM users"
    values = [id]
    run_sql(sql, values)


# UPDATE

def update(user):
    sql = """UPDATE users SET (f_name, l_name) = (%s, %s) 
    WHERE id = %s"""
    
    values = [user.f_name, user.l_name, user.id]
    run_sql(sql, values)

def task_return(user):
    sql = """SELECT * FROM tasks WHERE id=%s
    """
    values = [user.id]

    result = run_sql(sql, values)

    print(result)
