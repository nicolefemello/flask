from flask import Flask, render_template

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Comprar leite", "description": "Ir ao supermercado e comprar leite", "status": "Pendente"},
    {"id": 2, "title": "Estudar Flask", "description": "Ler a documentação e criar um projeto simples", "status": "Em andamento"},
    {"id": 3, "title": "Exercitar-se", "description": "Fazer uma caminhada de 30 minutos", "status": "Concluído"}
]

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)