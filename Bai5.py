import random
dem=0
name = input("Nhap ten file:")
a = [random.randint(-1000,1000) for i in range(1000)]
f = open("C:\Thu_muc_moi\Tao_file_bang_python\{}.txt".format(name),"w+")
for i in range(1000):
    f.write(str(a[i]))
    dem+=1
    if dem==10:
        dem=0
        f.write("\n")
    if dem>0:
        f.write(",")
f.close()
f = open("C:\Thu_muc_moi\Tao_file_bang_python\{}.txt".format(name),"r")
lst=f.read().split(",")
for i in range(1000-99):
    print(lst[i],end="  ")
f.close()