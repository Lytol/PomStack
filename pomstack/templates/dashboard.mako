<%inherit file="layouts/dashboard.mako"/>

<ul id="pomodoros">

  <li class="add">
    <a href="${request.route_url('add_pomodoro')}">Add a Pomodoro</a>
  </li>

  % for pomodoro in pomodoros:
    <li>${pomodoro.title}</li>
  % endfor
</ul>
