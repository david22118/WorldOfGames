import Utils
from flask import Flask

app = Flask(__name__)


def read_content():
    file = open(Utils.SCORES_FILE_NAME, 'r')
    return file.read()


def content_message(content):
    wrapper = f"""<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1 id="description">The score is <span id="score">{content}</span></h1>
        </body>
    </html>"""
    return wrapper


def error_content_message():
    wrapper = f"""<html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1 id="description" >Error <span id="score" style="color:red">{Utils.BAD_RETURN_CODE}</span></h1>
            </body>
    </html>"""
    return wrapper


@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return error_content_message(), int(Utils.BAD_RETURN_CODE)


@app.route("/get_score")
def score_server():
    content = read_content()
    return content_message(content)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8777)
