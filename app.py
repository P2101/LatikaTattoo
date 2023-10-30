from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/index.html')
def galeria():
    carpeta_imagenes = "imgs"
    imagenes = [imagen for imagen in os.listdir(carpeta_imagenes) if imagen.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return render_template('index.html', imagenes=imagenes)

@app.route('/galeria')
def redirigir_a_index():
    return redirect(url_for('galeria'))

if __name__ == '__main__':
    app.run(debug=True)