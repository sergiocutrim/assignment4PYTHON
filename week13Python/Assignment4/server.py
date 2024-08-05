from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/Static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'Static'), filename)

print(__name__)
@app.route("/")
def home():
    return  render_template("index.html")

if __name__ == "__main__":
     app.run()
