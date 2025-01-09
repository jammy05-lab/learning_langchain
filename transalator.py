import getpass
import os
# set up key
os.environ["OPENAI_API_KEY"] = "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"
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

LANGCHAIN_TRACING_V2=True
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="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"
LANGCHAIN_PROJECT="pr-bumpy-baseline-56"

model = ChatOpenAI(model = "gpt-4o")

system_template = "Transalate the following from English to {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system" ,system_template),("user", "{text}")]
)

prompt = prompt_template.invoke ({"language": "roman urdu", "text": "my name is ahmad jamshaid"})
# print(prompt)

response = model.invoke(prompt)
print(response.content)

message = [
    SystemMessage ("Pls transalate the following to romanized ."),
    HumanMessage ("How are you!"),
]

result=model.invoke(message)
# print(result)

for token in model.stream(message):
    print(token.content, end="|")