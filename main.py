
from langchain.google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser  
from dotenv import load_dotenv 
load_dotenv() 


chat_template = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an expert game development code assistant. You take user code and improve it based on requests.\n"
     "Respond with three clearly labeled sections: \n"
     "1. [Improved Code] - return only the updated code\n"
     "2. [Explanation] - explain what you changed and why\n"
     "3. [Suggestions] - list any additional improvements or refactor ideas"),
     
    ("human", 
     "Here is the code:\n```python\n{code}\n```\n\n"
     "User request: {request}\n\n"
     "Please return improved code and explain what was changed. Also add any smart suggestions if possible.")
])


try:
    Model=ChatGoogleGenerativeAI(model='gemini-1.5-flash',temperature=0.5) 
except Exception as e:
    print(f"Error initializing model: {e}. Please check your KEY or model availability.")
    exit(1) 

parser=StrOutputParser()


def generate_improved_code(code,request): 
    prompt=chat_template.format_messages(code=code,request=request) 
    chain=Model|parser 
    response=chain.invoke(prompt)
    # return response.content 

    sections={
        "improved_code":"",
        "explanation":"",
        "suggestions":""
    } 
    for section in ["Improved Code","Explanation","Suggestions"]: 
        if f"[{section}]" in response: 
            content=response.split(f"[{section}]")[1] 
            content=content.split("\n[")[0].strip() 
            sections[section.lower().replace(" ","_")]=content
    return sections 


