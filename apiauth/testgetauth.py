import requests
from apiauth.utilitiesk.resourcess import *
from apiauth.utilitiesk.configurationn import *

burl = getconfig()['API']['endpoint']+Resource.getresource
se=requests.session()
se.auth= auth = ('io', getpwd())


resp = se.get(burl,timeout = 1)
print(resp)
print(resp.text)
print(type(resp.text))
print (resp.json())
print (resp.status_code)

