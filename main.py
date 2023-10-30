from langchain.prompts import PromptTemplate
from langchain.chat_models import  ChatOpenAI
from langchain.chains import LLMChain, llm

if __name__ == "__main__":
    print("Hello langchain")

    summary_template = """
         given the information {information} about a person from I want you to create:
         1. a short summary
         2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    lie = ChatOpenAI(temperature=90, model_name="gpt-3.5-turbe")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))





