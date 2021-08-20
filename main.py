from flask import Flask,request,jsonify
import logging

app = Flask(__name__)

def countBmi(height,weight):
    height = height/100
    height = height*height
    value = weight/height
    return round(value,1)

@app.route('/')
def func():

    try:                                            # validation that the input must be numeric
        heightValue= int(request.args["height"])
        weightValue = int(request.args["weight"])
    except:                                         # throw error in response body and log to application logger
       app.logger.error('Height and Weight must be numeric')
       return "Height and Weight must be numeric !",500
    if heightValue < 1:
        app.logger.error('Height must not be 0 or negative !')
        return "Height must not be 0 or negative !",500
    elif weightValue < 1:
        app.logger.error('Weight must not be 0 or negative !')
        return "Weight must not be 0 or negative !",500
    bmiValue = countBmi(heightValue,weightValue)

    if bmiValue >= 25:
        index="overweight"
    elif bmiValue < 18.5:
        index="underweight"
    elif bmiValue >= 18.5 and bmiValue <= 24.9:
        index="healthy"

    return jsonify(BMI=bmiValue, label=index)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug= True)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)