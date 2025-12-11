from flask import Flask, render_template,request,redirect

app = Flask(__name__)

usuarios = [
    {
        "id": 1,
        "nome": "cláudio",
        "endereço": "Rua 12345"
    },
    {
        "id": 2,
        "nome": "Maria",
        "endereço": "Rua 54321"
    },
]

@app.route('/', methods=['GET', 'POST'])
def render_usuario():
        print(request.method)

        if request.method == "POST":
            name = request.form["nome"]
            endereco = request.form["endereço"]

            if len(name) == 0:
                return render_template(
                'usuarios.html', 
                usuarios=usuarios, 
                erro="Nome é obrigatório"
            )

            id = usuarios[-1]["id"] + 1
            usuarios.append({
                    "id": id,
                    "nome": name,
                    "endereço": endereco
            })
        return render_template('usuarios.html', pamonha=usuarios)

@app.route('/excluir/<int:id>')
def excluir_usuarios(id):
     usuarios.pop(id)
     return redirect('/')


@app.route('/editar/<int:id>', methods=["GET", "POST"])
def editar_usuario(id):
    usuario = usuarios[id]

    if request.method == "POST":
        nome = request.form["nome"]
        endereco= request.form["endereço"]

        usuarios[id] = {
            "id": usuario["id"],
            "nome": nome,
            "endereço": endereco
        }

        return redirect('/')

    return render_template('editar.html', usuario=usuario)

@app.route('/testes')
def render_testes():
    return render_template('teste.html')


app.run(debug=True)