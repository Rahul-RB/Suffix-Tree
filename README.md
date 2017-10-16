# Suffix Tree
This implementation of suffix tree, or more precisely Patricia Trie, has been done in Python.

This is a totally original implementation, I have not taken any code from any existing suffix tree implementations present online.<br>
Please read 'other notes' at end, for extra, off-topic information.

# Index: 
	1. How to run the code? 
	2. File Structure.
	3. Approach taken for questions --> explained in Report.pdf.
	4. Heuristics taken for question 3 --> explained in Report.pdf.
	5. Complexity of algorithm --> explained in Report.pdf.
	6. Test cases and Results --> explained in Report.pdf.

# To run,
```
$python3 Run.py questionNumber
```
where questionNumber can be: q1,q2 or q3 .
Eg: To execute Question1, please do :
```
$python3 Run.py q1
```
The option for custom input strings are done in execution time.

# Tests and Results: <all are average times>
### Creating GST:
 Creating a single GST:5.7536 seconds.<br>
 Creating 'n' trees, one for each document: 2.5846 seconds. 

### Question 1:
 Searching common string ‘one’ on single GST: 0.001463 seconds.<br>
 String “and thus addressed the Crow” on single GST: 0.0001406 seconds.

### Question 2:
Searching ‘charger’: 0.0303 seconds.<br>
Searching ‘it would be as if I should beg every Dog’: 1.2362 seconds.

### Question 3:
Searching default string “it would be as if I should beg every Dog”: 2.12736
seconds.<br>
Searching custom string “charger”: 0.06277 seconds.

# File Structure: 
  - ### SuffixTree.py
  		- The main class, which creates an object of type SuffixTree. 
  		- Constructor takes no argument.
  		- Has attributes: root as its only attribute.
  		- Has methods: 
  			-add() to add a string or word into the tree.
  			-privInsert() private method, which actually inserts into the tree. Helper method of add() method.
  			-getDescendantLeafNodes() method which returns a list of references, each element being of type LeafNode, for an input node. Returns empty list if input is a leaf itself.
  			-findAll() to find all occurences of the query string in a document, used for question 1.
  			-findAll2() to find first occurence of the query string or a substring of the same in all trees.

  - ### TreeNode.py
  		- The class which generates an object of type TreeNode.
  		- Constructor takes one argument: substring, which is the string on edge, which led to the currently creating node.
  			Eg: temp = TreeNode('adf') #We land at temp node via string 'adf' from some node, not mentioned here.
  		- Has attributes: 
			-substring(as defined above)
			-a dictionary 'edges' which stores: Key: substring of children node. Value: object reference to Child Node (can be TreeNode/LeafNode).
  		- Has methods:
  			-getEdge() which takes a character as input and returns the Node corresponding to the character. Returns None is no such node exists.
  				Eg: Say string 'adf' leads to a Node 'temp' from 'root'. So newNode = root.getEdge('a') returns the reference of 'temp' to newNode.
  			-getEdges() returns the dictionary of nodes(children) corresponding to the current node, returns None, if Node has no children.
  			-setEdge() takes a substring(as defined above) and child as input and sets it into the 'edges' dictionary of the current node.

  - ### LeafNode.py
  		- The class which generates a LeafNode type object.
  		- Constructor takes one argument: substring, which is the string on edge, which led to the currently creating node.
  		- Has attributes: 
  			-substring.
  			-documents  a list of object references to Document objects.
  			-suffixNumbers  a list of integers which is the suffix number of the suffix which ended at this node.
  		- Has methods:
  			-addDocument() which takes a Document object and suffixNumber as argument and appends these values to the LeafNode's attributes.
  			-setSuffixNumbers() to insert a suffixNumber into suffixNumbers list.
  			-setDocuments() to insert into a document into documents list.
  			-getDocuments() and getSuffixNumbers() are getter methods of the above setter methods.

  - ### Document.py
  		- A class which creates an object which binds a document (story text) and its corresponding title (story title).
  		- Constructor takes a title and text, as defined above.
  		- Has attributes: 
  			-title title of story, or any other text.
  			-text  text of story, or any other document.
  		- Has methods:
  			-getTitle() and setTitle() getter and setter for title.
  			-getText() and setText() getter and setter for text.

  - ### ParseDocuments.py
  		- A module which contains a function: getDocs()
  		- This getDocs() function parses input file, like AesopTales.txt.
  		- Returns two lists : docsArr and titlesArr which are list of documents and titles respectively.
  		- Brief functioning of getDocs() function: 
  			- Uses readlines() method of Files in Python to divide the files to lines and store to a list.
  			- Replaces all '\n' with leading spaces with '\n' .
  			- Add first line to titles list, then iterate over the list until a set of two '\n' are found. Add the following lines(until another set of two '\n') to documents list.
  			- Replace each '\n' of document with a space, thus making each document or story a single line. 
  
  - ### Run.py
  		- Driver module, which is used to compile.
  		- Takes ONE command line argument, which can be: 'q1', 'q2', 'q3' only.
  		- Does th appropriate functioning for each question as expected.


# Other notes:
This assignment has been even more interesting to do, in comparision to the first assignment. This is the first time I have done object oriented programming in Python. It has helped me develop a good insight into python's implementation of various inbuilt methods and has also helped me . Although it was a risk doing this assignment in a language which I had never used for implementing Data Structures, it has now rewarded me with increased confidence in implementing Data Structures in OO languages in general. <br>
I would like to thank NSK sir for boosting my confidence by showing a clear starting point for the assignment. I would also like to mention a friend of mine: Akhil MD who has helped me extensively in developing this. Ganesh, another friend of mine, has also helped me, for this assignment, in time of need. It would not have been possible for me to implement this DS without the help of any of them. <br>
Thank you.
