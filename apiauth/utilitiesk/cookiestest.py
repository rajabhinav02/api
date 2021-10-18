import requests
import json
from apiauth.utilitiesk.configurationn import *
from apiauth.utilitiesk.resourcess import *

byurl = getconfig()['API']['endpoint']+Resource.getcookies
df = requests.session()
df.cookies.update({'name': 'raj'})
cookie = {'email': 'lol'}

res= df.get(byurl, verify = False, allow_redirects=False , cookies = cookie, timeout = 2)
print(res.text)
print(res.status_code)
print(res.history)

jkurl = getconfig()['API']['endpoint2']+Resource.uploadimage
Files= {'File': open('C:\\Users\\Punam\\Desktop\\Harish_1.jpg', 'rb')}
rt = requests.post(jkurl, files=Files)
print(rt.text)
print(rt.status_code)