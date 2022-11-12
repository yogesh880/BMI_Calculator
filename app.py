from flask import Flask,render_template,request

app =Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi=''
    message=''
    if request.method == 'POST' and 'weight' in request.form :
        weight=float(request.form.get('weight'))
        height=float(request.form.get('height'))
        bmi= calc_bmi(weight,height)
        if bmi<19:
            message='under weight'
        elif bmi>19 and bmi<25:
            message='Normal weight'
        elif bmi>=25 and bmi<30:
            message='Over weight'
        else:
            message='Obesity'
    return render_template("bmi_calc.html",
                            bmi=bmi,message=message)
def calc_bmi(weight,height):
    return round((weight/((height/100)**2)),2)

app.run()