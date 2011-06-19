def view_root(context, request):
    return {'items':list(context), 'project':'PomStack'}

def view_model(context, request):
    return {'item':context, 'project':'PomStack'}
