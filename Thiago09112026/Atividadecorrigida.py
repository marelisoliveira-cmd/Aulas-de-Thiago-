
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

HTML_LOGIN = """
<h2>Login</h2>

<form method="POST">
    <input type="text" name="usuario" placeholder="Usuário" required>
    <br><br>

    <input type="password" name="senha" placeholder="Senha" required>
    <br><br>

    <button type="submit">Entrar</button>
</form>
"""

HTML_CALCULADORA = """
<h2>Calculadora</h2>

<form method="POST" action="/calcular">

    <input type="number" step="any" name="numero1"
    placeholder="Primeiro número" required>
    <br><br>

    <input type="number" step="any" name="numero2"
    placeholder="Segundo número" required>
    <br><br>

    <select name="operacao">
        <option value="+">Soma (+)</option>
        <option value="-">Subtração (-)</option>
        <option value="*">Multiplicação (*)</option>
        <option value="/">Divisão (/)</option>
    </select>

    <br><br>

    <button type="submit">Calcular</button>

</form>
"""

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "admin" and senha == "1234":
            return redirect(url_for("calculadora"))

        return """
        <h2>Usuário ou senha incorretos!</h2>
        <a href="/">Tentar novamente</a>
        """

    return render_template_string(HTML_LOGIN)


# ROTA PARA VOLTAR À CALCULADORA
@app.route("/calculadora")
def calculadora():

    return render_template_string(HTML_CALCULADORA)


@app.route("/calcular", methods=["POST"])
def calcular():

    n1 = float(request.form["numero1"])
    n2 = float(request.form["numero2"])
    operacao = request.form["operacao"]

    if operacao == "+":
        resultado = n1 + n2

    elif operacao == "-":
        resultado = n1 - n2

    elif operacao == "*":
        resultado = n1 * n2

    elif operacao == "/":

        if n2 == 0:
            return """
            <h2>Erro: não é possível dividir por zero.</h2>
            <a href="/calculadora">Voltar para calculadora</a>
            """

        resultado = n1 / n2

    else:
        return "Operação inválida!"

    return f"""
    <h1>Resultado</h1>

    <p>
        {n1} {operacao} {n2} =
        <strong>{resultado}</strong>
    </p>

    <br>

    <a href="/calculadora">Nova operação</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
