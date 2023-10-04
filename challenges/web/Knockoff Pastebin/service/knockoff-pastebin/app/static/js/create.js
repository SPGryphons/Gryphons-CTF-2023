const show_message = (msg) => {
  $('.error').css('display', 'block')

  if (msg) {
    $('.error').html(msg)
  }

  setTimeout(() => {
      $('.error').css('display', 'none')
  }, 10000)
}

const create = () => {
  let content = $('#content').val();
  if (!content) {
    show_message('Please input content')
    return;
  }

  fetch('/api/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      content: content
    })
  })
  .then(res => {
    if (res.status === 200) {
      if (res.url.includes('login')) {
        window.location.replace('/login')
      }
      res.json().then(data => {
        window.location.replace('/view/' + data['link'])
      })
    } else if (res.status === 429){
      show_message('Too many requests, please try again later')
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