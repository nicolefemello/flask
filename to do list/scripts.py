tasks = [
    {"id": 1, "title": "Comprar leite", "description": "Ir ao supermercado e comprar leite", "status": "Pendente"},
    {"id": 2, "title": "Estudar Flask", "description": "Ler a documentação e criar um projeto simples", "status": "Em andamento"},
    {"id": 3, "title": "Exercitar-se", "description": "Fazer uma caminhada de 30 minutos", "status": "Concluído"}
]

def add_task(title, description):
    new_id = max(task['id'] for task in tasks) + 1 if tasks else 1
    tasks.append({"id": new_id, "title": title, "description": description, "status": "Pendente"})

def update_task_status(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Concluído' if task['status'] == 'Pendente' else 'Pendente'
            return True
    return False

def delete_task(task_id):
    global tasks
    tasks[:] = [task for task in tasks if task['id'] != task_id]