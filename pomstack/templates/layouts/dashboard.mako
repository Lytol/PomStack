<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Dashboard &mdash; PomStack</title>

    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
    <script src="/static/js/jquery-1.6.1.min.js" type="text/javascript"></script>
  </head>
  <body>
    <div id="header">
      <h1>PomStack</h1>

      <div id="header-menu">
        <span class="email">${request.user.email}</span>
        <ul>
          <li class="logout"><a href="${request.route_url('logout')}">logout</a></li>
        </ul>
      </div>

      % if request.session.peek_flash():
        % for message in request.session.pop_flash():
          <p id="flash-message">${message}</p>
        % endfor
      % endif
      
    </div>
    <div id="content">

      ${next.body()}

    </div>
  </body>
</html>
