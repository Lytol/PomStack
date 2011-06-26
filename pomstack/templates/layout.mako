<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Dashboard &mdash; PomStack</title>
  </head>
  <body>
    <div id="header">
      <ul id="header-nav">
        % if request.user:
          <li class="logout">${request.user.email} (<a href="${request.route_url('logout')}">logout</a>)</li>
        % else:
          <li class="login"><a href="${request.route_url('login')}">login</a></li>
          <li class="signup"><a href="${request.route_url('signup')}">signup</a></li>
        % endif
      </ul>
      
    </div>

    ${next.body()}

  </body>
</html>
