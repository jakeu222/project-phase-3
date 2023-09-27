# lib/cli.py
from models.model_1 import *
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from helpers import (
    exit_program,
    helper_1
)
# import inquirer
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
        
        i1 = input("Please enter your username: ")
        one_user = session.query(User).filter(User.full_name == i1).first()
        if one_user:
            print("User profile exists")
            i5 = input("Do you want to create a new task? (yes/no): ")
            if i5 == "yes":


                i2 =input("Please enter a new task description: ")
                new_task = Task(task=i2, user=one_user)

            

                session.add(new_task)
                session.commit()

        else:
            print("Sorry, user not found")
            i3 = input("Please input your new user name: ")
            n_user_name = User(full_name=i3)
            session.add(n_user_name)
            i5 = input("Do you want to create a new task? (yes/no): ")
            if i5 == "yes":

                i4 = input("Please enter a new task description: ")
                new_task = Task(task=i4, user=n_user_name)

                session.add(new_task)
                session.commit()

        display = input("Do you want to display your tasks to update or delete? (yes/no): ").lower()
        if display == "yes":
            usertasks = session.query(Task).filter(Task.user == one_user).all()
            print(usertasks)
            update = input("Choose task id: ")
            updated_task = session.query(Task).filter(Task.id == int(update)).first()
            completion_status = input("Is the task completed? (yes/no): ").lower()
            if completion_status == "yes":
                updated_task.completed = True
                delete = input("Delete? (yes/no): ").lower()
                if delete == "yes":
                    session.delete(updated_task)
                    

            else:
                updated_task.completed = False

        else:
                pass
        
        
        session.commit()
        
            


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
