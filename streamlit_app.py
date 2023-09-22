import streamlit as st
from src.churn.pipeline.predict_pipeline import CustomData, PredictPipeline

# Streamlit app title
st.title("Customer Churn Prediction App")

# Define the input form
st.sidebar.header("User Input")
age = st.sidebar.slider("Age", 18, 100, 18)
gender = st.sidebar.radio("Gender", ["Male", "Female"])
location = st.sidebar.selectbox("Location", ["Los Angeles", "New York", "Miami", "Chicago", "Houston"])
subscription_length = st.sidebar.slider("Subscription Length (Months)", 1, 24, 1)
monthly_bill = st.sidebar.number_input("Monthly Bill Amount", 0.0)
total_usage_gb = st.sidebar.number_input("Total Usage (GB)", 0.0)

# Add a "Predict" button with improved styling
predict_button = st.sidebar.button("Predict", key='predict_button')

if predict_button:
    # Create a CustomData object from user input
    user_data = CustomData(
        Age=age,
        Gender=gender,
        Location=location,
        Subscription_Length_Months=subscription_length,
        Monthly_Bill=monthly_bill,
        Total_Usage_GB=total_usage_gb
    )

    # Create a DataFrame from the CustomData object
    input_data = user_data.get_data_as_data_frame()

    # Make a prediction using your PredictPipeline
    prediction_pipeline = PredictPipeline()

    try:
        results = prediction_pipeline.predict(input_data)
        result_value = "Churn" if results[0] == 1 else "Not-Churn"
    except Exception as e:
        # Handle the prediction error
        st.error('Prediction failed. Please check your input data.')
        st.stop()

    # Display the prediction result in the middle of the screen
    st.markdown("<h1 style='text-align:center; font-size:36px;'>Predicted Result: {}</h1>".format(result_value), unsafe_allow_html=True)
