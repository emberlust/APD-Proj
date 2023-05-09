from mpi4py import MPI
from algo import mergeSort
import os
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

chunks = []

result = open("result-p.txt","a")
for file in os.listdir("in"):
        if rank == 0:
            file = "in\\"+file
            with open(file) as f:
                data = [float(x) for x in f]
            f.close()
            if rank == 0:
                chunks = [[] for _ in range(size)]
                for i, chunk in enumerate(data):
                    chunks[i % size].append(chunk)
                data.clear()
                start = time.time()
            else:
                data = None

        local_data = comm.scatter(chunks, root=0)
        chunks.clear()

        mergeSort(local_data,0,len(local_data)-1)

        sorted_data = comm.gather(local_data, root=0)

        if rank == 0:
            final = []
            for i in range(size):
                final += sorted_data[i]
            sorted_data.clear()
            mergeSort(final,0,len(final)-1)
            final.clear()
            end = time.time()
            result.write("Elapsed time = " + str(end-start) + " " + file + " " + "\n")