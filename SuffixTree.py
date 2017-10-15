from Document import Document
from LeafNode import LeafNode
from TreeNode import TreeNode

def findMismatch(key,suffix):
	keyLen = len(key)
	suffixLen = len(suffix)
	count = 0
	if(keyLen >= suffixLen):
		if(key[0]==suffix[0]):
			for i in range(0,suffixLen):
				if(key[i] == suffix[i]):
					count +=1
				else:
					break
	else:
		if(key[0]==suffix[0]):
			for i in range(0,keyLen):
				if(key[i] == suffix[i]):
					count +=1
				else:
					break
	return count

def unpackResults(results):
	resultOfLeavesArr = results[0:]
	finalResult = []
	#the resultOfLeavesArr has a set of leaves, each of which has suffixNumbers in them
	#sort the leaves according to suffixNumbers to get first occurence. -- not sure

	for leaf in resultOfLeavesArr:
		leafSuffixNumbers = leaf.suffixNumbers[0:]
		leafDocuments = leaf.documents[0:]
		i=0
		for leafDoc in leafDocuments:
			index = leafSuffixNumbers[i]-1
			leafDocTextPoint = leafDoc.getText()[index]
			if(index-15 < 0):
				lower = 0
			else:
				lower = index-15
			finalText = leafDoc.getText()[lower:(index+16)]
			finalResult.append("\n"+leafDoc.getTitle() +"[..."+finalText+"...]")
			i+=1

	return finalResult


def unpackResults2(results): #FOR QUESTION 2
	resultOfLeavesArr = results[0:]
	finalResult = []
	
	originalSuffixNumbers = [ele.suffixNumbers[0] for ele in resultOfLeavesArr]
	resultLeaf = resultOfLeavesArr[originalSuffixNumbers.index(min(originalSuffixNumbers))]
	resultLeafDocs = resultLeaf.documents[0:]
	index = resultLeaf.suffixNumbers[0]
	if(index-15 < 0):
		lower=0
	else:
		lower = index-15
	finalText = resultLeafDocs[0].getText()[lower:(index+16)]			
	finalResult.append("\n"+resultLeafDocs[0].getTitle() +"[..."+finalText+"...]")		
	return finalResult

class SuffixTree(object):
	"""docstring for SuffixTree"""
	def __init__(self):
		self.root = TreeNode(None)
	
	def add(self,document):
		newWord = document.getText() + "$"
		suffixes = [newWord[i:] for i in range(0,len(newWord))]
		
		for i in range(0,len(suffixes)):
			self.privInsert(self.root,suffixes[i],i,document)

	def privInsert(self,node,suffix,suffixNumber,document):
		child = node.getEdge(suffix[0])
		
		if(child == None): # for first insertion, it'll be None, pointing to no children, as it has none.
			newChild = LeafNode(suffix)
			newChild.addDocument(document,suffixNumber)
			node.setEdge(suffix,newChild)
			return

		if(isinstance(child,LeafNode) and (child.substring == suffix)):
			child.addDocument(document,suffixNumber)
			return
		
		numMatched = findMismatch(child.substring, suffix)

		if(numMatched==len(child.substring) and (child.substring[len(child.substring)-1]!='$')):
			self.privInsert(child,suffix[numMatched:],suffixNumber,document)
			return
		
		elif(len(child.substring) < len(suffix)):
			if(isinstance(child,LeafNode)!=True):

				newChildString = child.substring[:numMatched] #is xba is suff and xa is child, then newChildString is x and restChildString is a .

				if(child.substring != newChildString):
					node.edges[newChildString] = node.edges[child.substring]
					del node.edges[child.substring]

				if(len(child.substring)>1 and len(child.substring)!=numMatched):
					restChildString = child.substring[numMatched:]

					newInternalNode = TreeNode(restChildString)

					for childString,childNode in child.edges.items():
						newInternalNode.setEdge(childString,childNode)
					child.edges.clear()
					child.setEdge(restChildString,newInternalNode)

				child.substring = newChildString
				self.privInsert(child,suffix[numMatched :],suffixNumber,document)	
				return
	
		
		newInternalNode = TreeNode(suffix[:numMatched])
		del node.edges[child.substring]
		newChildNode = LeafNode(suffix[numMatched:])
		newChildNode.addDocument(document,suffixNumber)
		child.substring = child.substring[numMatched:]

		newInternalNode.setEdge(suffix[numMatched:],newChildNode)
		newInternalNode.setEdge(child.substring,child)


		node.setEdge(suffix[:numMatched],newInternalNode)
		return


	def getDescendantLeafNodes(self,node):
		descedants = []
		if(isinstance(node,LeafNode)):
			descedants.append(node)
			return descedants

		if(node.edges=={}):
			return descedants


		nodeKeys = list(node.edges.keys())
		nodeKeys = sorted(nodeKeys)

		for key in nodeKeys:
			childDescedants = self.getDescendantLeafNodes(node.edges[key])
			descedants+=childDescedants

		return descedants


	def findAll(self,query):
		results = []
		child = self.root.getEdge(query[0])
		i,j = 0,0
		queryLen = len(query)
		if(child!=None):
			childSubstringLen = len(child.substring)
		else:
			return results
		while(child!=None):
			text = child.substring
			textLen = len(text)
			i = 0
			while((i<textLen) and (j<queryLen)):
				if(text[i]!=query[j]):
					results = unpackResults(results)
					return results
				i=i+1
				j=j+1

			if((i>=textLen) and (j<queryLen)):
				child = child.getEdge(query[j])

			elif((i<=textLen) and (j>=queryLen)):
				descedants = self.getDescendantLeafNodes(child)

				for desc in descedants:
					results.append(desc)

				results = unpackResults(results)
				return results

		results = unpackResults(results)
		return results

	def findAll2(self,query): #FOR QUESTION 2
		results = []
		child = self.root.getEdge(query[0])
		i,j = 0,0
		queryLen = len(query)
		if(child!=None):
			childSubstringLen = len(child.substring)
		else:
			return results
		while(child!=None):
			text = child.substring
			textLen = len(text)
			i = 0
			while((i<textLen) and (j<queryLen)):
				if(text[i]!=query[j]):
					if(results!=[]):
						results = unpackResults2(results)
					return results
				i=i+1
				j=j+1

			if((i>=textLen) and (j<queryLen)):
				child = child.getEdge(query[j])

			elif((i<=textLen) and (j>=queryLen)):
				descedants = self.getDescendantLeafNodes(child)

				for desc in descedants:
					results.append(desc)

				if(results!=[]):
					results = unpackResults2(results)
				return results

		if(results!=[]):
			results = unpackResults2(results)
		return results