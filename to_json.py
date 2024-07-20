import json
import os
slips_main=[]

def txtToJson(filename:str):
    slips=[]
    with open(filename,'r',encoding="UTF-8") as file:
        lines = file.readlines()
        i=0
        id=1
        while 1:
            try:
                if lines[i].strip()!="" and lines[i][0]!="#":
                    content=[]
                    sign=""
                    while 1:
                        if lines[i]!="\n" and lines[i][0:2]!="by":
                            content.append(lines[i][0:-1])
                        if lines[i][0:2]=="by":
                            sign=lines[i][0:-1]
                        if lines[i]=="\n":
                            break
                        i+=1
                    slips.append({"id":str(id),"content":content,"sign":sign})
                    id+=1
                i+=1
            except:
                slips.append({"id":str(id),"content":content,"sign":sign})
                break
    if filename == "东方签文.txt":
        global slips_main
        slips_main = slips.copy()
    else:
        for item in slips:
            item["id"]="0"+item["id"]
        slips = slips + slips_main
    j=json.dumps({"slips":slips},ensure_ascii=False,indent=4)
    with open('./Touhou_Fortune_Slips'+filename[5:-4]+'.json', 'w',encoding="UTF-8") as f:
        f.write(j)



txtToJson("东方签文.txt")
for filename in os.listdir("./"):
    if filename[0:4] == "东方签文" and filename != "东方签文（作品序）.txt" and filename != "东方签文.txt":
        txtToJson(filename)