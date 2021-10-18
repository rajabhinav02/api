import requests
import json

response=requests.get(url='http://216.10.245.166/Library/GetBook.php', params={'AuthorName':'Rahul Shetty'},)
#print(response.text)
""""
response_json= json.loads(response.text)
print(response_json)

for res in response_json:
    if res['book_name']== 'Devops':
        print (res['isbn'])
        print(type(res['isbn']))
"""
response_json = response.json()
print(response.text)
for res in response_json:
    #print(res)
    if res['isbn'] == 'RGHCC':
        print(res)
        print(res['book_name'])
        break
        #assert res['isbn']== 'bnid34' or res['isbn'] == 'abcd' or res['isbn']=='asdasadsdas'
        #print(type(res['isbn']))
expected_res =  {
        "book_name": "Learn with Java",
        "isbn": "RGHCC",
        "aisle": "222"
    } or {
        "book_name": "Learn with Java",
        "isbn": "RGHCC",
        "aisle": "22233"
    } or {
        "book_name": "Learn with Java",
        "isbn": "RGHCC",
        "aisle": "2223355"
    } or {
        "book_name": "Learn with Java",
        "isbn": "RGHCC",
        "aisle": "2675"
    } or {
        "book_name": "Learn with Java",
        "isbn": "RGHCC",
        "aisle": "2675890"
    }

assert res == expected_res

print(response.status_code)
print(response.headers)
assert response.headers['Content-Type']=='application/json;charset=UTF-8'