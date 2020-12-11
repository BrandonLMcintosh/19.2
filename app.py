from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "MassivelySuperSecret"
debug = DebugToolbarExtension(app)

@app.route("/")
def index():
    return render_template('index.html', story=stories.story)

@app.route("/story", methods=["POST"])
def create_story():
    print("####################################################")
    print(request.form)
    answers = dict(request.form.to_dict(flat=True))
    return render_template('story.html', story=stories.story, answers=answers)


