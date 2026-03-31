import os

# 1. Lista de seus trabalhos (Adicione novos aqui!)
meus_projetos = [
    {
        "titulo": "Sistema de Gestão de Estoque",
        "desc": "Automação com Python e SQLite para controle de entrada/saída.",
        "link": "https://github.com/seu-usuario/projeto-estoque"
    },
    {
        "titulo": "Dashboard de Vendas Real-Time",
        "desc": "Visualização de dados dinâmica usando bibliotecas de BI.",
        "link": "https://github.com/seu-usuario/projeto-dashboard"
    }
]

# 2. O Molde do Site (Template)
template_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Portfólio de Projetos Freela</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Projetos Freela</h1>
        <p>Desenvolvedor de Soluções e Automações</p>
    </header>
    <main>
        <section id="projetos">
            {cards_de_projeto}
        </section>
    </main>
</body>
</html>
"""

# 3. Lógica para gerar os Cards
cards = ""
for p in meus_projetos:
    cards += f'''
    <div class="card">
        <h3>{p["titulo"]}</h3>
        <p>{p["desc"]}</p>
        <a href="{p["link"]}" class="btn">Ver Projeto</a>
    </div>
    '''

# 4. Criar o arquivo index.html final
with open("index.html", "w", encoding="utf-8") as f:
    f.write(template_html.format(cards_de_projeto=cards))

print("✅ Sucesso! O arquivo index.html foi atualizado pelo Antigravity.")