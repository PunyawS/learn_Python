def inputscoretest(): 
    try:    
        fw=open("./text/testassignment.txt","a",encoding="UTF-8")
        while True:
            x=input("Ples input Code Student ID :")
            if x == "exit":
                break
            y=input("Ples input Score Test :")
            if not type(x) is str and not type(y) is str :
                raise Exception
            fw.writelines(x+"\t"+y+"\n")
        fw.close

    except Exception as a:
        print(a)

def gradescore():
    try:
        fr=open("./text/testassignment.txt","r",encoding="UTF-8")
        fw=open("./text/testassignment1.txt","a",encoding="UTF-8")
        s=fr.readlines()
        grade=None
        for i in s:
            codeid=i[:3]
            score=i[-4:].strip()
            score=int(score)
            if score >= 80:
                grade = "A"
            elif score <=80 and score >= 70:
                grade = "B"
            elif score <=70 and score >= 60:
                grade = "C"
            elif score <=60 and score >= 50:
                grade = "D"
            else:
                grade = "F"
            print("Code student ID :",codeid+"\tScore is :",str(score)+"\tGrade :",grade)
            fw.writelines("Code student ID :"+codeid+"\t"+"Score is :"+str(score)+"\t"+"Grade :"+grade+"\n")
        fw.close()
    except Exception as a:
        print(a)

inputscoretest()
gradescore()