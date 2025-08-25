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
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')


# this function load towards the doc
docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

# creates a chain
chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))
