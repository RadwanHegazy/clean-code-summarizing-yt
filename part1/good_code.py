from dataclasses import dataclass

MAX_OFFLINE_DAYS : int = 30

@dataclass()
class User:
    name : str
    email : str
    offline_days : int

    @property
    def is_offline(self) -> bool: 
        return self.offline_days > MAX_OFFLINE_DAYS
    
def get_inactive_users(list_of_users : list[User]) -> list[User]:
    list_inactive_users = []
    for user in list_of_users:
        if user.is_offline:
            list_inactive_users.append(user)
    return list_inactive_users

list_of_users : list[User] = [
    User(name="Ahmed",email="ahmed@email.com",offline_days=35),
    User(name="Ali",email="ali@email.com",offline_days=10),
]

print(get_inactive_users(list_of_users))


