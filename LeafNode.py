from TreeNode import TreeNode

class LeafNode(TreeNode):
	"""docstring for LeafNode"""
	def __init__(self,substring):
		self.substring = substring #the one which led to this node
		self.documents = []
		self.suffixNumbers = []

	def addDocument(self,document,suffixNumber):
		self.documents.append(document)
		self.suffixNumbers.append(suffixNumber)

	def setSuffixNumbers(self,suffixNumbers):
		if(isinstance(suffixNumbers,list)):
			self.suffixNumbers = suffixNumbers
		else:
			print("List expected")

	def setDocuments(self,documents):
		if(isinstance(documents,list)):
			self.documents = documents
		else:
			print("List expected")
	
	def getDocuments(self):
		return self.documents

	def getSuffixNumbers(self):
		return self.suffixNumbers
	# def __str__(self):
	# 	return "leaf node: "+self.substring
