from unidecode import unidecode
str = input("Nhập chuỗi cần chuyển đổi:")
str = unidecode(str)
str = str.lower()
str = str.replace(" ","-")
print(str)

