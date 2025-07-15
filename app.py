from flask import Flask

app = Flask(__name__)

# Bu fonksiyon HTML sayfalarını oluşturur
def render_page(title, content_html):
    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background-image: url('https://raw.githubusercontent.com/kbgyazilim46/Yakuza/main/background.jpg');
                background-size: cover;
                background-position: center;
                color: white;
                text-shadow: 1px 1px 3px black;
            }}
            nav {{
                background-color: rgba(0,0,0,0.6);
                padding: 15px;
                text-align: center;
            }}
            nav a {{
                color: #fff;
                text-decoration: none;
                margin: 0 15px;
                font-weight: bold;
            }}
            .content {{
                background-color: rgba(0,0,0,0.6);
                padding: 40px;
                margin: 50px auto;
                width: 80%;
                border-radius: 15px;
            }}
            footer {{
                text-align: center;
                font-size: 13px;
                padding: 20px;
                background-color: rgba(0,0,0,0.7);
                position: fixed;
                bottom: 0;
                width: 100%;
                color: #ccc;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Ana Sayfa</a>
            <a href="/hakkinda">Hakkında</a>
            <a href="/iletisim">İletişim</a>
        </nav>

        <div class="content">
            {content_html}
        </div>

        <footer>
            © BU SİTEDEKİ HERŞEY GİZLİLİK İÇİNDEDİR
        </footer>
    </body>
    </html>
    """

@app.route('/')
def index():
    content = "<h1>Yakuza'ya Hoşgeldiniz</h1><p>Bu, Yakuza'nın kişisel sitesidir.</p>"
    return render_page("Ana Sayfa", content)

@app.route('/hakkinda')
def hakkinda():
    content = "<h1>Hakkında</h1><p>İletişim için aşağıdaki adreslerden ulaşabilirsiniz.</p>"
    return render_page("Hakkında", content)

@app.route('/iletisim')
def iletisim():
    content = """
    <h1>İletişim</h1>
    <ul>
        <li><strong>Instagram:</strong> yakuzaxzw</li>
        <li><strong>Discord:</strong> yakuzaressh</li>
        <li><strong>TikTok:</strong> yakuzaxr7</li>
        <li><strong>Rave:</strong> yakuzaressh</li>
    </ul>
    """
    return render_page("İletişim", content)

if __name__ == '__main__':
    app.run(debug=True)