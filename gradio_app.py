import gradio as gr
from src.churn.pipeline.predict_pipeline import CustomData, PredictPipeline

# Define the prediction function
def predict_data(Age, Gender, Location, Subscription_Length_Months, Monthly_Bill, Total_Usage_GB):
    try:
        # Create a CustomData object from user input
        user_data = CustomData(
            Age=float(Age),
            Gender=Gender,
            Location=Location,
            Subscription_Length_Months=int(Subscription_Length_Months),
            Monthly_Bill=float(Monthly_Bill),
            Total_Usage_GB=int(Total_Usage_GB)
        )

        # Create a DataFrame from the CustomData object
        input_data = user_data.get_data_as_data_frame()

        # Make a prediction using your PredictPipeline
        prediction_pipeline = PredictPipeline()
        results = prediction_pipeline.predict(input_data)

        # Determine the result message based on the prediction
        if results[0] == 0:
            result_value = "Not-Churn"
        else:
            result_value = "Churn"

        return result_value

    except Exception as e:
        # Handle the prediction error
        print("Prediction Error:", e)
        return 'Prediction failed'

# Define the Gradio interface
iface = gr.Interface(
    fn=predict_data,
    inputs=[
        gr.inputs.Number(label="Age"),
        gr.inputs.Radio(["Male", "Female"], label="Gender"),
        gr.inputs.Radio(["Los Angeles", "New York", "Miami", "Chicago", "Houston"], label="Location"),
        gr.inputs.Number(label="Subscription Length (Months)"),
        gr.inputs.Number(label="Monthly Bill Amount"),
        gr.inputs.Number(label="Total Usage (GB)")
    ],
    outputs=gr.outputs.Textbox(label="Prediction")
)

if __name__ == '__main__':
    iface.launch()
