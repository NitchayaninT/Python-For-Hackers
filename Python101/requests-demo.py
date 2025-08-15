import requests

# Basic GET request
# x is the response object
x = requests.get('http://httpbin.org/get')

# look at the response headers
print(x.headers)
print(x.headers['Server'])
print(x.status_code)

if x.status_code == 200:
    print("Success!")
elif x.status_code == 404:
    print("Not Found!")

# how much time  from sending request to receiving response
# Useful for performing timing attack (like when performing SQL Injection and put SLEEP(5) in the payload)
# IF the sleep is actually executed, that means the injection is a success
x = requests.get('http://httpbin.org/get')
print(x.elapsed)
# All cookies sent back from the server in the response
print(x.cookies)
# Response body
print(x.text)

# Sending Query parameters. Automatically encodes them and appends to the url
x = requests.get('http://httpbin.org/get', params={'id':'1'})
print(x.url) # id=1 has been added to the request

# Same as above but append directly
x = requests.get('http://httpbin.org/get?id=2')
print(x.url)

# Adding custom headers
# Accept : Application/json tells the server we prefer JSON
x =  requests.get('http://httpbin.org/get', params={'id':'3'}, headers={'Accept':'application/json', 'test_header':'test'})
print(x.text)

# Delete Request (HTTP DELETE request)
x = requests.delete('http://httpbin.org/delete')
print(x.text)

# File Upload
files = {'file':open('google.png','rb')}
x = requests.post('http://httpbin.org/post', files=files)
print(x.text)

# Basic authentication
# Auth = tuple of (username, password) for HTTP Basic Auth
x = requests.get('http://httpbin.org/get', auth=('username','password'))
# Authorization : Basic 'encoded base64 of username:password'
print(x.text)

# Ignoring SSL errors. It disables SSL certificate verification
x = requests.get('http://expired.badssl.com', verify=False)

# Disabling redirects
# Normally http://github.com redirects to https://github.com
# This prevents auto-following
x = requests.get('http://github.com', allow_redirects=False)
print(x.headers)

# Specify timeout to stop waiting for a response
# If the server doesn’t respond in time, raises requests.exceptions.Timeout
x = requests.get('http://httpbin.org/get',timeout=0.01)
print(x.content)

# Sending Cookies
# cookies → dictionary of cookies to send in the request.
# Server will see Cookie: a=b
x = requests.get('http://httpbin.org/cookies', cookies={'a':'b'})
print(x.content)

# Session Cookies
# Session() object maintains cookies across requests automatically.
x = requests.Session()
x.cookies.update({'a':'b'})
print(x.get('http://httpbin.org/cookies').text)

# JSON response parsing
#.json() parses JSON response body into Python data structures (dict/list)
x = requests.get('http://api.github.com/events')
print(x.json())

# Downloading binary data
# wb mode writes binary data to file.
x = requests.get('https://www.google.com/webhp?hl=en&ictx=0&sa=X&ved=0ahUKEwiSvMPY_4yPAxV5XGwGHcBpHzcQpYkNCAo')
with open('google2.png','wb') as f:
    f.write(x.content)