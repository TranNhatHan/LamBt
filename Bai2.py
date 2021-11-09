name = input("Nhap ten file muon doc:")
f = open("C:\Thu_muc_moi\Tao_file_bang_python\{}".format(name),"r")
print(f.read())
f.close()