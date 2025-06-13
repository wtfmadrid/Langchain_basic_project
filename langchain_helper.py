from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os

os.environ['OPENAI_API_KEY'] = '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'

llm = OpenAI(temperature=0.7)



def generate_restaurant_name_and_items(cuisine):
    
    prompt_temp = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for it"
)
    chain = LLMChain(llm=llm, prompt = prompt_temp, output_key = "restaurant_name")

    
    prompt_temp_items = PromptTemplate(
    input_variables= ['restaurant_name'],
    template = "Suggest some menu items for {restaurant_name}. Return it as a comma separated."
)
    chain1 = LLMChain(llm=llm, prompt = prompt_temp_items, output_key = "menu_items")

    chain3 = SequentialChain(
    chains = [chain, chain1],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', 'menu_items']
)
    response = chain3({'cuisine':cuisine })
    
    return response

