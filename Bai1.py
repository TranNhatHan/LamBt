text = input("Nhap chuoi:")
name = input("Nhap ten file:")
import os
f = open("C:\Thu_muc_moi\Tao_file_bang_python\{}".format(name),"w")
f.write(text)
f.close()
