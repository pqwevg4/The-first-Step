S1 = set([10,20,30,40,50,60])
S2 = set([40,50,60,70,80,90])
print(S1,S2)
S1.add(55)
S1.add(66)
S1.discard(10)
S1.discard(30)
print(S1)
print(40 in S1)
print(S1.union(S2))
print(S1.intersection(S2))
print(S1.symmetric_difference(S2))