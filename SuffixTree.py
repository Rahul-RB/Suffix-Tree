from Document import Document
from LeafNode import LeafNode
from TreeNode import TreeNode

def findMismatch(key,suffix): #takes two strings and finds the number of matched characters, used for insertion.
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

def unpackResults(results): #Result to decorate and display appropriate output, used for question 1.
	resultOfLeavesArr = results[0:]
	finalResult = []
	#the resultOfLeavesArr has a set of leaves, each of which has suffixNumbers in them

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


def unpackResults2(results): ##Result to decorate and display appropriate output, used for question 2.
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
	finalText = resultLeafDocs[0].getText()[lower:(index+16)]		#Getting only first occurence.	
	finalResult.append("\n"+resultLeafDocs[0].getTitle() +"[..."+finalText+"...]")		
	return finalResult

class SuffixTree(object):
	def __init__(self):
		self.root = TreeNode(None)
	def add(self,document):
		newWord = document.getText() + "$"	# '$' is the terminating character.
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

		if(isinstance(child,LeafNode) and (child.substring == suffix)): #If entire substring matches suffix, but we end at Leaf node then just add document and return.
			child.addDocument(document,suffixNumber)
			return
		
		numMatched = findMismatch(child.substring, suffix)

		if(numMatched==len(child.substring) and (child.substring[len(child.substring)-1]!='$')): #If entire susbtring is matched, but it's a internal node, then insert rest of unmatched query ('$')
			self.privInsert(child,suffix[numMatched:],suffixNumber,document)
			return
		
		elif(len(child.substring) < len(suffix)): #If only a part of query matched substring, then we'll have to check further:
			if(isinstance(child,LeafNode)!=True):	

				newChildString = child.substring[:numMatched] #is xba is suff and xa is child, then newChildString is x and restChildString is a .

				if(child.substring != newChildString):
					node.edges[newChildString] = node.edges[child.substring] #creating a new key in dictinary and assigning it value of existing key and deleting existing key.
					del node.edges[child.substring]

				# for cases where: substring is 'xa' from root, lands on internal node, which protudes to twp leaf nodes with edges 'bxa$' and '$'
				# we're trying to insert 'xba$', so this will have to create a new inernal node between 'xa'
				# then copy all children of old 'xa' to newly created 'a'
				# then insert into the new internal node (between x and a) then unmatched part of query (i.e. 'xba$' in out case) 
				if(len(child.substring)>1 and len(child.substring)!=numMatched): 
					restChildString = child.substring[numMatched:]

					newInternalNode = TreeNode(restChildString)

					for childString,childNode in child.edges.items():
						newInternalNode.setEdge(childString,childNode) #copying edges
					child.edges.clear()	#deleting all edges of old internal node
					child.setEdge(restChildString,newInternalNode) #setting internal node to newly created internal node.

				child.substring = newChildString
				self.privInsert(child,suffix[numMatched :],suffixNumber,document)	#recursilvely calling function to insert unmatched part of query.
				return
	
		
		newInternalNode = TreeNode(suffix[:numMatched])
		del node.edges[child.substring]	#deleting the old edge pointing to internal node.
		newChildNode = LeafNode(suffix[numMatched:])
		newChildNode.addDocument(document,suffixNumber)
		child.substring = child.substring[numMatched:]

		newInternalNode.setEdge(suffix[numMatched:],newChildNode)
		newInternalNode.setEdge(child.substring,child)


		node.setEdge(suffix[:numMatched],newInternalNode) #adding new edge pointing to newly created internal node.
		return

	def getDescendantLeafNodes(self,node):
		descedants = []
		if(isinstance(node,LeafNode)): #if node is of type LeafNode, then return empty array or results respectively.
			descedants.append(node)
			return descedants

		if(node.edges=={}):		#if node has no children, empty list
			return descedants


		nodeKeys = list(node.edges.keys())
		nodeKeys = sorted(nodeKeys)

		for key in nodeKeys:	#go to every edge from lowest to highest in alpabetical order and recursively call function.
			childDescedants = self.getDescendantLeafNodes(node.edges[key])
			descedants+=childDescedants

		return descedants

	def findAll(self,query): #used for question one.
		results = []
		child = self.root.getEdge(query[0])
		i,j = 0,0
		queryLen = len(query)
		if(child!=None):
			childSubstringLen = len(child.substring) #just checking if we end at a node with no children.
		else:
			return results

		while(child!=None): 	#for every child
			text = child.substring
			textLen = len(text)
			i = 0
			while((i<textLen) and (j<queryLen)): #check the point till where query and substring of child match, see which exhausts first.
				if(text[i]!=query[j]):
					results = unpackResults(results)
					return results
				i=i+1
				j=j+1

			if((i>=textLen) and (j<queryLen)): #if substring exhausted first, it means that we'll have to search in children of the child node itself.
				child = child.getEdge(query[j]) #so find that new child, of the old child whose first character matches the first character of unmatched query.

			elif((i<=textLen) and (j>=queryLen)): #if query exhausted first, it means we'll just have to find all leaves of current node, unpack results and display them.
				descedants = self.getDescendantLeafNodes(child)

				for desc in descedants:
					results.append(desc)

				results = unpackResults(results)
				return results

		results = unpackResults(results)
		return results

	def findAll2(self,query): #FOR QUESTION 2, same logic as before, expect uses unpackResults2 to display first result only.
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


