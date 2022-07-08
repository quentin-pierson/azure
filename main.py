import requests
from flask import Flask, render_template, request
from form import Research, Upload
from flask_bootstrap import Bootstrap
import config.azure_config as azure_config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ErnR468dnezfheI3FUbeehui3'
Bootstrap(app)

az = azure_config.AzureServices()
@app.route('/', methods=['GET'])
def home():

    form = Research(request.form)
    form.tags.data = az.get_tags()
    return render_template('/form_tags.html', form=form)

@app.route('/set_picture', methods=['POST'])
def set_picture():
    form = Research(request.form)
    # img = az.get_picture(form.tags.data)
    img = "https://www.wapiti-magazine.com/wp-content/uploads/sites/26/2018/12/loutre-de-mer.jpg"
    return render_template('/form_tags.html', img=img, form=form)

@app.route('/picture', methods=['POST'])
def picture():
    if request.method == 'POST':
        request.g

        pass
    pass


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = Upload(request.form)
    return render_template('/form_img.html', form=form)


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000, debug=True, use_debugger=True, use_reloader=True)
    app.run(host='localhost', debug=True, port=5001)
