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
    #form = Research(request.form)
    #form.tags.data = az.get_tags()
    #img = az.get_picture(form.tags.data)
    #if form.validate_on_submit():
    f = request.form
    # 'form': ImmutableMultiDict([('tags', 'watch'), ('tags', 'person'), ('tags', 'man'), ('submit', 'Submit')])
    tags = []
    for key in f:
        if "tags" in key:
            tags.append(key["tags"])
        pass
    return str(tags)
    img = az.find_picture(tags)
    #img = "https://www.wapiti-magazine.com/wp-content/uploads/sites/26/2018/12/loutre-de-mer.jpg"
    return render_template('/set_picture.html', img=img, tags=tags)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = Upload(request.form)
    return render_template('/form_img.html', form=form)


@app.route('/upload_done', methods=['GET', 'POST'])
def upload_done():
    if request.method == 'POST':
        if request.form:
            url = request.form['imageUrl']
            name = request.form['imageName']
            description = request.form['imageDescription']
            print(url)
            # az.insert_pictures(name, description, url)
    return render_template('/uploaded.html', url=url, name=name, description=description)


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000, debug=True, use_debugger=True, use_reloader=True)
    app.run(host='localhost', debug=True, port=5001)
