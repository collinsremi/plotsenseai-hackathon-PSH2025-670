# 🌍 Air Quality Insights & Prediction  
**Plotsense Hackathon Submission — Track 1 (PlotSense ML)**  

**User ID:** `PSH2025-670`
**Track:** PlotSense ML  
**Team Name:** Remz  

---

## 📌 Project Description  

Urban air pollution is a major global health challenge. This project analyzes a large dataset of air quality metrics across 20+ cities worldwide, performs **exploratory data analysis (EDA)** using **Plotsense**, and builds a **machine learning model** to classify **Air Quality Index (AQI)** categories.  

It also extends the analysis into an **interactive Streamlit dashboard**, allowing users to visualize data, explore Plotsense-generated insights, and make real-time AQI predictions.

👉 [**Live Demo on Streamlit Cloud**](https://plotsense-app-seb2b5repevpalepalvbye.streamlit.app/)  

---

## 🚀 What We Did  

### 1️⃣ Data Cleaning & Preparation  
- Handled missing values and validated pollutant ranges.  
- Computed AQI sub-indices for **PM2.5, PM10, NO2, SO2, CO, O3** using EPA breakpoints.  
- Created a consolidated **AQI Category** column with the following classes:  
  - `Good`, `Moderate`, `Unhealthy-Sensitive`, `Unhealthy`, `Very Unhealthy`.  

---

### 2️⃣ Exploratory Data Analysis (EDA) with Plotsense  
We used Plotsense to automate visual generation and explanation:  
- **`recommender`** → Suggested suitable plot types for AQI & pollutants.  
- **`plotgen`** → Generated high-quality visualizations (bar, box, scatter, pie).  
- **`explainer`** → Produced Markdown-ready insights for each visualization.  

**Examples of analyses:**  
- Null value distribution (bar plot)  
- AQI category distribution (pie chart with interpretation)  
- Pollutant correlations (scatter plots, e.g. NO2 vs PM10)  
- City-wise comparisons (boxplots for PM10 & PM2.5)  

Plotsense allowed us to move from raw data to **publication-ready insights** quickly.

---

### 3️⃣ Handling Imbalanced Data  
- Detected severe imbalance (e.g., “Good” AQI < 1%).  
- Generated synthetic samples for underrepresented classes to balance training data.  
- Improved model robustness across AQI categories.

---

### 4️⃣ Machine Learning Pipeline  
We trained an **XGBoost Classifier** to predict AQI Category.  

**Preprocessing:**  
- Encoded categorical features (City, Country) with `LabelEncoder`.  
- Standardized numerical variables with `StandardScaler`.  

**Modeling & Evaluation:**  
- Train/test split (80/20).  
- Reported accuracy, precision, recall, and F1 scores per class.  
- Results stored and visualized for interpretability.

---

### 5️⃣ Interactive Streamlit App 🌐  
We built and deployed a Streamlit app to make insights and predictions accessible:  

- **Upload CSV Data** → Preview and explore datasets.  
- **View Saved Plots** → Interactively browse Plotsense visualizations & explanations.  
- **Make Predictions** → Input pollutant levels and predict AQI Category using the trained model.  

👉 [Live Streamlit App](https://plotsense-app-seb2b5repevpalepalvbye.streamlit.app/)

This bridges the gap between **data science analysis** and **real-world decision making**.

---

## 📊 Key Insights  
- Over **80%** of observations fall into **Unhealthy** or **Very Unhealthy** categories.  
- **NO2 and PM10** have a strong positive correlation (r ≈ 0.78).  
- Asian cities (e.g., Bangkok, Mumbai) show higher median pollutant levels than European/North American cities.  
- “Good” air quality is almost nonexistent in the dataset.  

---

## 💡 Why This Matters  
- 🏥 **Public Health:** Enables early warning systems and better air quality communication.  
- 🏛 **Policy:** Provides evidence for targeted interventions in high-risk cities.  
- 🧠 **Hackathon Goal:** Demonstrates how Plotsense can streamline **EDA → Modeling → Visualization → Deployment** in a single workflow.

---

## 🛠 Tech Stack  
- **Core:** pandas, numpy, Plotsense
- **ML:** scikit-learn, xgboost  
- **Visualization & Insights:** Plotsense (`recommender`, `plotgen`, `explainer`)  
- **Deployment:** Streamlit Cloud

---

## 📝 Setup Instructions  

```bash
# Clone the repo
git clone https://github.com/yourusername/plotsenseai-hackathon-PSH2025-670.git
cd plotsenseai-hackathon-PSH2025-670

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run interface.py

---

## 👥 Team Members  
| Name         | Role                        |
|-------------|-----------------------------|
| Diugwu Izudiugwu | ML Engineer / Developer     |

---

## 🔗 Social Media  
- [Twitter/X Post](https://x.com/your-post-link)  
- [LinkedIn Post](https://linkedin.com/in/your-profile-or-post-link)  

---

## 🎥 Demo Video  
[YouTube Demo Link](https://youtube.com/your-demo-video-link)  


---

## ✨ Acknowledgement  
This project was built as part of the **Plotsense Hackathon 2025**, showcasing how Plotsense accelerates **EDA, visualization, storytelling, and app deployment** in real-world data science workflows.

