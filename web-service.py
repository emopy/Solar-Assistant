from flask import *

app = Flask('Solar-Assistant')

@app.route('/')
def render_main():
  return render_template('index.html')


app.run(debug=False)