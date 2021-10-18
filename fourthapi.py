import json

with open("C:\\Users\\Punam\\Desktop\\json files\\thirdcolor.json") as li:

    data= json.load(li)

#with open("C:\\Users\\Punam\\Desktop\\json files\\secondexpense.json") as hi:
    #data = json.load(hi)

    for da in data["colors"]:
        if da["color"]=="red":
            print (da["code"]["hex"])