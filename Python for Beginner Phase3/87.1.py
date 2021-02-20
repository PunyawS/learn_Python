#Assignment โปรแกรมคำนวณเกรดนักเรียน

try:
    fr=open("./text/assignment.txt","r",encoding="UTF-8")
    fw=open("./text/Grade.txt","a",encoding="UTF-8")
    s=fr.readlines()
    grade=None
    for i in s:
        codeid=i[:4]
        score=i[-3:-1].strip() #.strip del gap
        score=int(score)
        if score >= 80:
            grade = "A"
        elif score >= 70 and score <80:
            grade = "B"
        elif score >= 60 and score <70:
            grade = "C"
        print("Code ID :",codeid,"Score :",score,"Grade :",grade)
        fw.writelines(codeid+str(score)+"\t"+grade+"\n")
    fw.close()
except Exception as a:
    print(a)