# Para Rodar o código, precisa baixar a biblioteca Flask. Usando Pip install flash no terminal

from flask import Flask, render_template_string, request

app = Flask(__name__)

# Código HTML simples embutido para o formulário
HTML_TELA = '''
<form method="POST">
    <h2>Login</h2>
    <input type="text" name="usuario" placeholder="Usuário" required><br><br>
    <input type="password" name="senha" placeholder="Senha" required><br><br>
    <button type="submit">Entrar</button>
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        # Validação simples
        if usuario == "admin" and senha == "1234":
            return f"<h1>Sucesso! Bem-vindo, {usuario}.</h1>"
        else:
            return "<h1>Falha! Usuário ou senha incorretos.</h1><a href='/'>Tentar de novo</a>"

    return render_template_string(HTML_TELA)

if __name__ == '__main__':
    app.run(debug=True)