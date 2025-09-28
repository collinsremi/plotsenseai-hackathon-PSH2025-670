import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page setup
st.set_page_config(page_title="AQI Prediction App", page_icon="🌍", layout="wide")

# Sidebar Navigation
st.sidebar.title("🌿 AQI Dashboard")
page = st.sidebar.radio("📌 Navigate", ["Upload Data", "View Saved Plots", "Make Prediction"])

# ---------------------------
# Upload Dataset
# ---------------------------
st.divider()
if page == "Upload Data":
    st.header("📂 Load Dataset")
    data_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

    if data_file is not None:
        df = pd.read_csv(data_file)
        st.success("✅ Dataset loaded successfully!")
        st.dataframe(df.head(50))
    else:
        st.info("Please upload a dataset to view.")
    st.divider()


# ---------------------------
# View Saved Plots
# ---------------------------
elif page == "View Saved Plots":
    st.header("🖼️ Explore Saved Plots")
    image_folder = r"images"
    explanation_path = r"md_files"


    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["📊 Bar Charts", "Histogram", "🥧 Pie Charts", "Bar Chart", "Box Plot", "Pie Chart", "Pie Chart", "🔬 Scatter Plots", "Box Plot"])
    
    with tab1:
        st.image(os.path.join(image_folder, "Bar Chart1.png"))
        for explanation_file in os.listdir(explanation_path):
            if explanation_file.startswith("explainer_0") and explanation_file.endswith(".md"):
                explanation_path_full = os.path.join(explanation_path, explanation_file)
                with open(explanation_path_full, "r") as f:
                    st.markdown(f.read())
                break

    with tab2:
        st.image(os.path.join(image_folder, "Summary of Temperature Histogram.png"))
        for explanation_file in os.listdir(explanation_path):
            if explanation_file.startswith("explainer_1") and explanation_file.endswith(".md"):
                explanation_path_full = os.path.join(explanation_path, explanation_file)
                with open(explanation_path_full, "r") as f:
                    st.markdown(f.read())
                break

    with tab3:
        st.image(os.path.join(image_folder, "Pie Chart Country Distribution.png"))
        for explanation_file in os.listdir(explanation_path):
            if explanation_file.startswith("explainer_2") and explanation_file.endswith(".md"):
                explanation_path_full = os.path.join(explanation_path, explanation_file)
                with open(explanation_path_full, "r") as f:
                    st.markdown(f.read())
                break

    with tab4:
        st.image(os.path.join(image_folder, "Bar Chart AQI_PM2.5 by AQI Category.png"))
        for explanation_file in os.listdir(explanation_path):
            if explanation_file.startswith("explainer_3") and explanation_file.endswith(".md"):
                explanation_path_full = os.path.join(explanation_path, explanation_file)
                with open(explanation_path_full, "r") as f:
                    st.markdown(f.read())
                break

    with tab5:
        st.image(os.path.join(image_folder, "Box Plot PM10 Levels Across Major Cities.png"))
        for explanation_file in os.listdir(explanation_path):
            if explanation_file.startswith("explainer_4") and explanation_file.endswith(".md"):
                explanation_path_full = os.path.join(explanation_path, explanation_file)
                with open(explanation_path_full, "r") as f:
                    st.markdown(f.read())
                break

    with tab6:
        st.image(os.path.join(image_folder, "AQI Category Pie Chart1.png"))
        for explanation_file in os.listdir(explanation_path):
            if explanation_file.startswith("explainer_5") and explanation_file.endswith(".md"):
                explanation_path_full = os.path.join(explanation_path, explanation_file)
                with open(explanation_path_full, "r") as f:
                    st.markdown(f.read())
                break

    with tab7:
        st.image(os.path.join(image_folder, "AQI Category Pie Chart2.png"))
        for explanation_file in os.listdir(explanation_path):
            if explanation_file.startswith("explainer_6") and explanation_file.endswith(".md"):
                explanation_path_full = os.path.join(explanation_path, explanation_file)
                with open(explanation_path_full, "r") as f:
                    st.markdown(f.read())
                break
    
    with tab8:
        st.image(os.path.join(image_folder, "Scatter Plot NO₂ vs PM₁₀2.png"))
        for explanation_file in os.listdir(explanation_path):
            if explanation_file.startswith("explainer_7") and explanation_file.endswith(".md"):
                explanation_path_full = os.path.join(explanation_path, explanation_file)
                with open(explanation_path_full, "r") as f:
                    st.markdown(f.read())
                break

    with tab9:
        st.image(os.path.join(image_folder, "Box Plot EValuation.png"))
        for explanation_file in os.listdir(explanation_path):
            if explanation_file.startswith("explainer_8") and explanation_file.endswith(".md"):
                explanation_path_full = os.path.join(explanation_path, explanation_file)
                with open(explanation_path_full, "r") as f:
                    st.markdown(f.read())
                break



# ---------------------------
# Make Prediction
# ---------------------------
elif page == "Make Prediction":
    st.header("🤖 Predict AQI Category")
    st.write("Enter pollution levels below to predict the AQI category:")

    col1, col2, col3 = st.columns(3)
    with col1:
        pm25 = st.number_input("PM2.5", min_value=0.0, max_value=500.0, value=50.0)
        pm10 = st.number_input("PM10", min_value=0.0, max_value=500.0, value=80.0)
    with col2:
        no2 = st.number_input("NO2", min_value=0.0, max_value=500.0, value=40.0)
        so2 = st.number_input("SO2", min_value=0.0, max_value=500.0, value=10.0)
    with col3:
        co = st.number_input("CO", min_value=0.0, max_value=50.0, value=1.0)
        o3 = st.number_input("O3", min_value=0.0, max_value=500.0, value=60.0)

    if st.button("🔮 Predict AQI"):
        model = joblib.load(r"model_pipeline.pkl")
        input_data = np.array([[pm25, pm10, no2, so2, co, o3]])
        Class_mapping = {'Good': 0, 
                         'Moderate': 1, 
                         'Unhealthy': 2, 
                         'Unhealthy-Sensitive': 3, 
                         'Very Unhealthy': 4
                         }

        prediction = model.predict(input_data)
        predicted_category = [key for key, value in Class_mapping.items() if value == prediction[0]][0]
        category_colors = {"Good": "#4CAF50",
                           "Moderate": "#FFC107",
                           "Unhealthy-Sensitive": "#FF9800", 
                           "Unhealthy": "#F44336",
                           "Very Unhealthy": "#6A1B9A"}
        color = category_colors.get(predicted_category, "gray")
        st.markdown(f"""
                    <div style="text-align:center; padding:20px; border-radius:10px; 
                    background-color:{color}; color:white; font-size:24px; 
                    font-weight:bold;">
                    🌍 Predicted AQI Category: {predicted_category}
                    </div>
                    """, unsafe_allow_html=True)

        st.toast("Prediction completed successfully!", icon="🎉")
        
        
