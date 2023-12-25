const show_message = (msg) => {
  $('.error').css('display', 'block')

  if (msg) {
    $('.error').html(msg)
  }

  setTimeout(() => {
      $('.error').css('display', 'none')
  }, 10000)
}

const login = () => {
  let username = $('#username').val();
  let password = $('#password').val();
  let otp = $('#otp').val();

  if (!username || !password || !otp) {
    show_message('Please fill in all fields');
    return;
  }

  fetch('/api/login', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          'username': username,
          'password': password,
          'otp': otp
      })
  })
  .then(res => {
    if (res.status === 200) {
      res.json().then(data => {
        document.cookie = `token=${data['token']};`;
        window.location.replace('/profile');
      })
    } else {
      res.json().then(data => {
        show_message(data['error']);
      })
    }
  }).catch((err) => {
    if (err) {
      console.log(err);
    }
  })
}