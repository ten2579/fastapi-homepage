from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>私のホームページ</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    color: #333;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #0066cc;
                }
                a {
                    text-decoration: none;
                    color: #ff6600;
                }
            </style>
        </head>
        <body>
            <h1>ようこそ！</h1>
            <p>FastAPIで作ったホームページです。</p>
            <p><a href="https://www.example.com" target="_blank">Exampleサイトを見る</a></p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
