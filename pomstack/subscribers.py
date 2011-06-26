from pyramid.httpexceptions import HTTPForbidden


def csrf_validation(event):
    if event.request.method == "POST":
        token = event.request.POST.get("_csrf")
        if token is None or token != event.request.session.get_csrf_token():
            raise HTTPForbidden('CSRF token is missing or invalid')

