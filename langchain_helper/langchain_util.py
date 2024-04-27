from dotenv import load_dotenv
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain

load_dotenv()


def get_cuisine_for(cuisine_type):

    restaurant_name_prompt = PromptTemplate(
        input_variables=["cuisine_type"],
        template="""Give me a good name for a restaurant which serves {cuisine_type} type cousine. Return only one name without any special characters"""
    )

    restaurant_name_chain = LLMChain(llm=OpenAI(temperature=0.9), prompt=restaurant_name_prompt, output_key="restaurant_name")

    # print(restaurant_name_chain.run(cuisine_type))

    cuisine_prompt = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""Suggest some menu items for {restaurant_name}. Return menu_items with comma separated as show in below example.\n
                1 Margherita Pizza, 2 Spaghetti Carbonara, 3 Chicken Parmigiana, 4 Lasagna Bolognese, 5 Fettuccine Alfredo, 6 Eggplant Parmesan, 7 Shrimp Scampi, 8 Chicken Marsala, 9 Penne Arrabiata, 10 Caprese Salad, 11 Bruschetta, 12 Antipasto Platter, 13 Gnocchi with Pesto Sauce, 14 Ravioli with Marinara Sauce, 15 Meatball Sub, 16 Tiramisu, 17 Cannoli, 18 Gelato, 19 Lemon Sorbet, 20 Espresso\n
                Menue limit should be limit to 20 and "items" and "." should not be part of menu_items"""
    )

    cuisine_chain = LLMChain(llm=OpenAI(temperature=0.3), prompt=cuisine_prompt, output_key= "menu_items")


    chain = SequentialChain(chains=[restaurant_name_chain,cuisine_chain],
                    input_variables=["cuisine_type"],
                    output_variables=["restaurant_name", "menu_items"])
    
    response = chain({"cuisine_type":cuisine_type})

    print(response)

    return response