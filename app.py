import streamlit as st
import pandas as pd
import joblib

# --- Load Model and Scaler ---
try:
    # Load model and scaler using joblib
    model = joblib.load('model.pkl')
    scaler = joblib.load('scaler.pkl')
except FileNotFoundError:
    st.error("Model or scaler not found. Please run create_model.py first.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading model or scaler: {e}")
    st.stop()


# --- Streamlit App Interface ---
st.title("💰 Future Bank Balance Predictor ")
st.write("Enter the customer's financial details to get a prediction.")

# Create columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=40)
    annual_income = st.number_input("Annual Income", value=1000000)
    monthly_expenses = st.number_input("Monthly Expenses", value=40000)
    savings_rate = st.slider("Savings Rate", 0.0, 1.0, 0.25)
    debt_to_income_ratio = st.slider("Debt to Income Ratio", 0.0, 2.0, 0.35)
    current_investments_value = st.number_input("Current Investments Value", value=2000000)
    total_loan_amount = st.number_input("Total Loan Amount", value=500000)
    avg_credit_score = st.slider("Average Credit Score", 300, 850, 650)

with col2:
    inflation_rate = st.slider("Inflation Rate (%)", 0.0, 10.0, 6.0)
    interest_rate = st.slider("Interest Rate (%)", 0.0, 12.0, 7.0)
    years_of_employment = st.number_input("Years of Employment", value=10.0)
    job_stability_score = st.slider("Job Stability Score", 0.0, 1.0, 0.5)
    emergency_fund_value = st.number_input("Emergency Fund Value", value=200000)
    retirement_fund_contribution = st.number_input("Retirement Fund Contribution", value=100000)
    customer_segment = st.selectbox("Customer Segment", ["Bronze", "Silver", "Gold"])

# --- Prediction Logic ---
if st.button("🏦 Bank Balance Forecaster ✨"):
    # Convert customer segment to one-hot encoding
    segment_gold = 1 if customer_segment == 'Gold' else 0
    segment_silver = 1 if customer_segment == 'Silver' else 0

    # Create a DataFrame from the inputs
    input_data = pd.DataFrame({
        'Age': [age], 'Annual_Income': [annual_income], 'Monthly_Expenses': [monthly_expenses],
        'Savings_Rate': [savings_rate], 'Debt_to_Income_Ratio': [debt_to_income_ratio],
        'Current_Investments_Value': [current_investments_value], 'Total_Loan_Amount': [total_loan_amount],
        'Avg_Credit_Score': [avg_credit_score], 'Inflation_Rate': [inflation_rate], 'Interest_Rate': [interest_rate],
        'Years_of_Employment': [years_of_employment], 'Job_Stability_Score': [job_stability_score],
        'Emergency_Fund_Value': [emergency_fund_value], 'Retirement_Fund_Contribution': [retirement_fund_contribution],
        'Customer_Segment_Gold': [segment_gold], 'Customer_Segment_Silver': [segment_silver]
    })

    # Scale the input data and make a prediction
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    # Display the result
    st.success(f"Predicted Future Balance: ₹{prediction[0]:,.2f}")