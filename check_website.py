import requests
def alert( msg, exit_code ):
  print(msg)
  exit(exit_code)

try:
  response = requests.get("http://csit.iceage.me.uk")
  #response = requests.get("http://google.com")

  if response.status_code == 200:
    print "Response received successfully",response.status_code
    if response.content == 'Hello, you are viewing file version .. 1.7.0':
      alert("Ok - Response is correct", 0)
    else:
      alert("Warning - Response is wrong", 1)
  else:
    alert("Critical - Server is Down", 2)
except Exception as e:
  alert("Critical - Server is Down", 2)
