# Customer Churn Prediction Machine Learning Project

Welcome to the Customer Churn Prediction project! This project is designed to help you understand how to predict customer churn using machine learning. Below, we'll provide an overview of the project, how to set up the environment, run the applications, and explore the project's structure and architecture.

## Project Overview

Customer churn is a critical concern for businesses, especially those offering subscription-based services. Churn prediction involves identifying customers who are likely to cancel their subscriptions. By predicting churn early, businesses can take proactive steps to retain customers and minimize revenue loss.

This project aims to build a churn prediction model using machine learning techniques. It takes into account various customer attributes and usage patterns to make predictions about whether a customer is likely to churn or not.

## Pending Tasks

- **GitHub Actions**: Automated workflows for testing, building, and deploying the project are pending.
- **AWS Deployment**: Deployment of the application on AWS infrastructure is also in progress.

## Usage

### Creating a New Environment

To get started, you can create a new Python environment using the provided `requirements.txt` file. This ensures that you have all the necessary dependencies installed.

```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

### Running the Flask App

You can open the Flask-based web application using the following command:

```bash
python app.py
```

### Running the Streamlit App

To open the Streamlit-based web application, use the following command:

```bash
streamlit run streamlit_app.py
```
### Running the Streamlit Web App (Deployed)
```bash
https://customer-churn-prediction-milanbeherazyx.streamlit.app/
```

### Running the Gradio App

To open the Gradio-based web application, use the following command:

```bash
python gradio_app.py
```

### Making Predictions

Once you have the web application running, you can input customer data to make predictions. Follow the instructions provided in the respective applications to enter customer details and get churn predictions.

## Project Structure and Architecture

The project is organized into several directories and files:

- `src/churn`: Contains the core project code.
  - `components`: Includes modules for data ingestion, data transformation, and model training.
  - `constants`: Stores project-specific constants.
  - `data`: Houses data used in the project (e.g., dataset files).
  - `pipeline`: Contains the prediction and training pipelines.
- `artifacts`: Holds model-related artifacts.
- `css`: Contains the project's CSS styles.
- `research`: Includes Jupyter notebooks for data exploration and model training.
- `templates`: Stores HTML templates for the web applications.
- `app.py`, `streamlit_app.py`, `gradio_app.py`: Application entry points.
- `main.py`: Main execution script.
- `Dockerfile`: Docker configuration for containerization.
- `requirements.txt`: List of project dependencies.
- `setup.py`: Project setup script.
- `README.md`: Project documentation.

The project follows a modular architecture, making it easy to maintain and extend. The components are organized to handle different aspects of the machine learning workflow, from data preprocessing to model training and prediction.

Enjoy exploring and using the Customer Churn Prediction Machine Learning Project! If you have any questions or need further assistance, feel free to reach out.