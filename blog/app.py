from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios_cadastrados = {"admin": "1234"}

noticias = {
    1: {
        "titulo": "Flask é eleito o melhor para iniciantes",
        "resumo": "Simplicidade atrai novos devs.",
        "conteudo": "O Flask permite criar sites rápidos com poucas linhas..."
    },
    2: {
        "titulo": "Python 2026: O que mudou?",
        "resumo": "A linguagem continua no topo.",
        "conteudo": "Novas bibliotecas de IA integradas ao Python facilitam a vida..."
    },
    3: {
        "titulo": "Novas funcionalidades do Python 3.12",
        "resumo": "Atualizações importantes para desenvolvedores.",
        "conteudo": "Python 3.12 trouxe novas funcionalidades de desempenho e segurança..."
    }
}

@app.route('/')
def home():
    return render_template('index.html', noticias=noticias)

@app.route('/noticia/<int:id>')
def visualizar_noticia(id):
    noticia = noticias.get(id)
    
    if noticia:
        return render_template('noticia.html', noticia=noticia)
    
    return "Notícia não encontrada!", 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
            return f"<h1>Bem-vindo, {usuario}! Login realizado.</h1><a href='/'>Voltar para Home</a>"
        else:
            return "Erro: Usuário ou senha inválidos!", 401
            
    return render_template('login.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        novo_usuario = request.form.get('usuario')
        nova_senha = request.form.get('senha')
        
        usuarios_cadastrados[novo_usuario] = nova_senha
        
        return redirect(url_for('login'))
        
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)