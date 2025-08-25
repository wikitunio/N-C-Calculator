import streamlit as st

# Title
st.title("N/C Ratio Calculator")

st.markdown("""
This app calculates the **N/C ratio** based on the given weight percentages of:
- Ammonia (NH₃)
- Carbon Dioxide (CO₂)
- Urea
""")

# User Inputs
nh3 = st.number_input("Enter weight% of NH₃", min_value=0.0, format="%.4f")
co2 = st.number_input("Enter weight% of CO₂", min_value=0.0, format="%.4f")
urea = st.number_input("Enter weight% of Urea", min_value=0.0, format="%.4f")

# Calculation
if st.button("Calculate N/C Ratio"):
    try:
        numerator = (2 * urea / 60) + (nh3 / 17)
        denominator = (urea / 60) + (co2 / 44)
        
        if denominator == 0:
            st.error("Denominator became zero. Please check your inputs.")
        else:
            nc_ratio = numerator / denominator
            st.success(f"N/C Ratio = {nc_ratio:.4f}")
    except Exception as e:
        st.error(f"Error: {e}")
