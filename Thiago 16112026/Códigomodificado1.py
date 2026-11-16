
from flask import Flask, request, render_template_string

app = Flask(__name__)

# ==================================================
# ALTERAÇÃO 1: VISUAL DO SISTEMA
# Adicionado CSS para melhorar cores, botões,
# tabelas, campos e organização das páginas.
# ==================================================

ESTILO = """
<style>
* {
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: #eef2f7;
    margin: 0;
    padding: 25px 15px;
    color: #263238;
}

.container {
    background: white;
    max-width: 650px;
    margin: 35px auto;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.10);
}

h1, h2 {
    text-align: center;
    color: #1e3a5f;
}

p {
    text-align: center;
}

label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
}

input, select {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccd5df;
    border-radius: 7px;
    font-size: 15px;
    margin-bottom: 18px;
}

button {
    width: 100%;
    padding: 13px;
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 7px;
    font-size: 16px;
    cursor: pointer;
    font-weight: bold;
}

button:hover {
    background: #1d4ed8;
}

a {
    display: block;
    text-align: center;
    color: #2563eb;
    margin-top: 20px;
    text-decoration: none;
    font-weight: bold;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th {
    background: #2563eb;
    color: white;
    padding: 13px;
}

td {
    padding: 12px;
    text-align: center;
    border-bottom: 1px solid #ddd;
}

tr:nth-child(even) {
    background: #f1f5f9;
}

.resultado {
    background: #eff6ff;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin-top: 20px;
    font-size: 20px;
    color: #1d4ed8;
    font-weight: bold;
}

.erro {
    color: #dc2626;
    text-align: center;
}

.opcoes {
    background: #f8fafc;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
}
</style>
"""


# ==================================================
# ALTERAÇÃO 2: LOGIN
# Mantido usuário admin e senha 1234.
# Melhorada a aparência da tela.
# ==================================================

HTML_LOGIN = ESTILO + """
<div class="container">

    <h1>Sistema Matemático</h1>
    <h2>Login do Sistema</h2>

    <form method="POST">

        <label>Usuário:</label>
        <input type="text" name="usuario"
               placeholder="Digite seu usuário" required>

        <label>Senha:</label>
        <input type="password" name="senha"
               placeholder="Digite sua senha" required>

        <button type="submit">Entrar</button>

    </form>

</div>
"""


# ==================================================
# ALTERAÇÃO 3: MENU PRINCIPAL
# Agora os campos aparecem conforme a opção escolhida.
# O conversor possui seleção de origem e destino.
# ==================================================

HTML_MENU = ESTILO + """
<div class="container">

    <h1>Sistema Matemático</h1>

    <p>Escolha uma ferramenta para utilizar.</p>

    <form action="/executar" method="POST">

        <label>Escolha uma opção:</label>

        <select name="opcao" id="opcao" onchange="mostrarCampos()">
            <option value="calculadora">Calculadora</option>
            <option value="tabuada">Tabuada</option>
            <option value="parimpar">Par ou Ímpar</option>
            <option value="conversor">Conversor de Medidas</option>
        </select>

        <div class="opcoes">

            <div id="campo_num1">
                <label id="label_num1">Número 1:</label>
                <input type="number" step="any" name="num1"
                       placeholder="Digite um número" required>
            </div>

            <div id="campo_num2">
                <label>Número 2:</label>
                <input type="number" step="any" name="num2"
                       placeholder="Digite o segundo número">
            </div>

            <div id="campo_operacao">
                <label>Operação da Calculadora:</label>
                <select name="operacao">
                    <option value="+">Soma (+)</option>
                    <option value="-">Subtração (-)</option>
                    <option value="*">Multiplicação (*)</option>
                    <option value="/">Divisão (/)</option>
                </select>
            </div>

            <div id="campo_conversor">

                <label>Converter de:</label>

                <select name="origem">
                    <option value="km">Quilômetro (km)</option>
                    <option value="m">Metro (m)</option>
                    <option value="cm">Centímetro (cm)</option>
                    <option value="mm">Milímetro (mm)</option>
                    <option value="kg">Quilograma (kg)</option>
                    <option value="g">Grama (g)</option>
                    <option value="mg">Miligrama (mg)</option>
                    <option value="l">Litro (L)</option>
                    <option value="ml">Mililitro (mL)</option>
                </select>

                <label>Converter para:</label>

                <select name="destino">
                    <option value="m">Metro (m)</option>
                    <option value="km">Quilômetro (km)</option>
                    <option value="cm">Centímetro (cm)</option>
                    <option value="mm">Milímetro (mm)</option>
                    <option value="kg">Quilograma (kg)</option>
                    <option value="g">Grama (g)</option>
                    <option value="mg">Miligrama (mg)</option>
                    <option value="l">Litro (L)</option>
                    <option value="ml">Mililitro (mL)</option>
                </select>

            </div>

        </div>

        <button type="submit">Executar</button>

    </form>

</div>

<script>
function mostrarCampos() {

    let opcao = document.getElementById("opcao").value;

    let num2 = document.getElementById("campo_num2");
    let operacao = document.getElementById("campo_operacao");
    let conversor = document.getElementById("campo_conversor");
    let label = document.getElementById("label_num1");

    num2.style.display = "none";
    operacao.style.display = "none";
    conversor.style.display = "none";

    if (opcao === "calculadora") {
        num2.style.display = "block";
        operacao.style.display = "block";
        label.innerText = "Número 1:";
    }

    else if (opcao === "tabuada") {
        label.innerText = "Número da tabuada:";
    }

    else if (opcao === "parimpar") {
        label.innerText = "Digite um número:";
    }

    else if (opcao === "conversor") {
        label.innerText = "Valor para converter:";
        conversor.style.display = "block";
    }
}

mostrarCampos();
</script>
"""


