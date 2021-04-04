from flask import *

app = Flask('Solar-Assistant')

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
        Sites = request.form['Sites']
        print(yield1,Module_Temp,Insolation,Sites)
        return redirect(url_for("calc_result",yield1 = yield1,module_temp = Module_Temp,insolation = Insolation,site = Sites))
    else:
        return render_template('calculator.html')

@app.route('/<yield1>?<module_temp>?<insolation>?<site>')
def calc_result(yield1,module_temp,insolation,site):
    Efficiency = 0
    message = "null"
    if site == "SiteA":
        Efficiency = float(yield1) / 658.35 * float(insolation) * (1+((float(module_temp) - 25) * -0.0042))
    elif site == "SiteB":
        Efficiency = float(yield1) / 480.38 * float(insolation) * (1 + ((float(module_temp) - 25) * -0.0042))
    elif site == "SiteC":
        Efficiency = float(yield1) / 379.78 * float(insolation) * (1 + ((float(module_temp) - 25) * -0.0042))

    Efficiency = float("{0:.2f}".format(Efficiency))
    if Efficiency <= 30:
        message = "Your solar modules need to be washed"
    else:
        message = "Your solar modules are good to be used"
    return render_template('result.html',efficiency = Efficiency,message = message)

@app.errorhandler(400)
def handle_invalid_req(somearg):
    return render_template("invalid_value.html")


app.run(debug=False)