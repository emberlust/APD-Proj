import random

def _random(size = 0, lower = -100000 + 1 , upper = 100000):
    dimension = 2**size
    random.seed(size)
    dataset = open("datasets/dataset" + str(size) + ".txt","w")
    for i in range(dimension):
        dataset.write(str((random.uniform(lower,upper))) + "\n")

def main():
    for i in range(1,28):
        _random(i)

main()