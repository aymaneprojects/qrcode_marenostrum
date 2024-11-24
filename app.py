from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/'

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None
    if request.method == "POST":
        link = request.form.get("link")
        if link:
            # Génération du QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Sauvegarde dans le dossier static
            qr_code_path = os.path.join(app.config['UPLOAD_FOLDER'], 'qr_code.png')
            img.save(qr_code_path)
            qr_code = 'static/qr_code.png'

    return render_template("index.html", qr_code=qr_code)

if __name__ == "__main__":
    app.run(debug=True)