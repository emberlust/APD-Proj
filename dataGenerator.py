import random

def random_list(size = 0, lower = -100000 + 1 , upper = 100000):
    dimension = 2**size
    random.seed(size)
    dataset = open("datasets/dataset" + str(size) + ".txt","w")
    for i in range(dimension):
        dataset.write(str((random.uniform(lower,upper))) + "\n")
    return list

def main():
    for i in range(26,27):
        random_list(i)

main()