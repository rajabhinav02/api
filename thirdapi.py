import json

with open("C:\\Users\\Punam\\Desktop\\json files\\secondexpense.json") as hi:
    data=json.load(hi)
    #print(data)
   # print(data["WEEK"])
    for na in data:
        if na["WHO"]=="Joe":
            #print (na["WEEK"])
            for ca in na["WEEK"]:
                if ca["NUMBER"] ==4:
                    #print (ca["EXPENSE"])
                    for da in ca["EXPENSE"]:
                        if da["WHAT"]=="Beer":
                            print(da["AMOUNT"])

    print ("########"*10)
    for hd in data:
        for jd in hd["WEEK"]:
            for ld in jd["EXPENSE"]:
                #for kd in ld["WHAT"]:
                if ld["WHAT"]=="Beer":
                    print(ld["AMOUNT"])
    print("*************"*20)
    for ol in data:

        for pl in ol["WEEK"]:
            if pl["NUMBER"]==5:
                for hl in pl["EXPENSE"]:
                    if hl["WHAT"]=="Car":
                        print(hl["AMOUNT"])

    print ("&"*20)
    for tf in data:
        if tf["WHO"]=="Janet":
            for yf in tf["WEEK"]:
                if yf["NUMBER"]==4:
                    for uf in yf["EXPENSE"]:
                        if uf["WHAT"]=="Car":
                            print(uf["AMOUNT"])
                        else:
                            print("None")
    print("%"*100)

    for te in data:
        for ye in te["WEEK"]:
            if ye["NUMBER"]==5:
                for re in ye["EXPENSE"]:
                    if re["WHAT"]== "Food":
                        print(re["AMOUNT"])






"""
    for name in data:
        if name["WHO"] == "Beth":
            for exp in data["WEEK"]:
                if exp["NUMBER"]== 4 and exp["EXPENSE"]["WHAT"]=="Beer":
                    print (exp["EXPENSE"]["AMOUNT"])
"""














print("############"*20)

with open("C:\\Users\\Punam\\Desktop\\json files\\secondexpense.json") as row:
    daga = json.load(row)

    for da in daga:
        if da["WHO"]=="Joe":
            for ga in da["WEEK"]:
                if ga["NUMBER"] == 3:
                    for ha in ga["EXPENSE"]:
                        if ha["WHAT"]=="Food":
                            print(ha["AMOUNT"])

