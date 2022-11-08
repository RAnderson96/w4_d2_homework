import pdb 
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository 
import repositories.user_repository as user_repository 

task_repository.delete_all()
user_repository.delete_all()




user1 = User("Rory", "Anderson")
user2 = User("Ed", "D")
user3 = User("Bob", "E")

task1 = Task("Gym", "Alex", 120, user1, False)
task2 = Task("Be bad at Krunker", "Eddie", 99999999, user2, False)
task3 = Task("Make Chicken Noise", "Rory", 24*60*364, user3, False)

user_repository.save(user1)
user_repository.save(user2)
user_repository.save(user3)

user1.f_name = "Rory The King of Krunker"
user_repository.update(user1)


task_repository.save(task1)
task_repository.save(task2)
task_repository.save(task3)

task2.description = "Be bad at Krunker and with a trackpad"
task_repository.update(task2)

# result = task_repository.select_all()

# result2 = task_repository.select(1)

test = user_repository.task_return(user1)

# for task in result:
#     print(task.__dict__)

pdb.set_trace()


