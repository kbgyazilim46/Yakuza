from flask import Flask

app = Flask(__name__)

contact_info = """
<h2>İletişim</h2>
<ul>
    <li><strong>Instagram:</strong> yakuzaxzw</li>
    <li><strong>Discord:</strong> yakuzaressh</li>
    <li><strong>TikTok:</strong> yakuzaxr7</li>
    <li><strong>Rave:</strong> yakuzaressh</li>
</ul>
"""

footer_text = "© BU SİTEDEKİ HERŞEY GİZLİLİK İÇİNDEDİR"

def render_page(title, content_html):
    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8" />
        <title>{title}</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background-image: url('https://raw.githubusercontent.com/kbgyazilim46/deneme-yakuzaya-sittir/main/background.jpg');
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
        </nav>
        <div class="content">
            {content_html}
        </div>
        <footer>
            {footer_text}
        </footer>
    </body>
    </html>
    """

@app.route('/')
def index():
    content = (
        "<h1>Yakuza'ya Hoşgeldiniz</h1>"
        "<p>Bu, Yakuza'nın kişisel sitesidir.</p>"
        "<hr>"
        "<h1>Hakkında</h1>"
        "<p>İletişim için aşağıdaki adreslerden ulaşabilirsiniz.</p>"
        f"{contact_info}"
    )
    return render_page("Ana Sayfa", content)

if __name__ == '__main__':
    app.run(debug=True)
