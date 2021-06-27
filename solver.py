node = 6
ga = {i:set() for i in range(6)}

ga[0] = {1}
ga[1] = {0,4,2}
ga[2] = {1,3}
ga[3] = {2,4}
ga[4] = {1,3,5}
ga[5] = {}

res = list()

def backtracking(path):
    if(len(path) == node):
        res.append(path)
    else:
        for adj in ga[path[-1]]:
            if(not adj in path):
                backtracking(path + [adj])
            # else:
            #     print(f"reject : next {adj} from {path}")

backtracking([0])

if(res):
    print("Found it {l} solution".format(l = len(res)))
    for i in res:
        print(i)
else:
    print("Have no solution")
