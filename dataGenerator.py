import random

def _random(size = 0, lower = -100000 + 1 , upper = 100000):
    dimension = 2**size
    random.seed(size)
    dataset = open("datasets/dataset" + str(size) + ".txt","w")
    for i in range(dimension):
        dataset.write(str((random.uniform(lower,upper))) + "\n")

def main():
    _random(17)
    _random(18)
    _random(20)
    _random(21)
    _random(22)
    _random(23)
    _random(27)
    _random(28)
    _random(30)

main()