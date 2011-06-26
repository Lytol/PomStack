from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import unauthenticated_userid

from pomstack.models import DBSession
from pomstack.models import User

class RequestWithUserAttribute(Request):
    @reify
    def user(self):
        session = DBSession()
        user_email = unauthenticated_userid(self)
        if user_email is not None:
            # this should return None if the user doesn't exist
            # in the database
            return session.query(User).filter(User.email==user_email).first()

