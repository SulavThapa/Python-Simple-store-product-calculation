def reads():
    file=open("record.txt","r")
    line_=file.readlines()
    list_=[]
    for line in line_:
        list_.append(line.replace("\n","").split(","))
    file.close()
    for i in range(len(list_)):
        print("products available:", list_[i][0], "\t price:",list_[i][1], "\t quantity:",list_[i][2])
    return list_
