from lession2.Role import Role

class User(Role):
    def __init__(self, name='No Name', age='No Email', roleName='No Role', address='No Address', phone='No Phone'):
        super().__init__(roleName, address, phone)
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} <{self.age}>, Role: {self._Role__roleName}, Address: {self._Role__address}'

    def __repr__(self):
        return f'{self.name} Age:{self.age}, Role: {self._Role__roleName}, Address: {self._Role__address}'

    def get_email_data(self):
        return {
            'name': self.name,
            'age': self.age
        }

    def get_phone(self):
        return self._Role__phone

    def set_name(self, name):
        self.name = name