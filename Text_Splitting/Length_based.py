from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=5, #this define the overlap between 2 chunks if suppose you set this to 5 then there will be a overlapped chunk between every two chunks
    separator=''
)

result = splitter.split_documents(docs) #the Splitter function is used to Split the chunk 
print(len(result))

print(result[1].page_content)