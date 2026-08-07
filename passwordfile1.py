class User:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password
    def check_password(self,password):
        if self.__password==password:
            print("Password is True")
            return True
        else:
            print("Password is false")
            return False
    def change_password(self,old,new):
        if self.check_password(old):
            self.__password=new