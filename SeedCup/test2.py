def clearDirtyData():
    with open("./SeedCup_pre_train.csv","r")as f:
        lines=f.readlines()
        print(lines[1])
    with open("./SeedCup_pre_train.csv","w")as w:
        for i in lines:
            if "1970" not in i:
                w.write(i)

if __name__ == '__main__':
    clearDirtyData()