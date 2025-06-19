from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# 課題9-1: GETメソッドでHTMLを返す
@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>FastAPI ホームページ</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #0066cc;
                }
            </style>
        </head>
        <body>
            <h1>ようこそ！FastAPIの世界へ</h1>
            <p>これはGETメソッドで表示されたページです。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# 課題9-2: POSTメソッドで文字列を受け取り、JSONで返す
@app.post("/present")
async def give_present(present: str):
    return {"response": f"サーバです。メリークリスマス！{present}ありがとう。お返しはキャンディーです。"}
