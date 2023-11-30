from flask import Flask, render_template, redirect, url_for, request
from csp_new import *
from fertilizer import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/crop', methods=["GET", "POST"])
def crop():
    if request.method == "POST":
        constraints=[]
        soil_type = request.form.get("soil")
        temp = float(request.form.get("temp"))
        precipitation = float(request.form.get("Precipitation"))
        ph = float(request.form.get("ph"))
        humidity = float(request.form.get("humidity"))
        Irrigation_type = str(request.form.get("Irrigation_type"))
        irrigation_fre = float(request.form.get("Irrigation_Frequency"))
        location = "Rajasthan"
        constraints.extend([soil_type,precipitation,temp, humidity,
                           ph, Irrigation_type, irrigation_fre, location])
        crop_rank = calculate_best_crop(constraints, 1, [])
        crop_rank.sort(reverse=True)
        crop_rank = crop_rank[:10]
        
        for i in range(3):
            crop_rank[i][1]=crop_rank[i][1].capitalize()
        for i in range(3):
            crop_rank[i][2]=int(float(crop_rank[i][2]))
            crop_rank[i][5]=int(float(crop_rank[i][5]))
        for i in range(3):
            if crop_rank[i][1]==crop_rank[i+1][i]:
                crop_rank.remove(crop_rank[i])
        print(crop_rank)
        return render_template("submit.html", ex1=crop_rank[0], ex2=crop_rank[1], ex3=crop_rank[2])

    else:
        return render_template("crop.html")

@app.route('/Fertilizer',methods=['GET','POST'])
def fertilizer():
    if request.method=='POST':
        nitrogen=float(request.form.get("nitrogen"))
        potassium=float(request.form.get("potassium"))
        calcium=float(request.form.get("calcium"))
        moisture=float(request.form.get("moisture"))
        crop=str(request.form.get("crop"))
        constraints.extend([nitrogen,potassium,calcium,moisture,crop])
        fertilizer_suggestion=calculate_fertilizer(constraints,1,variables=[])
        fertilizer_suggestion.sort(reverse=True)
        fertilizer_suggestion=fertilizer_suggestion[0:4]
        for i in range(3):
            fertilizer_suggestion[i][2]=int(float(fertilizer_suggestion[i][2]))
        return render_template("fert_submit.html",ex1=fertilizer_suggestion[0],ex2=fertilizer_suggestion[1],ex3=fertilizer_suggestion[2])
    else:
        return render_template("fertilizer.html")

@app.route('/result')
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run()
