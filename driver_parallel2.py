import threading
from algo import mergeSort
import os
import time


chunks = []
size = 8

result = open("result-p2.txt","a")
for file in os.listdir("in"):
    file = "in\\"+file
    with open(file) as f:
        data = [float(x) for x in f]
    f.close()
    chunks = [[] for _ in range(size)]
    for i, chunk in enumerate(data):
        chunks[i % size].append(chunk)
    data.clear()
    start = time.time()

    workers = []
    for i in range(size):
        var = threading.Thread(target=mergeSort,args=(chunks[i],0,len(chunks[i])-1))
        workers.append(var)

    for i in range(size):
        workers[i].start()

    for i in range(size):
        workers[i].join()
        
    final = []
    for i in range(size):
        final += chunks[i]
        chunks[i].clear()
        mergeSort(final,0,len(final)-1)
        final.clear()
        end = time.time()
        result.write("Elapsed time = " + str(end-start) + " " + file + " " + "\n")