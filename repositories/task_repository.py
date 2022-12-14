from db.run_sql import run_sql

from models.task import Task
import repositories.user_repository as user_repository
  
def select_all():  
    tasks = [] 

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        task = Task(
            row['description'], 
            row['assignee'], 
            row['duration'], 
            user, 
            row['completed'], 
            row['id'] 
            )
        tasks.append(task)
    return tasks 

# SAVE
def save(task):
    sql = """INSERT INTO tasks (description, assignee, duration, user_id, completed) 
    VALUES (%s, %s, %s, %s, %s) RETURNING *
    """
    values = [task.description, task.assignee, task.duration, task.user_id.id, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task

# SELECT


def select(id):

    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are `falsy`
    # Could alternatively have ...
    # if len(results) > 0

    if results:
        result = results[0]
        user = user_repository.select(result['user_id'])
        task = Task(
            result['description'], 
            result['assignee'], 
            result['duration'], 
            user, 
            result['completed']
            )
    return task

# DELETE 

def delete(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# DELETE ALL

def delete_all():
    sql = "DELETE FROM tasks"
    values = [id]
    run_sql(sql, values)


# UPDATE

def update(task):
    sql = """UPDATE tasks SET (description, assignee, duration, user_id, completed) = (%s, %s, %s, %s, %s) 
    WHERE id = %s"""
    
    values = [task.description, task.assignee, task.duration, task.user_id.id, task.completed, task.id]
    run_sql(sql, values)
