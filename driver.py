from algo import mergeSort
import time
import os

def main():

    result = open("result.txt","a")
    for file in os.listdir("in"):
        file = "in\\"+file
        with open(file) as f:
            data_set = [float(x) for x in f]
        f.close()
        dlen = len(data_set)
        start = time.time()
        mergeSort(data_set,0,dlen - 1)
        end = time.time()
        result.write("Elapsed time = " + str(end-start) + " " + file + " " + "\n")

main()