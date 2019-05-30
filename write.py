def writing(List, Dictionary):
    list_=List
    dict_=Dictionary
    for key_ in dict_.keys():
        if key_=="PHONE":
            list_[0][2]=str(int(list_[0][2])-dict_["PHONE"])
        elif key_=="LAPTOP":
            list_[1][2]=str(int(list_[1][2])-dict_["LAPTOP"])
        else:
            list_[2][2]=str(int(list_[2][2])-dict_["HDD"])
    print(list_)

    files=open("record.txt","w")
    for every in list_:
        files.write(str(",".join(every)))
        files.write("\n")
    files.close()
    return
