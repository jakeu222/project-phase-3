# lib/cli.py
from models.model_1 import *
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from helpers import (
    exit_program,
    helper_1
)
import inquirer
# questions = [
#   inquirer.Text('name', message="What's your name"),
#   inquirer.Text('surname', message="What's your surname"),
#   inquirer.Text('phone', message="What's your phone number",
#                 validate=lambda _, x: re.match('\+?\d[\d ]+\d', x),
#                 )
# ]
# answers = inquirer.prompt(questions)
# players.name = answers['name']


def main():
    engine = create_engine("sqlite:///todo.db")


    Base.metadata.create_all(engine)

    with Session(engine) as session:

        title = '''   .___________.  ______                 _______   ______      __       __       _______.___________.
   |           | /  __  \               |       \ /  __  \    |  |     |  |     /       |           |
   `---|  |----`|  |  |  |    ______    |  .--.  |  |  |  |   |  |     |  |    |   (----`---|  |----`
       |  |     |  |  |  |   |______|   |  |  |  |  |  |  |   |  |     |  |     \   \       |  |     
       |  |     |  `--'  |              |  '--'  |  `--'  |   |  `----.|  | .----)   |      |  |     
       |__|      \______/               |_______/ \______/    |_______||__| |_______/       |__|     
                                                                                                     '''
        
        print(title)
        
        import inquirer
        questions = [
        inquirer.List('size',
                        message="Look Ma, I can use inquire too!",
                        choices=[ 'Does this list even do anything?', 'No it doesnt', 'Lets continue'],
                    ),
        ]
        answers = inquirer.prompt(questions)
        print()
        i1 = input("Please enter your username: ")
        print()
        one_user = session.query(User).filter(User.full_name == i1).first()
        if one_user:
            print()
            print("User profile exists")
            print()



            

            print()
            i5 = input("Do you want to create a new task? (yes/no): ")
            print()
            if i5 == "yes":
                print()


                i2 =input("Please enter a new task description: ")
                print()
                new_task = Task(task=i2, user=one_user)

            

                session.add(new_task)
                session.commit()

        else:
            print()
            print("Sorry, user not found")
            print()
            i3 = input("Please input your new user name: ")
            print()
            n_user_name = User(full_name=i3)
            session.add(n_user_name)
            print()
            i5 = input("Do you want to create a new task? (yes/no): ")
            print()
            if i5 == "yes":
                print()

                i4 = input("Please enter a new task description: ")
                print()
                new_task = Task(task=i4, user=n_user_name)

                session.add(new_task)
                session.commit()
            
        print()
        display = input("Do you want to display your tasks to update or delete?  (yes/no): ").lower()
        print()
        if display == "yes":
            print()
            usertasks = session.query(Task).filter(Task.user == one_user).all()
            print(usertasks)
            print()
            update = input("Choose task id: ")
            print()
            updated_task = session.query(Task).filter(Task.id == int(update)).first()
            print()
            completion_status = input("Is the task completed? (yes/no): ").lower()
            print()
            if completion_status == "yes":
                updated_task.completed = True
                print()
                delete = input("Would you like to delete your completed task? (yes/no): ").lower()
                print()
                if delete == "yes":
                    session.delete(updated_task)
                    print()
                    print("You are now being logged out")
                    print()
                else:
                    print()
                    print("You are now being logged out")
                    print()


                    

            else:
                updated_task.completed = False
                print()
                print("You are now being logged out")
                print()
            


        else:   
                print()
                print("You are now being logged out")
                print()
        
        
        session.commit()
        
            


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
