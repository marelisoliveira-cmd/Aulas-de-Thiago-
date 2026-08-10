<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Meu primeiro projeto Front-End</title> 
    <link rel="stylesheet" href="estilo.css"> 
    <script src="script.js" defer></script>
</head>
<body>
    <header class="cabecalho">
        <p class="etiqueta">Programação Front-End • 2º DS Subsequente</p>
        <h1>Meu primeiro projeto Front-End</h1>
        <p>Uma página organizada para conferir se HTML, CSS e JavaScript estão conectados corretamente.</p>
    </header>

    <main>
        <section class="painel" aria-labelledby="titulo-arquivos">
            <h2 id="titulo-arquivos">Arquivos do projeto</h2>
            <div class="grade-arquivos">
                <article>
                   <strong>index.html</strong>
                   <span>Organiza o conteúdo e conecta os demais arquivos.</span>
                </article>
                <article>
                    <strong>estilo.css</strong>
                    <span>Controla cores, espaçamentos e responsividade.</span>
                </article>
                <article>
                    <strong>script.js</strong>
                    <span>Adiciona comportamento e responde às ações do usuário.</span>
                </article>
                <article>
                    <strong>README.md</strong>
                    <span>Documenta o projeto, o estudante e a forma de execução.</span>
                </article>
            </div>
        </section>
        
        <section class="painel" aria-labelledby="titulo-teste">
            <h2 id="titulo-teste">Teste do ambiente</h2>
            <p>Abra a página no navegador e use o botão para verificar a ligação entre os arquivos.</p>
            <button id="testarProjeto" type="button">Verificar projeto</button>
            <p id="statusProjeto" class="status" aria-live="polite">Aguardando a verificação.</p>
        </section>
    </main>

    <footer>
        <p>Exercício FE01 • Colégio Estadual Alberto Gomes Veiga</p>
    </footer>
</body>
</html>

