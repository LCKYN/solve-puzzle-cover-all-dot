node = 16
last = 13
ga = {i:list() for i in range(node)}

temp = [[1],
        [2,5],
        [1,3,6],
        [2,7,4],
        [3,8],
        [1,6,9],
        [2,5,7,10],
        [3,6,8,11],
        [4,7,12],
        [5,10,14],
        [6,9,11,15],
        [7,10,12],
        [8,11],
        [14],
        [9,13,15],
        [10,14]]

for i in range(node):
    ga[i] = temp[i]

res = list()

def backtracking(path):
    if(len(path) == node and path[-1] == last):
        res.append(path)
    else:
        for adj in ga[path[-1]]:
            if(not adj in path):
                backtracking(path + [adj])

backtracking([0])

if(res):
    print("Found it {l} solution".format(l = len(res)))
    for i in res:
        print(i)
else:
    print("Have no solution")
