import sys
import time
import SuffixTree as st
import ParseDocuments as pd
from Document import Document

docsArr,titlesArr = pd.getDocs()
allDocuments = []

try:
	argument = sys.argv[1]
except:
	print("Please note that searches are case sensitive.")
	print("Please enter either of the following options to execute the program:")
	print("1. To execute Question 1. $python3 run.py q1")
	print("2. To execute Question 2. $python3 run.py q2")
	print("3. To execute Question 3. $python3 run.py q3")
	print("Exiting now.")
	exit()

if(argument=='q1'):
	for title,doc in zip(titlesArr,docsArr):
		allDocuments.append(Document(title,doc))
	t3 = st.SuffixTree()

	start = time.time()
	for ele in allDocuments:
		t3.add(ele)
	end = time.time()
	print("Tree Building done,took:",end-start)

	query = input("Enter custom query, enter * to use default query - 'one':")
	
	if(query=='*'):
		query = 'one'
	start = time.time()
	results = t3.findAll(query)
	end = time.time()

	resCount = 0

	for res in results:
		print(res)
		resCount+=1

	print("Number of Results:",resCount)
	print("Results found in:",end-start,"ms")

elif(argument=='q2'):
	treesArray = []
	def getAllSubstrings(query):
		length = len(query)
		return [query[i:j+1] for i in range(length) for j in range(i,length)]

	for title,doc in zip(titlesArr,docsArr):
		allDocuments.append(Document(title,doc))
		treesArray.append(st.SuffixTree())


	start = time.time()

	i=0
	for ele in allDocuments:
		treesArray[i].add(ele)
		i=i+1

	end = time.time()
	print("Tree Building done,took:",end-start)

	query = input("Enter custom query, enter * to use default query - 'charger'")
	
	if(query=='*'):
		query = "charger"

	queryList = getAllSubstrings(query)
	queryList.sort(key=len,reverse=True)

	queryElementArr = []
	resultsArr = []
	start = time.time()
	for tree in treesArray:
		for queryElement in queryList:
			res = tree.findAll2(queryElement)
			if(res!=[]):
				# print("***QUERY:***",queryElement)
				# print(res[0])
				queryElementArr.append(queryElement)
				resultsArr.append(res[0])
				break
	end = time.time()

	for query,result in zip(queryElementArr,resultsArr):
		print("QUERY:",query)
		print(result)
	
	print("Results found in:",end-start,"ms")

elif(argument=='q3'):
	#YET TO IMPLEMENT PEEPS
	rank = 0
	def printRes(results):
		for res in results:
			print(res)
	
	def getAllSubstrings(query):
		length = len(query)
		return [query[i:j+1] for i in range(length) for j in range(i,length)]

	def ranGen():
		global rank
		rank+=1
		yield rank

	def words_in_string(word_list, a_string):
		return set(word_list).intersection(a_string.split())

	treesArray = []
	for title,doc in zip(titlesArr,docsArr):
		allDocuments.append(Document(title,doc))
		treesArray.append(st.SuffixTree())


	start = time.time()
	i=0
	for ele in allDocuments:
		treesArray[i].add(ele)
		i=i+1

	end = time.time()
	print("Tree Building done,took:",end-start)

	query = input("Enter custom query, enter * to use default query - 'it would be as if I should beg every Dog'")
	results = []
	checkIf = 0
	checkElse=0

	if(query=="*"):
		queryMain = " it would be as if I should beg every Dog "
		query = "it would be as if I should beg every Dog"
		listOfWords = query.split(' ')
		checkIf = 1
	else:
		if(query[0]!=' ' and query[1]!=' '):
			queryMain = ' '+query+' '
			listOfWords = query.split(' ')
			checkElse=1
	
	start = time.time()

	for tree in treesArray:
		results+=tree.findAll(queryMain)
	print("\nHighest Rank Results:")
	printRes(results)
	
	results=[]

	if(checkIf):
		for tree in treesArray:
			results+=tree.findAll(query)
		print("\nHigher Rank Results:")
		printRes(results)
	
	
	if(checkElse):
		for tree in treesArray:
			results+=tree.findAll(query)

		print("\nHigher Rank Results:",printRes(results))

	queryList = getAllSubstrings(query)
	queryList.sort(key=len,reverse=True)

	results=[]
	queryLenArr=[]
	for queryElement in queryList:
		for tree in treesArray:
			res = tree.findAll2(queryElement)
			if(res!=[]):
				print("\n***QUERY:***",queryElement)
				print(res[0])
				break
	end = time.time()
	print("Results found in:",end-start,"ms")
	print("Note: This time is INCLUSIVE of time taken to execute all the print statements.")

else:
	print("Please note that searches are case sensitive.")
	print("Please enter either of the following options to execute the program:")
	print("1. To execute Question 1. $python3 run.py q1")
	print("2. To execute Question 2. $python3 run.py q2")
	print("3. To execute Question 3. $python3 run.py q3")
	print("Exiting now.")