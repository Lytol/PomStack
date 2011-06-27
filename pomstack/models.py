import transaction
import cryptacular.bcrypt

from pyramid.security import Everyone
from pyramid.security import Authenticated
from pyramid.security import Allow

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import synonym
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import Column

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
crypt = cryptacular.bcrypt.BCRYPTPasswordManager()

def hash_password(password):
    return unicode(crypt.encode(password))

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(Unicode(50))

    _password = Column('password', Unicode(60))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def get_by_email(cls, email):
        return DBSession.query(cls).filter(cls.email==email).first()

    @classmethod
    def check_password(cls, email, password):
        user = cls.get_by_email(email)
        if not user:
            return False
        return crypt.check(user.password, password)
    

class Pomodoro(Base):
    __tablename__ = 'pomodoros'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(Unicode(255), unique=True)

    user = relationship(User, backref=backref('pomodoros', order_by=id))

    def __init__(self, title):
        self.title = title


class RootFactory(object):
    __acl__ = [
        (Allow, Everyone, 'public'),
        (Allow, Authenticated, 'auth')
    ]
    def __init__(self, request):
        pass

