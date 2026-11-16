#mexer no visual 

from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_LOGIN = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>

    <h2>Login do Sistema</h2>

    <form method="POST">
        <input type="text" name="usuario" placeholder="Usuário" required>
        <br><br>

        <input type="password" name="senha" placeholder="Senha" required>
        <br><br>

        <button type="submit">Entrar</button>
    </form>

</body>
</html>
"""

HTML_MENU = """
<!DOCTYPE html>
<html>
<head>
    <title>Sistema Matemático</title>
</head>
<body>

    <h1>Sistema Matemático</h1>

    <form action="/executar" method="POST">

        <label>Escolha uma opção:</label>

        <select name="opcao">
            <option value="calculadora">Calculadora</option>
            <option value="tabuada">Tabuada</option>
            <option value="parimpar">Par ou Ímpar</option>
            <option value="conversor">Conversor de Medidas</option>
        </select>

        <br><br>

        <input type="number"
               step="any"
               name="num1"
               placeholder="Número 1"
               required>

        <br><br>

        <input type="number"
               step="any"
               name="num2"
               placeholder="Número 2">

        <br><br>

        <label>Operação da Calculadora:</label>

        <select name="operacao">
            <option value="+">Soma (+)</option>
            <option value="-">Subtração (-)</option>
            <option value="*">Multiplicação (*)</option>
            <option value="/">Divisão (/)</option>
        </select>

        <br><br>

        <button type="submit">
            Executar
        </button>

    </form>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == "admin" and senha == "1234":
            return render_template_string(HTML_MENU)

        return """
        <h2>Usuário ou senha incorretos!</h2>
        <a href="/">Voltar</a>
        """

    return render_template_string(HTML_LOGIN)


@app.route("/executar", methods=["POST"])
def executar():

    opcao = request.form.get("opcao")

    try:

        if opcao == "calculadora":

            n1 = float(request.form.get("num1"))
            n2 = float(request.form.get("num2"))

            operacao = request.form.get("operacao")

            if operacao == "+":
                resultado = n1 + n2

            elif operacao == "-":
                resultado = n1 - n2

            elif operacao == "*":
                resultado = n1 * n2

            elif operacao == "/":

                if n2 == 0:
                    return """
                    <h2>Erro: divisão por zero.</h2>
                    <a href="/">Voltar</a>
                    """

                resultado = n1 / n2

            return f"""
            <h1>Resultado</h1>

            <p>
                {n1} {operacao} {n2}
                =
                <strong>{resultado}</strong>
            </p>

            <a href="/">Voltar</a>
            """

        elif opcao == "tabuada":

            numero = int(float(request.form.get("num1")))

            resultado = "<h1>Tabuada</h1>"

            for i in range(1, 11):
                resultado += f"<p>{numero} x {i} = {numero * i}</p>"

            resultado += '<br><a href="/">Voltar</a>'

            return resultado

        elif opcao == "parimpar":

            numero = int(float(request.form.get("num1")))

            if numero % 2 == 0:
                texto = "PAR"
            else:
                texto = "ÍMPAR"

            return f"""
            <h1>Resultado</h1>

            <p>O número {numero} é {texto}</p>

            <a href="/">Voltar</a>
            """

        elif opcao == "conversor":

            metros = float(request.form.get("num1"))

            centimetros = metros * 100
            milimetros = metros * 1000

            return f"""
            <h1>Conversão</h1>

            <p>{metros} m = {centimetros} cm</p>

            <p>{metros} m = {milimetros} mm</p>

            <a href="/">Voltar</a>
            """

        else:

            return """
            <h2>Opção inválida.</h2>
            <a href="/">Voltar</a>
            """

    except Exception as erro:

        return f"""
        <h2>Erro encontrado:</h2>
        <p>{erro}</p>

        <br>

        <a href="/">Voltar</a>
        """


if __name__ == "__main__":
    app.run(debug=True)