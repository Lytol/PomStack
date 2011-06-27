<%inherit file="layouts/dashboard.mako"/>

${form.begin(request.route_url('add_pomodoro'))}
  ${form.csrf_token()}
  <ul>
    <li>
      ${form.errorlist('title')}
      ${form.label('title', 'Title')}
      ${form.text('title')}
    </li>
    <li>
      ${form.submit('submit', 'Add')}
    </li>
  </ul>
${form.end()}
