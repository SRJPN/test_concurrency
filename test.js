var request = require('request');
var options = {
  'method': 'PUT',
  'url': 'http://127.0.0.1:8001/current-spend-summary/0994f047-cd7c-4b95-9ccd-70abc69db8d3',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "cleared_balance": "100.00",
    "reward_balance": "30.00"
  })
};

var another_options = {
    'method': 'PUT',
    'url': 'http://127.0.0.1:8000/current-spend-summary/0994f047-cd7c-4b95-9ccd-70abc69db8d3',
    'headers': {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "cleared_balance": "100.00",
      "reward_balance": "40.00"
    })
  };
// 800
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(options.url, response.body);
});

request(another_options, function (error, response) {
    if (error) throw new Error(error);
    console.log(options.url, response.body);
  });
