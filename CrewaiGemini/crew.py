from crewai import Crew, Process
from agents import novo_escritor, novo_pesquisador, tradutor
from task import tarefa_pesquisador, tarefa_escritor, tarefa_tradutor

crew = Crew(
    agents=[novo_pesquisador, novo_escritor, tradutor],
    tasks=[tarefa_escritor,tarefa_pesquisador, tarefa_tradutor],
    process=Process.sequential,
)

result=crew.kickoff(inputs={'topic':'O novo petróleo e Serviços Cloud'})
print(result)