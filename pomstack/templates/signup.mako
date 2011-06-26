<%inherit file="layout.mako"/>

<form action="${request.route_url('signup')}" method="POST">
  <ul>
    <li>
      <label for="user_email">Email</label>
      <input type="text" name="email" id="user_email" />
    </li>
    <li>
      <label for="user_password">Password</label>
      <input type="password" name="password" id="user_password" />
    </li>
    <li>
      <label for="user_password_confirmation">Password (again)</label>
      <input type="password" name="password_confirmation" id="user_password_confirmation" />
    </li>
    <li>
      <input type="submit" value="Signup" />
    </li>
  </ul>
</form>
