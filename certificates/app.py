import os, json
from PIL import Image, ImageFont, ImageDraw
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def read_json(f):
    f = os.path.abspath(f)
    with open(f) as f:
        data = json.load(f)
    return data

@app.route("/")
def index():
    return "Efico Certificate Generate, Navigate to /certificate/<email>, remove everything after @ in the email"


@app.route("/certificate/<email>")
def generate(email):
    certificate = {
        'Image Path': "Path nt found, it seems your email is not authorized"
    }
    for data in read_json('detailsList.json'):
        if email.lower() == data['email'].split('@')[0].lower():
            certificate = make_certificate(data['name'])
    return certificate


def make_certificate(name):
    def draw_text(filename, name):
        font = "LibreBaskerville-Italic.otf"
        color = "#3b181d"
        size = 30
        y = 290
        x = 0
        text = "{}".format(name).upper()
        raw_img = Image.open(filename)
        img = raw_img.copy()
        draw = ImageDraw.Draw(img)

        # draw name
        PIL_font = ImageFont.truetype(os.path.join("fonts", font), size)
        w, h = draw.textsize(text, font=PIL_font)
        W, H = img.size
        x = 305 + (W - 305 - w)/2 if x == 0 else x
        draw.text((x, y), text, fill=color, font=PIL_font)

        filename = "{}.png".format(('-').join(name.split(' ')))



        path = os.path.join(os.path.abspath('../assets/img/certificates'), filename)
        print(path)
        img.save(path)
        return {
            'Image Path':path
            }
    cert = draw_text("certificate.png", name)
    return jsonify(cert)


if __name__ == "__main__":
    app.run(debug=True)