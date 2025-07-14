from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") 

# Define your LLM (make sure you have set OPENAI_API_KEY in your .env file)
llm = ChatOpenAI()

hiring_prompt = "We need to hire a Software Engineer for our backend team."
# Define the prompt
jd_prompt = ChatPromptTemplate.from_template(
    "Create a job description based on the following hiring request:\n\n{request}"
)

parser=StrOutputParser()
jd_chain=jd_prompt | llm | parser

#Step3 
def approve_jd (jd:str)-> bool :
    return "Approved"
#Step4

def post_jd(jd:str):
    print("JD approved and posted :\n")


#step5 - Loop until JD is approved (Glue code)
approved = False
jd_output = None

while not approved :
    jd_output = jd_chain.invoke({"request" :hiring_prompt})
    print(jd_output)
    
    approved = approve_jd(jd_output)
    
    if not approved:
        print("JD not approved, please revise...\n")
        
#Final step 
if approved :
    post_jd(jd_output)
    print("Job Description posted successfully!")



# # Run the chain
# result = jd_chain.invoke({"request": hiring_prompt})
# print(result)