import json
from lession2.User import User

if __name__ == '__main__':
    # user = User()
    # user.name = 'Trung'
    # print(user)
    # print(repr(user))
    # print(user.get_email_data())
    # print(user.get_phone())
    b = User(name='Trung', age='20', roleName='Dev', address='Hanoi', phone='0123456789')
    print(b)
    print(b.get_phone())
    # # Get from JSON
    # with open('data.json', 'r') as file:
    #     data = json.load(file)
    #
    # users = [User(name=item['name'], age=item['age'], roleName=item['roleName'], address=item['address']) for item in data]
    # for user in users:
    #     print(user)
    #     print(user.get_email_data())