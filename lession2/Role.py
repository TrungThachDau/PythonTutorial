class Role:
    def __init__(self, roleName, address, phone):
        self.__roleName = roleName
        self.__address = address
        self.__phone = phone

    def print(self):
        print(f'Role: {self.__roleName}, Address: {self.__address}')