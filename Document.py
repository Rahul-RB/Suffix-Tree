class Document(object):

	def __init__(self,title,text):
		self.title = title
		self.text = text

	def getTitle(self):
		return self.title


	def getText(self):
		return self.text

	def setTitle(self,title):
		self.title = title

	def setText(self,text):
		self.text = text