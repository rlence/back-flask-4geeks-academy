from models import User, db

def creat_user(user):
    try:
        print('REPOSITORY', user)
        new_user = User(user['email'], user['password'])
        print('Repository',new_user)
        db.session.add(new_user)
        db.session.commit()
        return new_user.serialize()

    except Exception as err:
        print('ERROR',err)


def get_all_user():
    try:
        list_user = User.query.all()
        print(list_user)
        return [user.serialize() for user in list_user]
    except Exception as err:
        print(err)