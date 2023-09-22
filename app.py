from flask import Flask, request, render_template
from src.churn.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the home page.
    """
    return render_template('home.html')

@app.route('/predictdata', methods=['POST'])
def predict_data():
    # Get user input from the HTML form
    age = int(request.form.get('Age'))
    gender = request.form.get('Gender')
    location = request.form.get('Location')
    subscription_length = int(request.form.get('Subscription_Length_Months'))
    monthly_bill = float(request.form.get('Monthly_Bill'))
    total_usage_gb = int(request.form.get('Total_Usage_GB'))

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
        if results[0] == 0:
            result_value = "Not-Churn"
        else:
            result_value = "Churn"
    except Exception as e:
        # Handle the prediction error
        print("Prediction Error:", e)
        return render_template('home.html', error='Prediction failed')

    # Render the HTML template with the result_value
    return render_template('home.html', results=result_value)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
