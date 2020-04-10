

from flask import Request






class Users_details():

    def __init__(self,request: Request):
    #def __init__(self, x):
        self.request = request

    def get(self, **kwargs):
        print ("ssssssssssssssssssss {}".format(kwargs))
        return "Hello i am here"
