import numpy as np
import pickle
import streamlit as st
import sklearn

loaded_model = pickle.load(open('./Models/trained_model.sav', 'rb'))

#creating the function for prediction
def accident_prediction(input_data):
    
    #change to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==1):
        return "An accident is likely to occur based on the current conditions."
    else:
        return "No accident predicted with the given inputs."
    
    
def main():
    # giving the title
    st.title("RailGuard")
    
    # getting the input data from the user
    Track_Class = st.text_input("Track Class")
    Gross_Tonnage = st.text_input("Gross Tonnage")
    Maximum_Speed = st.text_input("Maximum Speed")
    Train_Speed = st.text_input("Train Speed")
    Joint_Track_Class = st.text_input("Joint Track Class")
    Track_Type_Code = st.text_input("Track Type Code")
    Station_encoded = st.text_input("Station (Encoded)")
    Track_Name_encoded = st.text_input("Track Name (Encoded)")
    
    result = ''
    
    # creating a button for the prediction
    if st.button('Accident Prediction Result'):
        result = accident_prediction([Track_Class, Gross_Tonnage, Maximum_Speed, Train_Speed, 
                                         Joint_Track_Class, Track_Type_Code, Station_encoded, Track_Name_encoded])
        
    st.success(result)
    
if __name__ == '__main__':
    main()




    
    
    
    
    