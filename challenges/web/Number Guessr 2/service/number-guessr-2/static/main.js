const alertPlaceholder = $('#alert-placeholder')

const show_message = (message, type, timeout=true) => {
  let alert = $([
      `<div class="alert alert-${type} alert-dismissible" role="alert">`,
      `   <div>${message}</div>`,
      '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
      '</div>'
    ].join(''))
  alertPlaceholder.append(alert)

  if (timeout) {
    setTimeout(() => {
      alert.alert('close')
    }, 5000)
  }
}

var score = 0;

const update_score = () => {
  $('#score').text("Your score is: " + score);
}

const ws = new WebSocket("ws://" + window.location.host + "/ws");

ws.onmessage = (event) => {
  let data;
  try {
    data = JSON.parse(event.data);
  } catch (error) {
    show_message("Invalid JSON: " + event.data, "danger");
    return;
  }

  if (data["type"] == "guess_result") {
    if (data["result"] == "correct") {
      show_message("Correct!", "success");
    } else if (data["result"] == "incorrect") {
      show_message("Incorrect! I chose " + data["number"] + "!", "danger");
    }
    score = data["score"];
    update_score();
  }
  else if (data["type"] == "flag") {
    show_message("The flag is " + data["flag"], "success", false);
  }
}

const guess = () => {
  const number = $('#guess').val();
  if (!number) {
    show_message("Please enter a number!", "warning");
    return;
  } else if (number < 1 || number > 100) {
    return;
  }

  if (ws.readyState != ws.OPEN) {
    show_message("Not connected to server, please reload the page" , "danger");
    return;
  }

  ws.send(JSON.stringify({
    "type": "guess",
    "number": number
  }));

  $('#guess').val('');
}

$('#guess-btn').click(guess);