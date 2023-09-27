from sqlalchemy import Column, Boolean, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user_table'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    # age = Column(Integer)

    tasks = relationship("Task", back_populates="user")

class Task(Base):
    __tablename__ = 'task_table'

    id = Column(Integer, primary_key=True)
    task = Column(String)
    completed = Column(Boolean, default=False)

    user_id =Column(Integer, ForeignKey("user_table.id"))

    user = relationship("User", back_populates="tasks")

    def __repr__(display):
        return f"Task(id={display.id}, task='{display.task}')"

    

if __name__ == '__main__':
    engine = create_engine("sqlite:///todo.db")

    # User.__table__.drop(engine)
    # Task.__table__.drop(engine)

    Base.metadata.create_all(engine)

#     with Session(engine) as session:
#         # all_users = session.query(User).order_by(User.full_name.desc()).all()
#         # for user in all_users:
#         #     print(user.full_name)




#         i1 = input("Please enter your username: ")
#         one_user = session.query(User).filter(User.full_name == i1).first()
#         if one_user:
#             print("User profile exists")

#             i2 =input("Please enter a new task description: ")
#             new_task = Task(task=i2, user=one_user)
            
#             # completion_status = input("Is the task completed? (yes/no): ").lower()
#             # if completion_status == "yes":
#             #     new_task.completed = True
#             #     # if new_task.completed == True:
#             #     #     session.delete(new_task)
#             # else:
#             #     new_task.completed = False

#             session.add(new_task)
#             session.commit()

#         else:
#             print("Sorry, user not found")
#             i3 = input("Please input your new user name: ")
#             n_user_name = User(full_name=i3)
#             session.add(n_user_name)

#             i4 = input("Please enter a new task description: ")
#             new_task = Task(task=i4, user=n_user_name)

#             # session.add(new_task)

#             # completion_status = input("Is the task completed? (yes/no): ").lower()
#             # if completion_status == "yes":
#             #     new_task.completed = True
#             #     # if new_task.completed == True:
#             #     #     session.delete(new_task)
#             # else:
#             #     new_task.completed = False

            
#             session.add(new_task)
#             session.commit()

#     #    current_user = session.query(Task).filter(

            


#         session.commit()
        
#             # i2 = input("What do you want to change the username to? ")
#             # one_user.full_name = i2
#             # # session.add(one_user)
#             # session.add(one_user)
#             # session.commit()

#         # user_age = input("Input user age")
#         # n_user_age = User(age=user_age)



#         # # # jake = User(full_name = "Jake", last_name = "Underwood", age = 29)
#         # # # session.add(jake)
#         # session.add(n_user_age)
        

#         # print(n_user.id)







