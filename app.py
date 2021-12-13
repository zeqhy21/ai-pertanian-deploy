from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

class_dict = {0: 'banana',
              1: 'blackgram',
              2: 'chickpea',
              3: 'coconut',
              4: 'coffee',
              5: 'cotton',
              6: 'jute',
              7: 'kidneybeans',
              8: 'lentil',
              9: 'maize',
              10: 'mango',
              11: 'mothbeans',
              12: 'mungbean',
              13: 'muskmelon',
              14: 'orange',
              15: 'papaya',
              16: 'pigeonpeas',
              17: 'pomegranate',
              18: 'rice',
              19: 'watermelon'}

@app.route('/')
def index():
    return render_template('index.html', hasil_prediksi_tanaman="")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    nitrogen, fosfor, kalium, suhu, kelembaban, phtanah, curahhujan  = [x for x in request.form.values()]

    data = []

    data.append(float(nitrogen))
    data.append(float(fosfor))
    data.append(float(kalium))
    data.append(float(suhu))
    data.append(float(kelembaban))
    data.append(float(phtanah))
    data.append(float(curahhujan))
    # if sex == 'Laki-laki':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])

    # if smoker == 'Ya':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])
    
    prediction = model.predict([data])
    crop_name = class_dict[prediction[0]]
    output = crop_name
    #output = prediction

    return render_template('index.html', hasil_prediksi_tanaman=output, nitrogen=nitrogen, fosfor=fosfor, kalium=kalium, suhu=suhu, kelembaban=kelembaban, phtanah=phtanah, curahhujan=curahhujan)


if __name__ == '__main__':
    app.run(debug=True)