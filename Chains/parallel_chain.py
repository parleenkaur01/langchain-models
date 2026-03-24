from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()

model1=ChatOpenAI()

model2 =ChatOpenAI()

prompt1=PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2=PromptTemplate( 
    template='Generate 5 short question-answer pairs from the following text\n{text}',
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template ='Merge the provided notes and quiz into the single document \n notes->{notes} and quiz->{quiz}',
    input_variables=['notes','quiz']

)
parser=StrOutputParser()


parallel_chain=RunnableParallel(
    {
        'notes':prompt1 | model1 | parser,
        'quiz':prompt2 | model2 | parser
    }
)

merge_chain =prompt3 | model1 | parser

chain= parallel_chain | merge_chain
text ="""
Modern technology has transformed the way people live, work, and communicate. Over the past few decades, advancements in computers, smartphones, and the internet have made information more accessible than ever before. People can now connect with others across the world instantly, share ideas, and collaborate on projects without being in the same location. This has greatly improved productivity and opened up new opportunities in education and business.

One of the most significant impacts of technology is in the field of education. Online learning platforms allow students to access courses from top universities, learn at their own pace, and explore subjects beyond traditional classrooms. Digital tools such as videos, simulations, and interactive quizzes make learning more engaging and effective. However, it also requires discipline and time management skills from learners.

Technology has also changed the workplace. Remote work has become more common, allowing employees to work from home or anywhere with an internet connection. This flexibility can improve work-life balance and reduce commuting time. At the same time, it has created new challenges, such as maintaining communication, staying motivated, and managing distractions.

Despite its many benefits, technology also has drawbacks. Excessive use of digital devices can lead to reduced physical activity, eye strain, and sleep problems. Social media, while useful for staying connected, can sometimes cause stress, comparison, and reduced real-life interaction. It is important for individuals to use technology mindfully and maintain a healthy balance between online and offline activities.

In conclusion, technology plays a crucial role in modern society by improving communication, education, and work environments. While it offers many advantages, it is important to use it responsibly to avoid its negative effects. By finding the right balance, people can enjoy the benefits of technology while maintaining their well-being.

"""

result =chain.invoke({'text':text})
print(result)

                   
chain.get_graph().print_ascii()