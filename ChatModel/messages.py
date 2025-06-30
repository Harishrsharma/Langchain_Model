from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()

#when creating an OPen source model we have to create llm to choose and initiate the model
llm =HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    provider="together"  # specify a provider that actually hosts the model
)

model = ChatHuggingFace(llm=llm)

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
