import requests
import json
from payload import *
from utilities.configuration import *
from utilities.resources import *

baseurl = getconfiguration()['API']['endpoint_url']+Resources.addbook
response= requests.post(baseurl, json= addbook("hjgf", "987"),)


response_json = response.json()
print(response_json)
print(response_json['ID'])

responsedel = requests.post('http://216.10.245.166/Library/DeleteBook.php', json= {

"ID" : response_json['ID']

}
)

print (responsedel.json())