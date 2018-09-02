import requests
r = requests.get('https://webhook.site/9915eb94-ee00-4e62-b2b3-5665d7b7732d')
s = requests.get('https://webhook.site/9915eb94-ee00-4e62-b2b3-5665d7b7732d')
t = requests.get('https://webhook.site/9915eb94-ee00-4e62-b2b3-5665d7b7732d')
print (r.headers['date'])
print (s.headers['date'])
print (t.headers['date'])