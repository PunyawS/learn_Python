
def inputscoretest():
    try:
        fw=open("./Text/testassignment.txt","w",encoding="UTF-8")
    
        while True:
            x=(input("Ples input code :"))
            if not type(x) is str:
                raise Exception
            if x == "exit":
                break
            y=(input("Ples input score :"))
            fw.writelines(x+"\t"+y+"\n")
        fw.close()

    except Exception as a:
        print(a)

def gradescore():
    try:
        fr=open("./Text/testassignment.txt","r",encoding="UTF-8")
        fw=open("./Text/testassignment1.txt","w",encoding="UTF-8")
        s=fr.readlines()
        grade = None
        for i in s:
            codeid=i[:4]
            score=i[-3:].strip()
            score=int(score)
            if score >= 80:
                grade = "A"
            elif score < 80 and score >= 70:
                grade = "B"
            elif score < 70 and score >= 60:
                grade = "C"
            elif score < 60 and score >= 50:
                grade = "D"
            else:
                grade = "F"
            print("Code ID :",codeid,"Score :",score,"Grade :",grade)
        fw.writelines(codeid+str(score)+"\t"+grade+"\n")
        fw.close()
    except Exception as a:
        print(a)

inputscoretest()
gradescore()
