from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional,Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

#schema
{
    "title":"Review",
    "type":"object",

}


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated.There are too many 
pre-installed apps that I can't remove.Also, the UI looks outdated compared to other 
brans.Hoping for a software update to fix this 
                                 
Review By Adarsh.""")



print(result.name)