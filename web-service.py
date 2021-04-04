from flask import *

app = Flask('Solar-Assistant')
app.secret_key = "lololololol"

@app.route('/')
def render_main():
  return render_template('home.html')

@app.route('/<path:path>')
def send_root(path):
    return send_from_directory('templates',path)

@app.route('/calculator',methods=["POST","GET"])
def calc():
    if request.method == "POST":
        yield1 = request.form['entry.1994759724']
        Module_Temp = request.form['entry.1369317306']
        Insolation = request.form['entry.766253923']
        print(yield1,Module_Temp,Insolation)
        return redirect(url_for("calc_result",yield1 = yield1,module_temp = Module_Temp,insolation = Insolation))
    else:
        return render_template('calculator.html')

@app.route('/<yield1>?<module_temp>?<insolation>')
def calc_result(yield1,module_temp,insolation):
    return render_template('result.html',yield1 = yield1,module_temp = module_temp,insolation = insolation)


app.run(debug=False)