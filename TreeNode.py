class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self,substring):
		self.edges = {}
		self.substring = substring #the one which led to this node

	def getEdges(self):
		if(self.edges == {}):
			return None
		return self.edges
	
	def getEdge(self,firstChar):
		child = firstChar
		keys = list(self.edges.keys())
		if(keys != []):
			for key in keys:
				if(key.startswith(child)):
					# return key.find(ele)
					return self.edges[key]
		else:
			return None
		return None

	def setEdge(self,substring,child):
		self.edges[substring] = child
