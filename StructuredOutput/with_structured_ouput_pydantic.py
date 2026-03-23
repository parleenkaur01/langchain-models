from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional,Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

#schema
class Review(BaseModel):
    key_themes:list[str] = Field(description="Write down all te key themes discussed in the review")
    summary:str = Field(description="A brief summary of the review")
    sentiment:Literal["pos","neg"] =Field(description="Return sentiment of the review either negative,positive or neutral")

    pros:Optional[list[str]]= Field(default=None,description="Write down all the pros inside a list")

    cons:Optional[list[str]]= Field(default=None,description="Write down all the cons inside a list")

    name:Optional[str]= Field(default=None,description="Write the name of the reviewer")


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated.There are too many 
pre-installed apps that I can't remove.Also, the UI looks outdated compared to other 
brans.Hoping for a software update to fix this 
                                 
Review By Adarsh.""")



print(result.name)