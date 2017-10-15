def getDocs():
	fp = open("AesopTales.txt", "r")
	titlesArr = []
	docsArr = []
	indicesArr = []

	lines = fp.readlines()

	for i in range(0,len(lines)):
		if(lines[i] == ' \n'):
			lines[i]='\n'
			
	i=0
	j=0

	titlesArr.append(lines[0])

	for i in range(1,len(lines)):
		if(i < len(lines)-1):
			if(lines[i]=='\n' and lines[i+1]=='\n'):
				titlesArr.append(lines[i+2])
				indicesArr.append(i+1)
				indicesArr.append(i+4)
				docsArr.append(lines[i+4])
	del(indicesArr[0])


	for k in range(0,len(indicesArr),2):
		low = indicesArr[k]
		if(k<len(indicesArr)-1):
			high = indicesArr[k+1]-2
		else:	#done only for the last document manually.
			low = 4392
			high = 4398

		docsArr[j] = ''

		for p in range(low,high+1):
			docsArr[j] = docsArr[j] + lines[p].replace("\n"," ")
		j=j+1

	temp = ''
	for i in range(2,16): #only first document inserted manually
		temp = temp + lines[i].replace("\n"," ")
	docsArr.insert(0,temp)

	return docsArr,titlesArr

if __name__ == '__main__':
	# print(getDocs())
	# print("A")
	docsArr,titlesArr = getDocs()

	# print(docsArr)
	# print(titlesArr)

	for ele in docsArr:
		print(ele)

	# for ele in titlesArr:
	# 	print(ele)