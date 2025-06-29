from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
#when creating an OPen source model we have to create llm to choose and initiate the model
llm =HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    provider="together"  # specify a provider that actually hosts the model
)

model = ChatHuggingFace(llm=llm)

#we have to creat a chat history so that model could remember our chat 
chat_history = []

while True:
    user_input = input('You:')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    print("AI:",result.content)