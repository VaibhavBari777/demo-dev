from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI() 

@app.get("/",response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!  i am second one and this this fourth one </h1>
        </body>
    </html>
    """
