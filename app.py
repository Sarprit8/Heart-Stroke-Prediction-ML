import streamlit as st
import pandas as pd 
import joblib 

#load the model,scaler,column
model = joblib.load("Logistic.pkl")
scaler = joblib.load("scaler.pkl")
expected_column = joblib.load("columns.pkl")

#name given title and subtitle
st.title("Heart Stroke Prediction by Preet👨🏻‍⚕️")
st.markdown("Provide the following details to check your heart stroke risk:")

#user input data
age = st.slider("Age",18,100,40)
sex = st.selectbox("Sex",["Male","Female"])
chest_pain = st.selectbox("Chest Pain Type",["Atypical Angina (non-classic heart pain)",
                                              "Non-Anginal Pain (pain not caused by the heart)",
                                              "Typical Angina (classic heart-related pain)",
                                              "Asymptomatic (no chest pain)"])
resting_bp = st.number_input("Resting Blood Pressure ",80,200,120)
cholesterol = st.number_input("Cholesterol Level",100,600,200)
fasting_bs = st.selectbox("Fasting Blood Sugar >120 mg/dl",[0,1])
resting_ecg = st.selectbox("Resting ECG",["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60,220,150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])


# predict button press then analyze them
if st.button("Predict"):
     raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }
     
     input_df = pd.DataFrame([raw_input])
# raw data values not in expected_column then make it 0
     for col in expected_column:
          if col not in input_df.columns:
            input_df[col] = 0

     # Reorder columns
     input_df = input_df[expected_column]

 
    # Make prediction
     prediction = model.predict(input_df)[0]

    # Show result
     if prediction == 1:
      st.error("⚠️ High Risk of Heart Disease")
     else:
      st.success("✅ Low Risk of Heart Disease")            