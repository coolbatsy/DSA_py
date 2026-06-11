def func(i, n):
    if i < 1: # whenever i == 0
        return
    func(i - 1, n)  # go all the way down first
    print(i)        # print on the way back up

func(5, 5)