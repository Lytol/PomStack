<%inherit file="layout.mako"/>

<form action="${request.route_url('add_pomodoro')}" method="POST">
  <ul>
    <li>
      <label for="pomodoro_title">Title</label>
      <input type="text" name="title" id="pomodoro_title" />
    </li>
    <li>
      <input type="submit" value="Add" /> or <a href="${request.route_url('dashboard')}">cancel</a>
    </li>
  </ul>
</form>
