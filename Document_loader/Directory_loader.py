from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf', # which file format you are trying to load the astreick specify every pdf file in the direcory 
    loader_cls=PyPDFLoader # this is the loader file which we will use
)

docs = loader.load()
# docs = loader.lazy_load()
# Lazy load gives you a generator of documents it load a document once at a time and it get vanish after the usage
# Normal load function does eager loading
print(docs[222].page_content)
# for document in docs:
#     print(document.metadata)