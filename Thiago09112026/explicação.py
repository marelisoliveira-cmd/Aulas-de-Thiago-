
# IMPORTACAO DAS BIBLIOTECAS
# Foi acrescentado o redirect e o session.
# redirect permite mudar de pagina.
# session permite controlar quem esta conectado.
from flask import Flask, render_template_string, request, redirect, session

# Cria a aplicacao Flask
app = Flask(__name__)

# ALTERACAO: foi adicionada uma chave secreta.
# POR QUE: para permitir o funcionamento das sessoes.
app.secret_key = "chave_calculadora_123"


# TELA DE LOGIN
# Cria o HTML que sera mostrado ao usuario.
HTML_LOGIN = """
<h2>Login</h2>

<form method="POST">

    <!-- Campo para digitar o usuario -->
    <input type="text" name="usuario" placeholder="Usuario" required>

    <br><br>

    <!-- Campo para digitar a senha -->
    <input type="password" name="senha" placeholder="Senha" required>

    <br><br>

    <!-- Botao para entrar -->
    <button type="submit">Entrar</button>

</form>

<!-- Mostra mensagens de erro -->
<p>{{ mensagem }}</p>
"""


# TELA DA CALCULADORA
# Cria o formulario das operacoes matematicas.
HTML_CALCULADORA = """
<h2>Calculadora</h2>

<form method="POST" action="/calcular">

    <!-- Campo do primeiro numero -->
    <input type="number" step="any" name="numero1" placeholder="Primeiro numero" required>

    <br><br>

    <!-- Campo do segundo numero -->
    <input type="number" step="any" name="numero2" placeholder="Segundo numero" required>

    <br><br>

    <!-- Opcoes de operacoes matematicas -->
    <select name="operacao">
        <option value="+">Soma (+)</option>
        <option value="-">Subtracao (-)</option>
        <option value="*">Multiplicacao (*)</option>
        <option value="/">Divisao (/)</option>
    </select>

    <br><br>

    <!-- Botao para realizar o calculo -->
    <button type="submit">Calcular</button>

</form>

<!-- Local onde aparece o resultado -->
<h3>{{ resultado }}</h3>

<!-- ALTERACAO: foi adicionado um link para sair -->
<!-- POR QUE: para permitir que o usuario encerre a sessao -->
<a href="/sair">Sair</a>
"""


# ROTA PRINCIPAL DO LOGIN
# ALTERACAO: a rota aceita GET e POST.
# POR QUE: GET mostra a tela e POST recebe os dados do login.
@app.route("/", methods=["GET", "POST"])
def login():

    mensagem = ""

    if request.method == "POST":

        # Recebe o usuario informado
        usuario = request.form.get("usuario")

        # Recebe a senha informada
        senha = request.form.get("senha")

        # Verifica se os dados estao corretos
        if usuario == "admin" and senha == "1234":

            # ALTERACAO: registra o login na sessao.
            # POR QUE: para identificar que o usuario entrou corretamente.
            session["logado"] = True

            # Redireciona para a calculadora
            return redirect("/calculadora")

        else:

            # Mostra mensagem se os dados estiverem incorretos
            mensagem = "Usuario ou senha incorretos!"

    # Exibe a tela de login
    return render_template_string(HTML_LOGIN, mensagem=mensagem)


# ROTA DA CALCULADORA
@app.route("/calculadora")
def calculadora():

    # ALTERACAO: foi adicionada a verificacao da sessao.
    # POR QUE: impedir o acesso a calculadora sem fazer login.
    if not session.get("logado"):
        return redirect("/")

    # Mostra a calculadora
    return render_template_string(HTML_CALCULADORA, resultado="")


# ROTA RESPONSAVEL PELOS CALCULOS
@app.route("/calcular", methods=["POST"])
def calcular():

    # ALTERACAO: verifica se o usuario esta conectado.
    # POR QUE: proteger tambem a rota dos calculos.
    if not session.get("logado"):
        return redirect("/")

    # ALTERACAO: foi utilizado try/except.
    # POR QUE: evitar que dados invalidos interrompam o programa.
    try:

        # Recebe o primeiro numero e converte para decimal
        n1 = float(request.form["numero1"])

        # Recebe o segundo numero e converte para decimal
        n2 = float(request.form["numero2"])

        # Recebe a operacao escolhida
        operacao = request.form["operacao"]

        # Verifica se foi escolhida a soma
        if operacao == "+":
            resultado = n1 + n2

        # Verifica se foi escolhida a subtracao
        elif operacao == "-":
            resultado = n1 - n2

        # Verifica se foi escolhida a multiplicacao
        elif operacao == "*":
            resultado = n1 * n2

        # Verifica se foi escolhida a divisao
        elif operacao == "/":

            # ALTERACAO: verifica se o segundo numero e zero.
            # POR QUE: impedir uma divisao por zero.
            if n2 == 0:
                resultado = "Erro: divisao por zero!"

            else:
                resultado = n1 / n2

        else:

            # ALTERACAO: verifica operacoes desconhecidas.
            # POR QUE: evitar operacoes que nao existem.
            resultado = "Operacao invalida!"

        # Mostra o resultado na pagina
        return render_template_string(
            HTML_CALCULADORA,
            resultado=f"Resultado: {resultado}"
        )

    # ALTERACAO: trata valores ou campos incorretos.
    # POR QUE: mostrar uma mensagem em vez de interromper o programa.
    except (ValueError, KeyError):

        return render_template_string(
            HTML_CALCULADORA,
            resultado="Digite numeros validos!"
        )


# ROTA PARA SAIR DO SISTEMA
# ALTERACAO: foi criada uma nova rota /sair.
# POR QUE: permitir que o usuario encerre sua sessao.
@app.route("/sair")
def sair():

    # Apaga os dados da sessao
    session.clear()

    # Retorna para a tela inicial
    return redirect("/")


# INICIALIZACAO DO PROGRAMA
if __name__ == "__main__":

    # Inicia o servidor Flask em modo de desenvolvimento
    app.run(debug=True)

