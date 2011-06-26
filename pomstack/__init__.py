import os

from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from pomstack.helpers import RequestWithUserAttribute

from pomstack.models import initialize_sql
from sqlalchemy import engine_from_config


def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    if 'sqlalchemy.url' not in settings:
        settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL')

    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    session_factory = UnencryptedCookieSessionFactoryConfig('dubb5oxalic')
    authn_policy = AuthTktAuthenticationPolicy('dubb5oxalic')
    authz_policy = ACLAuthorizationPolicy()

    settings['mako.directories'] = 'pomstack:templates'

    config = Configurator(
        settings=settings,
        root_factory='pomstack.models.RootFactory',
        authentication_policy=authn_policy,
        authorization_policy=authz_policy,
        session_factory=session_factory
    )

    config.set_request_factory(RequestWithUserAttribute)
    
    config.add_static_view('static', 'pomstack:static')

    """ Routes
    """
    config.add_route('home', '/')
    config.add_route('signup', '/signup')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('dashboard', '/dashboard')
    config.add_route('add_pomodoro', '/pomodoros/add')

    config.scan()

    return config.make_wsgi_app()


