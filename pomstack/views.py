from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from pyramid.security import authenticated_userid, remember, forget

import formencode
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

from pomstack.models import DBSession
from pomstack.models import User, Pomodoro


@view_config(permission='public', route_name='home', renderer='home.mako')
def home(request):
    return dict()

class SignupSchema(formencode.Schema):
    allow_extra_fields = False
    email = formencode.validators.Email(resolve_domain=False)
    password = formencode.validators.String(not_empty=True)
    password_confirmation = formencode.validators.String(not_empty=True)
    chained_validators = [
        formencode.validators.FieldsMatch('password','password_confirmation')
    ]

@view_config(permission='public', route_name='signup', renderer='signup.mako')
def signup(request):
    form = Form(request, schema=SignupSchema)

    if request.method == 'POST' and form.validate():
        session = DBSession()
        user = User(
            email=form.data['email'],
            password=form.data['password']
        )
        session.add(user)
        headers = remember(request, user.email)
        redirect_url = route_url('dashboard', request)
        return HTTPFound(location=redirect_url, headers=headers)

    return dict()

@view_config(permission='public', route_name='login', renderer='login.mako')
def login(request):
    if request.method == "POST":
        email = request.params['email']
        password = request.params['password']
        if User.check_password(email, password):
            headers = remember(request, email)
            return HTTPFound(location=route_url('dashboard', request),
                            headers=headers)
      
    return dict()

@view_config(permission='auth', route_name='logout', renderer='logout.mako')
def logout(request):
    request.session.invalidate()
    headers = forget(request)
    return HTTPFound(location=route_url('home', request),
                    headers=headers)

@view_config(permission='auth', route_name='dashboard', renderer='dashboard.mako')
def dashboard(request):
    session = DBSession()
    pomodoros = session.query(Pomodoro)
    return dict(pomodoros=pomodoros)

@view_config(permission='auth', route_name='add_pomodoro', renderer='add_pomodoro.mako')
def add_pomodoro(request):
    if request.method == "POST":
        session = DBSession()
        title = request.params['title']
        pomodoro = Pomodoro(title)
        session.add(pomodoro)
        return HTTPFound(location = route_url('dashboard', request))

    pomodoro = Pomodoro('')
    return dict(pomodoro=pomodoro)

