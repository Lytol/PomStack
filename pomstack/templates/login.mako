<%inherit file="layout.mako"/>

${form.begin(request.route_url('login'))}
  ${form.csrf_token()}
  <ul>
    <li>
      ${form.errorlist('email')}
      ${form.label('email', 'Email:')}
      ${form.text('email')}
    </li>
    <li>
      ${form.errorlist('password')}
      ${form.label('password', 'Password:')}
      ${form.password('password')}
    </li>
    <li>
      ${form.submit('submit', 'Login')}
    </li>
  </ul>
${form.end()}
