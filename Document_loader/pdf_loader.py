from langchain_community.document_loaders import PyPDFLoader

from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os



from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

load_dotenv()
#when creating an OPen source model we have to create llm to choose and initiate the model
llm =HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    provider="together"  # specify a provider tha t actually hosts the model
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Write a summary of this pdf - \n {docs}',
    input_variables=['docs']
)

parser = StrOutputParser()

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)

# creates a chain
chain = prompt | model | parser

print(chain.invoke({'docs':docs}))
