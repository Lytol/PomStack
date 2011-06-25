from pyramid.config import Configurator

from pomstack.models import initialize_sql
from sqlalchemy import engine_from_config


def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    settings['mako.directories'] = 'pomstack:templates'

    config = Configurator(settings=settings)
    config.add_static_view('static', 'pomstack:static')

    config.add_route('dashboard', '/')
    config.add_view('pomstack.views.dashboard',
                    route_name='dashboard',
                    renderer='dashboard.mako')
    
    config.add_route('add_pomodoro', '/pomodoros/add')
    config.add_view('pomstack.views.add_pomodoro',
                    route_name='add_pomodoro',
                    renderer='add_pomodoro.mako')

    return config.make_wsgi_app()


