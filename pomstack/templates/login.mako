<%inherit file="layout.mako"/>

<form action="${request.route_url('login')}" method="POST">
  <ul>
    <li>
      <label for="email">Email</label>
      <input type="text" name="email" id="email"/>
    </li>
    <li>
      <label for="password">Password</label>
      <input type="password" name="password" id="password"/>
    </li>
    <li>
      <input type="submit" value="login"/>
    </li>
  </ul>
</form>
