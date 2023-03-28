import domain.user.repository as Repository

def create_user(user):
    print("controller", user)
    return Repository.creat_user(user)

def get_all_user():
    return Repository.get_all_user()