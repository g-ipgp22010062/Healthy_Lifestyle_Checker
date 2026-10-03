import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Test Healthy Lifestyle Checker",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Healthy Lifestyle Checker")
st.subheader("System Test")

st.success("✅ Streamlit berjaya berjalan!")

# Test Pandas
data = {
    "Indicator": [
        "Water",
        "Sleep",
        "Physical Activity",
        "Fruit & Vegetables"
    ],
    "Value": [
        "2.0 L",
        "7 hours",
        "150 minutes",
        "5 servings"
    ]
}

df = pd.DataFrame(data)

st.write("### 📊 Test Pandas")
st.dataframe(df, use_container_width=True)

# Input test
st.write("### 👤 Test User Input")

name = st.text_input("Nama", "Aqil")
age = st.number_input("Umur", 10, 100, 22)
weight = st.number_input("Berat (kg)", 20.0, 300.0, 80.0)
height = st.number_input("Tinggi (cm)", 100.0, 250.0, 175.0)

if st.button("🚀 TEST ANALYSIS", type="primary"):

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Kurang berat badan"
    elif bmi < 25:
        category = "BMI normal"
    elif bmi < 30:
        category = "Berlebihan berat badan"
    else:
        category = "Obesiti"

    st.success("✅ Analysis berjaya!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("BMI", f"{bmi:.1f}")

    with col2:
        st.metric("Umur", age)

    st.info(f"""
    **Nama:** {name}

    **Kategori BMI:** {category}

    Sistem berjaya mengira BMI menggunakan Python.
    """)

st.divider()

st.caption("Healthy Lifestyle Checker — System Test")