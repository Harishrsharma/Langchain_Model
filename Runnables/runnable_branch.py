from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda


from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

load_dotenv()
#when creating an OPen source model we have to create llm to choose and initiate the model
llm =HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    provider="together"  # specify a provider tha t actually hosts the model
)

model = ChatHuggingFace(llm=llm)


prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))
