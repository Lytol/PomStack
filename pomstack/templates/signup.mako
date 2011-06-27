<%inherit file="layouts/public.mako"/>

${form.begin(request.route_url('signup'))}
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
      ${form.errorlist('password_confirmation')}
      ${form.label('password_confirmation', 'Confirm password:')}
      ${form.password('password_confirmation')}
    </li>
    <li>
      ${form.submit('submit', 'Signup')}
    </li>
  </ul>
${form.end()}

