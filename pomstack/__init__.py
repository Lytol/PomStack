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

    config.add_route('dashboard', '/', view='pomstack.views.dashboard', renderer='dashboard.mako')

    return config.make_wsgi_app()


