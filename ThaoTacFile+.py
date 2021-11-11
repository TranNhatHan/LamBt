class Person:
    def __init__(self,name,phone_number,email_address):
        self.n=name
        self.pn=phone_number
        self.ea=email_address

    def outputInfo(self):
        return f"Tên: {self.n}, SĐT: {self.pn}, Email: {self.ea}"
class Student(Person):
    def __init__(self,name,phone_number,email_address,student_number,average_mark):
        super().__init__(name,phone_number,email_address)
        self.sn=student_number
        self.am=average_mark

    def outputInfo(self):
        return f"Tên: {self.n}, SĐT: {self.pn}, Email: {self.ea}, Mã sinh viên: {self.sn}, Điểm trung bình: {self.am}"

class Professor(Person):
    def __init__(self,name,phone_number,email_address,salary):
        super().__init__(name, phone_number, email_address)
        self.s=salary

    def outputInfo(self):
        return f"Tên: {self.n}, SĐT: {self.pn}, Email: {self.ea}, Lương: {self.s}"

def name():
    n=["Bùi Tấn Trường","Nguyễn Văn Toản","Đặng Văn Lâm","Đỗ Duy Mạnh","Lương Xuân Trường","Nguyễn Tuấn Anh","Nguyễn Công Phượng", "Nguyễn Tiến Linh","Nguyễn Văn Toàn","Hà Đức Chinh" ]
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

per = []
n = name()
pn = phone_number()
ea = email_address()
for i in range(10):
    tam=Person(n[i],pn[i],ea[i])
    per.append(tam)

stu = []
n = name()
pn = phone_number()
ea = email_address()
sn = student_number()
am = average_mark()
for i in range(10):
    stu.append(Student(n[i], pn[i], ea[i], sn[i], am[i]))

pro=[]
n = name()
pn = phone_number()
ea = email_address()
s = salary()
for i in range(10):
    pro.append(Professor(n[i], pn[i], ea[i], s[i]))

for i in range(10):
    for j in range(i,10):
        if per[i].n < per[j].n:
            per[i],per[j]=per[j],per[i]

for i in range(10):
    for j in range(i,10):
        if stu[i].am < stu[j].am:
            stu[i],stu[j]=stu[j],stu[i]

for i in range(10):
    for j in range(i,10):
        if pro[i].s > pro[j].s:
            pro[i],pro[j]=pro[j],pro[i]



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

pickle_in1 = open("list1.pickle","rb")
per = pickle.load(pickle_in1)
for i in range(len(per)):
    print(per[i].outputInfo())
pickle_out1.close()

pickle_in2 = open("list2.pickle","rb")
per = pickle.load(pickle_in2)
for i in range(len(stu)):
    print(stu[i].outputInfo())
pickle_out2.close()

pickle_in3 = open("list3.pickle","rb")
per = pickle.load(pickle_in3)
for i in range(len(pro)):
    print(pro[i].outputInfo())
pickle_out3.close()









