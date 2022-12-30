class User:
    def __init__(self,name , id):
        self.id = id
        self.name = name

    def get_name(self)-> str:
        return self.name

    def get_id(self):
        return self.id

db_users = []

def add_user(name: str):
    usr = User(name , len(db_users))
    db_users.append(usr)

def remove_user(name: str):

    for i in range(len(db_users)):
        if db_users[i].get_name() == name:
            db_users.remove(i)
            return 0 
    return -1
def get_users():
    return db_users