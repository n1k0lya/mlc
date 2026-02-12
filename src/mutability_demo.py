import copy

a = [1, 2]
b = a
b.append(3)
c = a.copy()
c.append(52)
print(a, b, c)

joker = [[1, 2]]
newlist = copy.deepcopy(joker)
newlist[0].append(52)
print(joker, newlist)