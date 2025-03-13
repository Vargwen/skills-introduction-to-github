#!/usr/bin/env python3
L = ("Un deux trois quatre cinq")
L1 = L.split()
print(L1)
M = []
for i in range(len(L1)):
	M += L1[len(L1)-1-i:len(L1)-i]
print(M)
M[1:1]=['truite', 'test', 'test']
print(M)
