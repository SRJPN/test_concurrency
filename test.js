var request = require('request');
id = "d374ad28-7185-4eaa-bf25-7d1658825900"
var options = {
  'method': 'PUT',
  'url': `http://127.0.0.1:8001/current-spend-summary/${id}`,
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
    'url': `http://127.0.0.1:8000/current-spend-summary/${id}`,
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
