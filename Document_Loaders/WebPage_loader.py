from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()


prompt = PromptTemplate(
    template ='Answer the following question \n{question} from the following text \n{text}',
    input_variables=['text','question']
)

parser= StrOutputParser()
url ='https://www.amazon.com/4pcs-DWTS-Drinking-glasses-Cleaning-Brushes/dp/B0B7WL9375/ref=sr_1_10?crid=EK6CRXQACXI5&dib=eyJ2IjoiMSJ9.QfvbSVU2T6unPzLpVP76tlnY3CA5SIS2GhhaAS8XyDIpUfngRzuznPGWmAnOHONTCAmhezepoZhQYyK0Vr35_TcEA8LbVE6AlV4zgk5xmyBEZjYiZ5I_ySO1QNvdonyKLlJiLmQadJO4yJcS9Rmhup-x6ScWl5We9LmBnsvZIsSvlBOe2D6TzgKOcF0vcrPphgNoCd2T5JZnzPAJCWDAAQc-5TChGp-f24IjzL5PAJotZxjF5ym4camm9BCOwIzq6pOo1r4FNDJcf2S63pcMFjoK4jrUhtEI8FKEQQRPjEE.V7NioAjy4kyycvVwdE24W2w6HNG5FiyI_weBxbFj0_M&dib_tag=se&keywords=coffee%2Bdrinking%2Bcups&qid=1774389800&sprefix=%2Caps%2C132&sr=8-10&th=1'
loader= WebBaseLoader(url)

docs= loader.load()

chain = prompt | model | parser
print(chain.invoke({'question':'What is the product about?','text':docs[0].page_content}))