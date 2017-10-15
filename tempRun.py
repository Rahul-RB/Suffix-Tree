import SuffixTree as st
import parseDocuments as pd
from Document import Document

docsArr,titlesArr = pd.getDocs()

doc1 = Document(titlesArr[0],docsArr[0])
doc2 = Document(titlesArr[5],docsArr[5])

t3 = st.SuffixTree()
t4 = st.SuffixTree()

t3.add(doc1)
t4.add(doc2)
