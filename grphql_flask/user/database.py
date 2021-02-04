from mongoengine import connect

from models import UserInfo

connect('gursheesh', host='localhost:27017', alias='default')

def init_db():
    user_obj = UserInfo(name='Engineering')
    user_obj.save()
    