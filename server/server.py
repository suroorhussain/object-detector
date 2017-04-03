import jinja2

from os.path import abspath, dirname, join
from flask import Flask, render_template, request, send_from_directory
from ..object_detector.test_classifier import detect
from ..object_detector.helpers import get_abspath

server = Flask('aip', static_url_path='/images')
template_loader = jinja2.ChoiceLoader([
    server.jinja_loader,
    jinja2.FileSystemLoader(get_abspath('templates', __file__))
])
server.jinja_loader = template_loader

@server.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@server.route('/', methods=['GET'])
def upload_form():
    return render_template('index.html')

@server.route('/detect', methods=['POST'])
def detect_image():
    img = request.files.get('input')
    img.save(abspath(join(dirname(__file__), 'images/testimage.pgm')))
    detect(abspath(join(dirname(__file__), 'images/testimage.pgm')))
    return render_template('image.html')

@server.route('/images/<imgname>')
def send_image(imgname):
    return send_from_directory(get_abspath('images', __file__), imgname)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8000)
