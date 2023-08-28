import json
import requests

url = "http://127.0.0.1:8000/sepsis_prediction"

input_data_for_model = {
    'Plasma_glucose' : 6,
    'Blood_Work_Result_1' : 148,
    'Blood_Pressure' : 72,
    'Blood_Work_Result_2' : 35,
    'Blood_Work_Result_3' : 0,
    'Body_mass_index' : 33.6,
    'Blood_Work_Result_4' : 0.627,
    'Age' : 50,
    'Insurance' : 0
}

response = requests.post(url, json=input_data_for_model)

print(response.text)