# main.py

# main.py

perguntas = {
    "nome_projeto": "Nome do projeto: ",
    "descricao": "Descrição do projeto: ",
    "tecnologias": "Tecnologias utilizadas (separadas por vírgula): ",
    "instalacao": "Como instalar o projeto: ",
    "uso": "Como utilizar o projeto: ",
    "licenca": "Licença: "
}

respostas = {}

for chave, pergunta in perguntas.items():
    respostas[chave] = input(pergunta)

readme = f"""# {respostas['nome_projeto']}

## Descrição
{respostas['descricao']}

## Tecnologias
{', '.join([tech.strip() for tech in respostas['tecnologias'].split(',')])}

## Instalação
{respostas['instalacao']}

## Uso
{respostas['uso']}

## Licença
{respostas['licenca']}
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("\n✅ README.md gerado com sucesso!")
