import json

with open("C:\\Users\\Punam\\Downloads\\example_2.json") as re:

    data=json.load(re)
    print(data)
    #print(data["quiz"]["maths"]["q1"]["options"][1])

    #print(data["quiz"]["maths"]["q2"]["options"])

    for course in data["quiz"]["maths"]["q2"]["options"]:
        print(course)
        if course["naa"]== "2":
            print(course["kaa"])

    for co in data["quiz"]["maths"]["q2"]["options"]:
        print(co)
        print(co["naa"])
