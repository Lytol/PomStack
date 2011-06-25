from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url

from pomstack.models import DBSession
from pomstack.models import Pomodoro


def dashboard(request):
    return {'project':'PomStack'}

def add_pomodoro(request):
    if request.method == "POST":
        session = DBSession()
        title = request.params['title']
        pomodoro = Pomodoro(title)
        session.add(pomodoro)
        return HTTPFound(location = route_url('dashboard', request))

    pomodoro = Pomodoro('')
    return dict(pomodoro=pomodoro)

