from flask import Flask, render_template,request

app = Flask(__name__)

Usuarios = [
    {
        "id": 1,
        "nome": "Dar aula sobre métodos HTTP",
        "endereço": "Dar aula sobre métodos HTTP"
    },
    {
        "id": 2,
        "nome": "Dar aula sobre métodos HTTP",
        "endereço": "Dar aula sobre métodos HTTP"
    },
]

@app.route('/', methods=['GET', 'POST'])
def render_usuario():
        print(request.method)

        if request.method == "POST":
            id = Usuarios[-1]["id"] + 1
            name = request.form["nome"]
            endereço = request.form["endereço"]
            Usuarios.append({
                "id": id,
                "nome": name,
                "endereço": endereço,
            })

        return render_template('usuarios.html', pamonha=Usuarios)

app.run(debug=True)