import random
import os
import math
from typing import ValuesView


def FilesCreation():
    path = r"D:\pycharm\kimoir\test"
    array_char = ['A', 'B', 'C', 'D', 'E', 'F']
    name = "sample"
    m = 1
    char_no = 20
    while m <= 10:
        FileName = os.path.join(path, name + str(m) + ".txt")
        testfile = open(FileName, "w")
        m += 1
        i = 1
        r = " "
        while (i <= char_no):
            r += random.choice(array_char)
            r += " "
            i += 1
        testfile.write(r)


def filescontent():
    filescontent = []
    directory = r'D:\pycharm\kimoir\folder'
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            f = open(os.path.join(directory, filename), "r")
            filescontent.append((f.read()).strip().upper())
    return filescontent


def statisticstermfreq(filescontent):
    prob = []
    for file in filescontent:
        filelength = (len(file) + 1) / 2
        dictionary = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
        for char in file:
            if char == " ":
                continue
            dictionary[char] += 1
        for char in dictionary:
            dictionary[char] /= filelength
        prob.append(dictionary)
    return prob


def score(prob, query):
    scores = []
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for file in prob:
        tscore = 0
        for term in file:
            tscore += file[term] * query[term]
        scores.append(tscore)
    lst_tuple = list(zip(scores, arr))
    lst_tuple.sort(key=lambda x: x[0], reverse=True)
    scores.sort(reverse=True)
    return lst_tuple

"""-----------------------------------------------------vector spcae---------------------------------------------------------------------------------------"""


def vectortermfreq(filescontent):
    prob = []
    for file in filescontent:
        dictionary = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
        for char in file:
            if char == " ":
                continue
            dictionary[char] += 1
        mix = max(dictionary.values())
        for char in dictionary:
            dictionary[char] /= mix
        prob.append(dictionary)

    return prob


def idf(termfreq):
    dictionary = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    for f in termfreq:
        for char in f:
            if f[char] > 0:
                dictionary[char] += 1
    for i in dictionary:
        dictionary[i] = math.log2(10 / dictionary[i])
    return dictionary


def weight(tf, idf):
    tfidf = []
    for file in tf:
        dictionary = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
        for term in file:
            dictionary[term] = file[term] * idf[term]
        tfidf.append(dictionary)

    return tfidf


def similarity(query, tfidf):
    scores = []
    arr= [0,1,2,3,4,5,6,7,8,9]
    for file in tfidf:
        tscore = 0
        for term in file:
            tscore += file[term] * query[term]
        deno = (cosine(list(file.values())) * cosine(list(query.values())))
        if deno > 0:
            tscore = tscore / deno
        else:
           tscore = 0
        scores.append(tscore)
    lst_tuple =list(zip(scores,arr))
    lst_tuple.sort(key=lambda x:x[0],reverse=True)
    scores.sort(reverse=True)
    return lst_tuple


def writenumber(query):
    query = query.strip()
    query = query[1:-1]
    query = query.split(";")
    query = {p.split(":")[0]: p.split(":")[1] for p in query}
    dictionary = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    flag = False
    for i in query:
        dictionary[i] = float(query[i])
        if (dictionary[i] > 1 or dictionary[i] < 0):
            flag = True
    if (flag): return False
    return (dictionary)


def printdic(dic):
    for i in dic:
        print(i)


def cosine(array):
    sum = 0
    for i in array:
        sum += i ** 2
    return math.sqrt(sum)


def statisticalmodel(query):
    fsc = filescontent()
    stf = statisticstermfreq(fsc)
    sscore = score(stf, query)
    return sscore


def vectorspace(query):
    fsc = filescontent()
    k = vectortermfreq(fsc)
    tfidf = weight(k, idf(k))
    return (similarity(query, tfidf))


def conversion(R):
    result = ""
    for i in R:
        result += (str(i)) + "<br>"
    return result

def conversiontuple(R):
    result1= " "
    for i in R:
        result1+= "document       "+str(i[1])+"        value     "+str(i[0])+ "<br>"
    return result1
if __name__ == "__main__":
    # Create()
    query = writenumber("<A:0.3;B:0.6;C:0.8;F:0.1>")
    # statisticalmodel(query)
    # vectorspace(query)
