import os
import re
import numpy as np

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
  return d[t]/sum(d.values())

def idf(t: str, TD: list):
  return len(TD)/(1+count(t, TD))

def tf_idf(t: str, d: dict, TD: list):
  return tf(t, d)*idf(t, TD)

def make_tf_idf_matrix(*f):
    m = []
    for i in f:
        temp = []
        for j in i:
            temp.append(tf_idf(j, i, f))
        m.append(temp)
    return np.array(m)



if __name__ == "__main__":
    # for f in os.listdir("corpus-tf-idf/tieng Anh"):
    #     file_path = f"corpus-tf-idf/tieng Anh/{f}"
    #     fregs0 = read_text_file(file_path)
    fregs1 = read_text_file("corpus-tf-idf/tieng Anh/vb01.txt")
    fregs2 = read_text_file("corpus-tf-idf/tieng Anh/vb02.txt")
    fregs3 = read_text_file("corpus-tf-idf/tieng Anh/vb03.txt")
    fregs4 = read_text_file("corpus-tf-idf/tieng Anh/vb04.txt")
    fregs5 = read_text_file("corpus-tf-idf/tieng Anh/vb05.txt")
    print(make_tf_idf_matrix(fregs1, fregs2, fregs3, fregs4, fregs5))

