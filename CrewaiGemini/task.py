from crewai import Task
from tools import tool
from agents import novo_escritor, novo_pesquisador, tradutor

tarefa_pesquisador = Task(
    description=(
        "Identificar a próxima grande tendência sobre {topic}."
        "Focar no como utilizar e na narrativa"
        "Seu relatório final deve deixar claro os pontos chaves,"
        "E falar sobre as oportunidades e os riscos."
        ),
        expected_output="3 longos paragráfos do relatório compreensiveis, sobre as últimas tendências de AI e Dados",
        tools=[tool],
        agent=novo_pesquisador
)

tarefa_escritor = Task(
    description=(
        "Escrever um artigo com ideias sobre {topic}."
        "Focar nas novidades e como isso impactaria os serviços cloud"
        "Seu artigo tem que ser fácil de entender, positivo e engajado"
        ),
        expected_output="4 longos paragráfos sobre {topic} formatados com excelente em Markdown",
        tools=[tool],
        agent=novo_escritor,
        async_execution=False
)

tarefa_tradutor= Task(
     description=(
        "Traduzir o artigo sobre o tópico {topic}."
        "Focar em manter termos chaves inglês em inglês"
        ),
        expected_output="4 longos paragráfos sobre {topic} formatados com excelente em Markdown em português",
        tools=[tool],
        agent=tradutor,
        async_execution=False,
        output_file="novo_artigo_traduzido.md"
)