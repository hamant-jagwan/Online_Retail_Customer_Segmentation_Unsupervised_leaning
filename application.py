import streamlit as st
import pickle
import numpy as np

# Load scaler and KMeans model
with open("scaler.pkl", "rb") as f:
    loaded_scaler = pickle.load(f)

with open("kmeans_model.pkl", "rb") as f:
    loaded_kmeans = pickle.load(f)

# Streamlit App UI
st.title("🛍️ RFM Customer Segmentation")

st.write("Enter customer Recency, Frequency, and Monetary values to classify the customer into a segment.")

# User Inputs
recency = st.number_input("Recency (days since last purchase):", min_value=0, step=1)
frequency = st.number_input("Frequency (number of purchases):", min_value=0, step=1)
monetary = st.number_input("Monetary (total spend):", min_value=0, step=1)

if st.button("Predict Cluster"):
    # Convert to numpy array
    new_customer = np.array([[recency, frequency, monetary]])

    # Preprocess
    new_customer_scaled = loaded_scaler.transform(new_customer)

    # Predict
    cluster = loaded_kmeans.predict(new_customer_scaled)[0]

    # Display Result
    if cluster == 0:
        st.error("⚠️  This customer belongs to **Cluster 0 → At Risk / Low Value**")
    else:
        st.success("✅ This customer belongs to **Cluster 1 → Loyal / High Value**")
