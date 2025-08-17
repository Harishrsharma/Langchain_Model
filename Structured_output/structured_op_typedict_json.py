import json
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    provider="together"
)

model = ChatHuggingFace(llm=llm)

prompt = """
Please analyze the following review and output only a JSON object with these fields:
- key_themes: list of key themes
- summary: short summary
- sentiment: "pos" or "neg"
- pros: list of pros
- cons: list of cons
- name: reviewer's name

Review:
"I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Review by Nitish Singh
"
"""

result = model.invoke(prompt)

# Extract content
raw_content = result.content

# Find JSON block
start = raw_content.find('{')
end = raw_content.rfind('}') + 1
json_str = raw_content[start:end]

# Parse
parsed = json.loads(json_str)

# Print any field
print(parsed)
