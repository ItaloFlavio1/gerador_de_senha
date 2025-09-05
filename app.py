from flask import Flask, render_template, request, flash
from gerador import gerar_senha

app = Flask(__name__)
app.secret_key = "chave_super_secreta"

@app.route("/", methods=["GET", "POST"])
def index():
    senha_gerada = None
    comprimento_atual = 12
    usar_letras_atual = True
    usar_numeros_atual = True
    usar_simbolos_atual = False

    if request.method == "POST":
        try:
            comprimento_atual = int(request.form.get("comprimento", 12))
        except ValueError:
            flash("Comprimento inválido!")
            comprimento_atual = 12

        usar_letras_atual = "letras" in request.form
        usar_numeros_atual = "numeros" in request.form
        usar_simbolos_atual = "simbolos" in request.form

        senha_gerada = gerar_senha(
            comprimento_atual,
            usar_letras_atual,
            usar_numeros_atual,
            usar_simbolos_atual
        )

        if senha_gerada in ["Nenhuma opção selecionada!", "Comprimento inválido!"]:
            flash(senha_gerada)
            senha_gerada = None

    return render_template(
        "index.html",
        senha=senha_gerada,
        comprimento=comprimento_atual,
        usar_letras=usar_letras_atual,
        usar_numeros=usar_numeros_atual,
        usar_simbolos=usar_simbolos_atual
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
