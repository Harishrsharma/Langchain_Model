from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

load_dotenv()
#when creating an OPen source model we have to create llm to choose and initiate the model
llm =HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    provider="together"  # specify a provider tha t actually hosts the model
)

model = ChatHuggingFace(llm=llm)


def word_count(text):
    return len(text.split())


prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)