from flask import Flask, request, render_template, jsonify
from utils import search_by_lesson
from utils import next_day
import logging
import werkzeug

app = Flask(__name__)

@app.route("/")
def page_index():
    return render_template('index.html', title='Home', posts=next_day())



@app.route("/search")
def search_by_word():
    week_days = search_by_lesson(request.args.get("s"))
    return render_template('search.html', title='Home', posts=week_days)


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    logging.warning(e)
    return ' статус-код 404', 404


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def handle_serverError(e):
    logging.error(e)
    return 'статус-код 500', 500


app.register_error_handler(404, handle_bad_request)
app.register_error_handler(500, handle_serverError)
app.run()
