from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Ana sayfa - Çıkma teklifi"""
    return render_template('index.html')

@app.route('/heart')
def heart():
    """Kalp sayfası - Evet dedikten sonra"""
    return render_template('kalp.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
