#Assignment โปรแกรมใส่เกรดนักเรียน

try:
    fw=open("./Text/Assignment.txt","a",encoding="UTF-8")
    while True:
        codeid=input("Ples input Code ID :")
        if codeid == "exit":
            break
        score=input("Ples input score test :")
        if not type(score) is str:
            raise Exception
        fw.writelines(codeid+"\t"+score+"\n")
    fw.close()

except Exception as a:
    print(a)