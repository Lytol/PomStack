from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pomstack.models import appmaker

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    get_root = appmaker(engine)

    settings['mako.directories'] = 'pomstack:templates'

    config = Configurator(settings=settings, root_factory=get_root)

    config.add_static_view('static', 'pomstack:static')
    config.add_view('pomstack.views.view_dashboard', renderer="dashboard.mako")

    return config.make_wsgi_app()


