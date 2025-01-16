from crewai import Agent
from dotenv import load_dotenv
import os
load_dotenv()
from tools import tool
from crewai import LLM

llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GEMINI_KEY")
)

novo_pesquisador=Agent(
    role="Pesquisador Senior",
    goal="Procurar os pontos principais para enteder webscraping e como pode se aliar junto com AI",
    verbose=True,
    memory=True,
    backstory=(
        "Guiado por uma curiosidade e um desejo de repassar seu conhecimento de fora acessível"
        "e também explora novas tecnologias para visualização."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

novo_escritor=Agent(
    role="Escritor",
    goal="Escrever histórias envolventes sobre webscraping e como pode se aliar junto com AI",
    verbose=True,
    memory=True,
    backstory=(
        "Gosta de simplificar tópicos complexos"
        "cria histórias engajadoras que cativa e educa"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

tradutor=Agent(
    role="Tradutor",
    goal="Traduzir artigos para o português, de forma que não perca a informação e mantenha termos especifícos de inglês em inglês",
    verbose=True,
    memory=True,
    backstory=(
        "Tem como objetivo aperfeiçoar o texto sem mudar sua essência"
    ),
    llm=llm,
    allow_delegation=False
)