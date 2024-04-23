import json
slips=[]
with open('东方签文（时间序）.txt', 'r',encoding="UTF-8") as file: 
    lines = file.readlines() 
    i=0
    while 1:
        try:
            if lines[i][0:-1].isdigit():
                id=lines[i][0:-1]
                content=[]
                sign=""
                while 1:
                    i+=1
                    if lines[i]!="\n" and lines[i][0:2]!="by":
                        content.append(lines[i][0:-1])
                    print(lines[i][0:2])
                    if lines[i][0:2]=="by":
                        sign=lines[i][0:-1]
                    if lines[i]=="\n":
                        break
                slips.append({"id":id,"content":content,"sign":sign})
            i+=1
        except:
            slips.append({"id":id,"content":content,"sign":sign})
            break
j=json.dumps({"slips":slips},ensure_ascii=False,indent=4)
with open('./Touhou_Fourtune_Slips.json', 'w',encoding="UTF-8") as f:
    f.write(j)
