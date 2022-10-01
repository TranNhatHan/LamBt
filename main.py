import os
import re
import numpy as np

fregs0 = {}

def frequency0(words):
    words = words.lower()
    words = words.replace("-","_")
    words = re.sub('\W+',' ', words)
    words = words.split(" ")
    for word in words:
        fregs0[word] = fregs0.get(word, 0) + 1

def read_text_file0(file_path):
    with open(file_path, 'r') as f:
        return frequency0(f.read())

def frequency(words):
    freqs = {}
    words = words.lower()
    words = words.replace("-","_")
    words = re.sub('\W+',' ', words)
    words = words.split(" ")
    for word in words:
        freqs[word] = freqs.get(word, 0) + 1
    return freqs

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return frequency(f.read())

def count(t: str, TD: list):
  count = 0
  for d in TD:
    if t in d.keys():
      count+=1
  return count

def tf(t: str, d: dict):
    if t in d.keys():
        return d[t]/sum(d.values())
    return 0

def idf(t: str, TD: list):
  return len(TD)/(1+count(t, TD))

def tf_idf(t: str, d: dict, TD: list):
  return tf(t, d)*idf(t, TD)

def make_tf_idf_matrix(f0, *f):
    m = []
    for i in f:
        temp = []
        for j in f0:
            temp.append(tf_idf(j, i, f))
        m.append(temp)
    return np.array(m)



if __name__ == "__main__":
    for f in os.listdir("corpus-tf-idf/tieng Anh"):
        file_path = f"corpus-tf-idf/tieng Anh/{f}"
        read_text_file0(file_path)
    fregs1 = read_text_file("corpus-tf-idf/tieng Anh/vb01.txt")
    fregs2 = read_text_file("corpus-tf-idf/tieng Anh/vb02.txt")
    fregs3 = read_text_file("corpus-tf-idf/tieng Anh/vb03.txt")
    fregs4 = read_text_file("corpus-tf-idf/tieng Anh/vb04.txt")
    fregs5 = read_text_file("corpus-tf-idf/tieng Anh/vb05.txt")
    print(make_tf_idf_matrix(fregs0, fregs1, fregs2, fregs3, fregs4, fregs5))