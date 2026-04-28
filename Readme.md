# 🚀 Data Science Internship — Advanced Tasks
### DevelopersHub Corporation | Data Science & Analytics

**Author:** Awais Ahmed Memon
**Email:** [awaisahmed93@gmail.com](mailto:awaisahmed93@gmail.com)
**Education:** Computer Science Student
**Internship Track:** Data Science & Analytics — Advanced

---

### 🛠️ Tech Stack & Skills

![Python](https://img.shields.io/badge/Python-3.11-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Pandas](https://img.shields.io/badge/Pandas-DataFrame-FF6B35?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Array-00D4FF?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-FF3CAC?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-784BA0?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Boosting-00C853?style=for-the-badge&logo=python&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-Explainable_AI-FF4081?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)
![Status](https://img.shields.io/badge/Status-✅_Completed-00E676?style=for-the-badge)

---

> This repository contains **3 advanced data science tasks** completed as part of my internship at **DevelopersHub Corporation**. Each task demonstrates real-world problem solving across classification, unsupervised learning, and business intelligence using industry-standard Python tools and libraries.

---

## 📋 Table of Contents

| # | Task | Domain | Status |
|---|------|--------|--------|
| [Task 1](#-task-1-term-deposit-subscription-prediction) | Term Deposit Subscription Prediction | Classification + XAI | ✅ Done |
| [Task 2](#-task-2-customer-segmentation-using-unsupervised-learning) | Customer Segmentation | Clustering + Visualization | ✅ Done |
| [Task 5](#-task-5-interactive-business-dashboard-in-streamlit) | Interactive Business Dashboard | BI + Streamlit | ✅ Done |

---

## 📌 Task 1: Term Deposit Subscription Prediction

![Task](https://img.shields.io/badge/Task-Classification-FF6B35?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-Bank_Marketing_UCI-00D4FF?style=flat-square)
![XAI](https://img.shields.io/badge/XAI-SHAP-FF3CAC?style=flat-square)

### 🎯 Objective
Predict whether a bank customer will subscribe to a term deposit as a result of a phone-based marketing campaign — a classic binary classification problem with real business impact.

### 📂 Dataset
**Bank Marketing Dataset** — UCI Machine Learning Repository
- ~45,000 records of customer interactions
- Features include age, job type, marital status, previous campaign outcome, and more
- Target variable: `y` — has the client subscribed? (`yes` / `no`)

### 🔍 Approach
1. **Exploratory Data Analysis (EDA)** — Distribution plots, correlation heatmaps, class imbalance analysis
2. **Preprocessing** — Label encoding for ordinal features, one-hot encoding for nominals, feature scaling
3. **Model Training** — Logistic Regression (baseline) and Random Forest Classifier
4. **Evaluation** — Confusion Matrix, F1-Score, ROC-AUC Curve comparison
5. **Explainability** — SHAP values used to explain 5+ individual model predictions (waterfall & beeswarm plots)

### 📊 Results & Insights
- Random Forest achieved superior F1-Score and ROC-AUC over Logistic Regression
- SHAP analysis revealed `duration` (call duration), `poutcome` (previous campaign outcome), and `euribor3m` (interest rate) as the top predictors of subscription
- Customers contacted in May had notably lower conversion rates

### 🧠 Skills Demonstrated
`Classification Modeling` · `Feature Encoding` · `Model Evaluation` · `Explainable AI (SHAP)` · `Customer Behavior Analysis`

📓 **Notebook:** [Open Task 1 Notebook](./Task1_Bank_Marketing.ipynb)

---

## 📌 Task 2: Customer Segmentation Using Unsupervised Learning

![Task](https://img.shields.io/badge/Task-Clustering-784BA0?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-Mall_Customers-00E676?style=flat-square)
![Method](https://img.shields.io/badge/Method-K--Means_+_PCA-FFD43B?style=flat-square)

### 🎯 Objective
Cluster mall customers based on spending habits and annual income, then propose data-driven marketing strategies tailored to each customer segment.

### 📂 Dataset
**Mall Customers Dataset**
- 200 customer records
- Features: `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score (1–100)`

### 🔍 Approach
1. **Exploratory Data Analysis (EDA)** — Distribution of income vs spending score, age distribution, gender breakdown
2. **Optimal K Selection** — Elbow Method and Silhouette Score analysis
3. **K-Means Clustering** — Segmenting customers into distinct behavioral groups
4. **Dimensionality Reduction** — PCA and t-SNE for 2D cluster visualization
5. **Strategy Development** — Marketing recommendation per cluster based on behavioral profile

### 📊 Results & Insights

| Cluster | Profile | Suggested Strategy |
|---------|---------|-------------------|
| 🟢 Cluster 1 | High Income, High Spend | Loyalty rewards, premium memberships |
| 🔵 Cluster 2 | High Income, Low Spend | Re-engagement campaigns, personalized offers |
| 🟡 Cluster 3 | Low Income, High Spend | Budget-friendly bundles, EMI options |
| 🔴 Cluster 4 | Low Income, Low Spend | Discount drives, awareness campaigns |
| 🟣 Cluster 5 | Mid Income, Average Spend | Seasonal promotions, upselling |

- Optimal number of clusters: **5** (confirmed by both Elbow and Silhouette)
- PCA and t-SNE both produced clean, well-separated cluster visualizations

### 🧠 Skills Demonstrated
`Unsupervised Learning` · `K-Means Clustering` · `PCA` · `t-SNE` · `Customer Segmentation` · `Strategy Development`

📓 **Notebook:** [Open Task 2 Notebook](./Task2_Customer_Segmentation (1).ipynb)

---

## 📌 Task 5: Interactive Business Dashboard in Streamlit

![Task](https://img.shields.io/badge/Task-Business_Intelligence-FF4B4B?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-Global_Superstore-00D4FF?style=flat-square)
![Tool](https://img.shields.io/badge/Tool-Streamlit-FF4081?style=flat-square)

### 🎯 Objective
Build a fully interactive business intelligence dashboard to analyze sales, profit trends, and segment-wise performance across regions and product categories.

### 📂 Dataset
**Global Superstore Dataset**
- ~51,000 orders across multiple countries
- Features: Order Date, Region, Category, Sub-Category, Sales, Profit, Discount, Customer Name, and more

### 🔍 Approach
1. **Data Cleaning & Preparation** — Handling nulls, type conversions, date parsing
2. **Feature Engineering** — Derived metrics (Profit Margin %, Month-Year, etc.)
3. **Dashboard Design in Streamlit:**
   - Sidebar filters: **Region**, **Category**, **Sub-Category**
   - KPI cards: Total Sales, Total Profit, Profit Margin
   - Bar chart: Top 5 Customers by Sales
   - Line chart: Monthly Sales Trend
   - Heatmap: Category vs Region profitability

### 📊 Dashboard Features

| Component | Description |
|-----------|-------------|
| 🗺️ Region Filter | Drill down by geography |
| 📦 Category Filter | Focus on Furniture, Office Supplies, or Technology |
| 💰 KPI Cards | Real-time aggregated metrics |
| 👤 Top Customers | Ranked bar chart of top 5 by revenue |
| 📈 Sales Trend | Month-over-month line chart |

### Key Insights
- Technology category yields the highest profit margins
- Western region consistently outperforms other regions in total sales
- High discounts in the Furniture category often result in negative profit margins

### 🧠 Skills Demonstrated
`Streamlit Dashboarding` · `Business Intelligence` · `Data Storytelling` · `KPI Design` · `Interactive Filtering`

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://datascienceinternshipassignment2-kjedvkmzgxiaffs6eob3ux.streamlit.app/)

---

## 📁 Repository Structure

```
📦 DevelopersHub-DS-Internship
├── 📓 Task1_Term_Deposit_Prediction.ipynb
├── 📓 Task2_Customer_Segmentation.ipynb
├── 🐍 Task5_Business_Dashboard.py
├── 📂 data/
│   ├── bank-marketing.csv
│   ├── mall_customers.csv
│   └── global_superstore.csv
├── 📂 outputs/
│   ├── plots/
│   └── models/
└── 📄 README.md
```

---

## ✅ Submission Checklist

- [x] Jupyter Notebooks with full EDA, modeling, and visualizations
- [x] Well-commented, readable, and structured code
- [x] GitHub repository with descriptive name
- [x] README with objectives, approach, and results
- [x] Submitted via Google Classroom

---

## 📬 Contact

| Platform | Link |
|---------|------|
| 📧 Email | [awaisahmed93@gmail.com](mailto:awaisahmed93@gmail.com) |
| 💼 LinkedIn | *Add your LinkedIn URL here* |
| 🐙 GitHub | *Add your GitHub profile URL here* |

---

<div align="center">

**Made with ❤️ by Awais Ahmed Memon**
*Data Science Intern @ DevelopersHub Corporation*

![Visitors](https://img.shields.io/badge/Internship-DevelopersHub_Corporation-00D4FF?style=for-the-badge)
![Completed](https://img.shields.io/badge/Tasks_Completed-3%2F5-00E676?style=for-the-badge)

</div>
