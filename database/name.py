import csv
import random

CSV1 = "nat2021.csv"
CSV2 = "test.csv"
CSV3 = "patronymes.csv"


def double(file,file2):

    with open(file,'r',encoding="UTF-8") as in_file, open(file2,'w',encoding="UTF_-8") as out_file:
        seen = []
        writer = csv.writer(out_file, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for line in in_file:
            temp:list = line.split(";")
            tempstr:str = temp[1]
            if tempstr in seen: continue
            
            seen.append(tempstr)
            phrase:str = f"{tempstr};"

            writer.writerow(phrase)


def read(file, file2,out)->None:

    with open(file, 'r', encoding='UTF-8') as in_file1, open(file2, 'r', encoding='UTF-8') as in_file2, open(out, 'a' ,encoding='UTF-8') as out:


        x = random.randint(1,36100)
        y = random.randint(1,879419)

        read_name = csv.reader(in_file1)
        read_surname = csv.reader(in_file2)

        rows_name = list(read_name)

        name = str(rows_name[x])
        name_l = len(name)
        name_f = name[2:(name_l-3)]
            


        rows_surname = list(read_surname)
        surname = str(rows_surname[y])
        surname_l = len(surname)
        surname_f = surname[2:(surname_l-3)]
            


        rand = random.randint(1,999)
        if rand < 100 :
            frand = f"0{str(rand)}"
        else :
            frand = str(rand)
        no_uti = f"22 100 {frand}"

        year = random.randint(1950,2004)
        month = random.randint(1,12)
        day = random.randint(1,28)
        if month < 10 :
            m = f"0{str(month)}"
        else :
            m = str(month)
        if day < 10 :
            d = f"0{str(day)}"
        else :
            d= str(day)
        birthday = f"{year}-{m}-{d}"

        mail:str = f"{name_f}.{surname_f}@cyu.fr" 
            
        phone = []
        phone.append("06")
        for i in range(8):
            phone.append(random.randint(0,9))
        ph_number = f"{phone[0]}{phone[1]}{phone[2]}{phone[3]}{phone[4]}{phone[5]}{phone[6]}{phone[7]}{phone[8]}" 
            
        dep = random.randint(1,4)

        awnser:str = f"INSERT INTO utilisateur (\"{no_uti}\";\"{surname_f}\";\"{name_f}\";\"{birthday}\";\"{mail}\";\"{ph_number}\";\"000{dep}\";0;false;NULL;false);"


        out.write(awnser)
        out.write('\n')



#### MAIN ####

#result:list = []

#result = double(CSV1,CSV2)

i:int = 0
for i in range(50):
    read(CSV2,CSV3,"data.sql")
