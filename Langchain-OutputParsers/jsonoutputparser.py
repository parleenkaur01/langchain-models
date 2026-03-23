#flaw of json output parser is that it doesn't enforce schema

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

 
model = ChatOpenAI()

parser= JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name,age aand city of a fictional person \n{format_instructions}',  
    input_variables = [],
    partial_variables={'format_instructions':parser.get_format_instructions()}  #variables that are pre-filled into the template before runtime not by user
)

# prompt = template.format()
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser
result =chain.invoke({})

print(result)
