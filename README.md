# 🛒 Online Retail Customer Segmentation

## 📌 Project Overview
This project applies **Unsupervised Machine Learning** techniques to segment customers of an online retail store based on their purchasing behavior.  
The dataset contains all transactions between **01/12/2010 and 09/12/2011** for a UK-based online retailer.

The main objective is to identify **customer segments** (loyal customers, churn risk, etc.) using **RFM Analysis** (Recency, Frequency, Monetary) and clustering algorithms.

---

## 📊 Problem Statement
Businesses often struggle to design effective marketing strategies without knowing their customer base.  
Through segmentation, we aim to:
- Identify different types of customers.
- Tailor marketing campaigns for each group.
- Improve customer retention and maximize revenue.

---

## 🔧 Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Scipy  
- **Algorithms:** K-Means, DBSCAN, Hierarchical Clustering  
- **Tools:** Jupyter Notebook  

---

## 📂 Dataset
The dataset is sourced from the UCI Machine Learning Repository and contains:
- Transactional records (Invoice No, Stock Code, Quantity, Invoice Date, Unit Price, Customer ID, Country).
- Period: **Dec 2010 – Dec 2011**.

---

## 🚀 Project Workflow
1. **Data Preprocessing**
   - Handling missing values
   - Removing duplicates
   - Feature engineering: Creating **RFM Model**
2. **Exploratory Data Analysis (EDA)**
   - Distribution plots, outlier analysis
   - Correlation heatmaps
3. **Clustering**
   - K-Means (Elbow Method, Silhouette Score)
   - DBSCAN
   - Hierarchical Clustering (Dendrograms)
4. **Model Evaluation**
   - Optimal number of clusters = **2**
   - Cluster profiling based on RFM scores
5. **Business Insights**
   - Cluster 0: Low-value, less-engaged customers
   - Cluster 1: High-value, frequent customers

---

## ✅ Conclusion
This project successfully demonstrates how **unsupervised learning** can reveal hidden patterns in customer behavior.  
Using **RFM Analysis** combined with clustering algorithms, we identified **two distinct customer groups**:
- **High-value, loyal customers** who contribute significantly to revenue.
- **Low-value, infrequent customers** who are at risk of churn.  

These insights can guide businesses in creating **targeted marketing strategies**, improving customer retention, and maximizing revenue.  
The methodology is **scalable and ready for real-world deployment**, making it a valuable solution for customer segmentation in e-commerce and retail businesses.

---

## 📈 Future Scope
- Deploy the clustering pipeline as a **web application** using Flask or Streamlit.  
- Build an **interactive dashboard** in Power BI/Tableau for real-time monitoring.  
- Incorporate **demographic and behavioral features** for richer segmentation.  
- Experiment with **advanced clustering methods** (Gaussian Mixture Models, Spectral Clustering).  
- Apply **deep learning-based autoencoders** for dimensionality reduction before clustering.  
- Integrate the model into a **marketing automation system** to trigger personalized campaigns.

---
