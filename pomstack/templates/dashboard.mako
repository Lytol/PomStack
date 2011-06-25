<%inherit file="layout.mako"/>

<ul class="actions">
  <li><a href="${request.route_url('add_pomodoro')}">Add a Pomodoro</a></li>
</ul>

<ul id="pomodoros">
  % for pomodoro in pomodoros:
    <li>${pomodoro.title}</li>
  % endfor
</ul>
