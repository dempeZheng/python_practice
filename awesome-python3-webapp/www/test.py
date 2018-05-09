'another sql check code'
from  models import User
async def print_user():
    data = await User.findAll()
    for d in data:
        print(d)


if __name__ == '__main__':
    print_user()