# ==================================================
# ALTERAÇÃO 4: ROTA DE LOGIN
# Mantida a verificação de usuário e senha.
# ==================================================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == "admin" and senha == "1234":
            return render_template_string(HTML_MENU)

        return render_template_string(
            ESTILO + """
            <div class="container">
                <h2 class="erro">Usuário ou senha incorretos!</h2>
                <a href="/">Voltar ao login</a>
            </div>
            """
        )

    return render_template_string(HTML_LOGIN)


# ==================================================
# ALTERAÇÃO 5: CALCULADORA
# Mantidas soma, subtração, multiplicação e divisão.
# ==================================================

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
                    return render_template_string(
                        ESTILO + """
                        <div class="container">
                            <h2 class="erro">Erro: divisão por zero!</h2>
                            <a href="/">Voltar</a>
                        </div>
                        """
                    )

                resultado = n1 / n2

            else:
                return "Operação inválida!"

            return render_template_string(
                ESTILO + """
                <div class="container">

                    <h1>Resultado da Calculadora</h1>

                    <div class="resultado">
                        {{ n1 }} {{ operacao }} {{ n2 }}
                        = {{ resultado }}
                    </div>

                    <a href="/">Voltar ao menu</a>

                </div>
                """,
                n1=n1,
                n2=n2,
                operacao=operacao,
                resultado=resultado
            )


        # ==========================================
        # ALTERAÇÃO 6: TABUADA EM FORMATO DE TABELA
        # Agora os resultados aparecem organizados
        # em duas colunas, de 1 até 10.
        # ==========================================

        elif opcao == "tabuada":

            numero = int(float(request.form.get("num1")))

            return render_template_string(
                ESTILO + """
                <div class="container">

                    <h1>Tabuada do {{ numero }}</h1>

                    <table>

                        <tr>
                            <th>Multiplicação</th>
                            <th>Resultado</th>
                        </tr>

                        {% for i in range(1, 11) %}
                        <tr>
                            <td>{{ numero }} x {{ i }}</td>
                            <td>{{ numero * i }}</td>
                        </tr>
                        {% endfor %}

                    </table>

                    <a href="/">Voltar ao menu</a>

                </div>
                """,
                numero=numero
            )


        # ==========================================
        # PAR OU ÍMPAR
        # Mantida a lógica original com visual novo.
        # ==========================================

        elif opcao == "parimpar":

            numero = int(float(request.form.get("num1")))

            if numero % 2 == 0:
                texto = "PAR"
            else:
                texto = "ÍMPAR"

            return render_template_string(
                ESTILO + """
                <div class="container">

                    <h1>Resultado</h1>

                    <div class="resultado">
                        O número {{ numero }} é {{ texto }}!
                    </div>

                    <a href="/">Voltar ao menu</a>

                </div>
                """,
                numero=numero,
                texto=texto
            )


        # ==========================================
        # ALTERAÇÃO 7: CONVERSOR DE MEDIDAS
        # O usuário escolhe a unidade de origem
        # e a unidade de destino.
        #
        # Comprimento: km, m, cm e mm.
        # Massa: kg, g e mg.
        # Capacidade: L e mL.
        # ==========================================

        elif opcao == "conversor":

            valor = float(request.form.get("num1"))

            origem = request.form.get("origem")
            destino = request.form.get("destino")

            unidades = {

                # Comprimento
                "km": ("Comprimento", 1000, "km"),
                "m": ("Comprimento", 1, "m"),
                "cm": ("Comprimento", 0.01, "cm"),
                "mm": ("Comprimento", 0.001, "mm"),

                # Massa
                "kg": ("Massa", 1, "kg"),
                "g": ("Massa", 0.001, "g"),
                "mg": ("Massa", 0.000001, "mg"),

                # Capacidade
                "l": ("Capacidade", 1, "L"),
                "ml": ("Capacidade", 0.001, "mL")
            }

            if origem not in unidades or destino not in unidades:
                return "Unidade inválida!"

            # Verifica se as unidades são da mesma categoria.

            if unidades[origem][0] != unidades[destino][0]:

                return render_template_string(
                    ESTILO + """
                    <div class="container">

                        <h2 class="erro">Conversão inválida!</h2>

                        <p>Escolha unidades da mesma categoria.</p>

                        <a href="/">Voltar ao menu</a>

                    </div>
                    """
                )

            # Realiza o cálculo da conversão.

            resultado = (
                valor * unidades[origem][1]
                / unidades[destino][1]
            )

            nome_origem = unidades[origem][2]
            nome_destino = unidades[destino][2]

            return render_template_string(
                ESTILO + """
                <div class="container">

                    <h1>Conversão de Medidas</h1>

                    <p>Categoria: {{ categoria }}</p>

                    <div class="resultado">
                        {{ valor }} {{ origem }}
                        =
                        {{ resultado }} {{ destino }}
                    </div>

                    <a href="/">Voltar ao menu</a>

                </div>
                """,
                categoria=unidades[origem][0],
                valor=valor,
                origem=nome_origem,
                destino=nome_destino,
                resultado=resultado
            )


        else:

            return "Opção inválida!"

    except (ValueError, TypeError):

        return render_template_string(
            ESTILO + """
            <div class="container">

                <h2 class="erro">Erro nos dados informados!</h2>

                <p>Verifique os números digitados.</p>

                <a href="/">Voltar ao menu</a>

            </div>
            """
        )


# ==================================================
# INICIALIZAÇÃO DO SISTEMA
# ==================================================

if __name__ == "__main__":
    app.run(debug=True)
