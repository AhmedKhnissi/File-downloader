from flask import Flask, jsonify, send_from_directory, render_template
import os

app = Flask(__name__)
FILES_DIR = 'Listed&Downloaded_Files'

@app.route('/')
def index():
    files = os.listdir(FILES_DIR)
    return render_template('index.html', files=files)

@app.route('/api/files')
def list_files():
    files = os.listdir(FILES_DIR)
    return jsonify(files)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(FILES_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
