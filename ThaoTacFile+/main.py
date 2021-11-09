class Person:
    def __init__(self,name,phone_number,email_address):
        self.n=name
        self.pn=phone_number
        self.ea=email_address
class Student(Person):
    def __init__(self,name,phone_number,email_address,student_number,average_mark):
        super().__init__(name,phone_number,email_address)
        self.sn=student_number
        self.am=average_mark
class Professsor(Person):
    def __init__(self,name,phone_number,email_address,salary):
        super().__init__(name, phone_number, email_address)
        self.s=salary
def name():
    n=["Bùi Tấn Trường"," Nguyễn Văn Toản","Đặng Văn Lâm","Đỗ Duy Mạnh","Lương Xuân Trường","Nguyễn Tuấn Anh","Nguyễn Công Phượng", "Nguyễn Tiến Linh","Nguyễn Văn Toàn","Hà Đức Chinh" ]
    return n
def phone_number():
    pn=["0765734700","0765734701","07657347027","0765734703","0765734704","0765734705","0765734706","0765734707","0765734708","0765734709","0765734710"]
    return pn
def email_address():
    ea=["a@gmail.com","b@gmail.com","c@gmail.com","d@gmail.com","e@gmail.com","f@gmail.com","g@gmail.com","h@gmail.com","i@gmail.com","j@gmail.com"]
    return ea
def average_mark():
    am=[8.5,8.6,9.5,8.8,8.9,8.6,9.1,8.3,9.3,9.0]
    return am
def student_number():
    sn=["21E1010011","21E1010012","21E1010013","21E1010014","21E1010015","21E1010016","21E1010017","21E1010018","21E1010019","21E1010010"]
    return sn
def salary():
    s=[6000,2000,7000,4000,9000,3000,7000,8000,2000,5000]
    return s
a=Person(name(),phone_number(),email_address())
per=[]
for i in range(10):
    data=[]
    data.append(a.n[i])
    data.append(a.pn[i])
    data.append(a.ea[i])
    per.append(data)
    data=[]
b=Student(name(),phone_number(),email_address(),student_number(),average_mark())
stu=[]
for i in range(10):
    data=[]
    data.append(b.n[i])
    data.append(b.pn[i])
    data.append(b.ea[i])
    data.append(b.sn[i])
    data.append(b.am[i])
    stu.append(data)
    data=[]
c=Professsor(name(),phone_number(),email_address(),salary())
pro=[]
for i in range(10):
    data=[]
    data.append(c.n[i])
    data.append(c.pn[i])
    data.append(c.ea[i])
    data.append(c.s[i])
    pro.append(data)
    data=[]
for i in range(10):
    for j in range(i+1,10):
        if per[i][0]<per[j][0]:
            per[i], per[j] = per[j], per[i]
def SSam(elem):
    return elem[4]
def SSs(elem):
    return elem[3]
stu.sort(key=SSam,reverse=True)
pro.sort(key=SSs)
import pickle
pickle_out1 = open("list1.pickle","wb")
pickle.dump(per, pickle_out1)
pickle_out1.close()
pickle_out2 = open("list2.pickle","wb")
pickle.dump(stu, pickle_out2)
pickle_out2.close()
pickle_out3 = open("list3.pickle","wb")
pickle.dump(pro, pickle_out3)
pickle_out3.close()
