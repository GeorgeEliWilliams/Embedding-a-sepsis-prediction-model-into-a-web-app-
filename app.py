from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

# create a fastapi instance
app = FastAPI

# features/inputs that will be passed to the model along with the dtypes
class InputData(BaseModel):
    Plasma_glucose : int
    Blood_Work_Result_1 : int
    Blood_Pressure : int
    Blood_Work_Result_2 : int
    Blood_Work_Result_3 : int
    Body_mass_index : float
    Blood_Work_Result_4 :float
    Age : int
    Insurance : int


# Load the saved prediction model using pickle
with open("models.pkl", "rb") as model_file:
    sepsis_model = pickle.load(model_file)

@app.post('/sepsis_prediction')
def sepsis_prediction(model_parameters : InputData):
    input_features = model_parameters.model_dump_json
    input_dictionary = json.loads(input_features)

    glucose = input_dictionary['Plasma_glucose']
    BW1 = input_dictionary['Blood_Work_Result_1']
    BP = input_dictionary['Blood_Pressure']
    BW2 = input_dictionary['Blood_Work_Result_2']
    BW3 = input_dictionary['Blood_Work_Result_3']
    BMI = input_dictionary['Body_Mass_Index']
    BW4 = input_dictionary['Blood_Work_Result_4']
    Age = input_dictionary['Age']
    Insurance = input_dictionary['Insurance']

    input_list = [glucose, BW1, BP, BW2, BW3, BMI, BW4, Age, Insurance]

    prediction = sepsis_model.predict([input_list])

    if prediction[0] == 0:
        return 'The individual does not have sepsis'
    else:
        return 'The individual hs sepsis'







