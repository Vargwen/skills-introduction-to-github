def stat(a_liste: list[int]):
	a=max(a_liste)
	b=min(a_liste)
	c=0
	b_liste = []
	for i in range(len(a_liste)):
		c+=a_liste[i]
	b_liste += [a,b,c]
	b_liste=tuple(b_liste)
	print(b_liste)

stat([1,2,3,4,5,6,7])
