from uti.configuration import *

query = 'update Books set aisle=%s where Bookname=%s'
data = (88,'Devops')

getquery(query,data)

