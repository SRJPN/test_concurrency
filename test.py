import requests
import json
import grequests

url = "http://127.0.0.1:8001/current-spend-summary/0994f047-cd7c-4b95-9ccd-70abc69db8d3"

payload = json.dumps({
  "cleared_balance": "0.00",
  "reward_balance": "30.00"
})

another_payload = json.dumps({
  "cleared_balance": "0.00",
  "reward_balance": "10.00"
})

headers = {
  'Content-Type': 'application/json'
}

grequests.map(rs)
another_response = grequests.put("PUT", "http://127.0.0.1:8000/current-spend-summary/0994f047-cd7c-4b95-9ccd-70abc69db8d3", headers=headers, data=another_payload)
response = requests.request("PUT", "http://127.0.0.1:8001/current-spend-summary/0994f047-cd7c-4b95-9ccd-70abc69db8d3", headers=headers, data=payload)

print(response.text)
print(another_response.text)
