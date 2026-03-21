from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI()

#schema

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str,"Return sentiment of the review either negative,positive or neutral"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated.There are too many 
pre-installed apps that I can't remove.Also, the UI looks outdated compared to other 
brans.Hoping for a software update to fix this.""")


print(type(result))
print(result['summary'])