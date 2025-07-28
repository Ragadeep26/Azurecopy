import math
import pandas as pd
import common
from PIL import Image

img = Image.open('./common/spez_volume_power_chart.png')
def main_energy_calculator(st):
    # ---------------------------
    # ---------------------------
    # Title and description
    # ---------------------------
    st.title("Jet Grouting Energy Calculator")
    st.markdown("""
    This tool calculates the energy and volume parameters for jet grouting columns based on input design parameters. 
    It is adapted from the Bauer Energy Calculator.
    """)

    # ---------------------------
    # User Inputs
    # ---------------------------
    st.header("Input Parameters")

    col1, col2 = st.columns(2)

    with col1:
        diameter_col = st.number_input("Diameter of the column [m]", value=1.0, format="%f")
        nozzle_factor = st.number_input("Nozzle Factor", value=1.5, format="%f")
        nozzle_d1 = st.number_input("Diameter of Nozzle 1 [mm]", value=200.0, format="%f")
        nozzle_d2 = st.number_input("Diameter of Nozzle 2 [mm]", value=200.0, format="%f")
        high_pressure = st.number_input("High Pressure [bar]", value=60.0, format="%f")
        withdrawl_rate = st.number_input("Withdrawal rate [min/m]", value=50.0, format="%f")
        wc_ratio = st.number_input("Water-Cement Ratio", value=5.0, format="%f")
        aufful = st.number_input("Auffüllhöhe [cm]", value=50.0, format="%f")

    with col2:
        water_density = st.number_input("Water Density [t/m³]", value=1.0, format="%f")
        cement_density = st.number_input("Cement Density [t/m³]", value=3.1, format="%f")
        chalk_density = st.number_input("Chalk Density [t/m³]", value=2.65, format="%f")
        bentonite_density = st.number_input("Bentonite Density [t/m³]", value=2.6, format="%f")
        cement_pct = st.number_input("Cement Weight %", value=65.0, format="%f")
        chalk_pct = st.number_input("Chalk Weight %", value=25.0, format="%f")
        bentonite_pct = st.number_input("Bentonite Weight %", value=10.0, format="%f")

    # ---------------------------
    # Validation
    # ---------------------------
    total_pct = cement_pct + chalk_pct + bentonite_pct
    if total_pct != 100:
        st.error("Weight percentages must sum to 100%")
        st.stop()

    # ---------------------------
    # Calculation Logic
    # ---------------------------
    g_water = wc_ratio
    g_cement = cement_pct / 100
    g_chalk = chalk_pct / 100
    g_bentonite = bentonite_pct / 100

    v_water = g_water / water_density
    v_cement = g_cement / cement_density
    v_chalk = g_chalk / chalk_density
    v_bentonite = g_bentonite / bentonite_density
    v_total = v_water + v_cement + v_chalk + v_bentonite

    s_water = g_water / v_total
    s_cement = g_cement / v_total
    s_chalk = g_chalk / v_total
    s_bentonite = g_bentonite / v_total
    s_total = s_water + s_cement + s_chalk + s_bentonite

    jetting_volume = math.pi * (nozzle_d1**2 + nozzle_d2**2) * 0.25 * 1e-6 * math.sqrt(high_pressure * 100 * 2 / s_total) * 1000 * 60 * nozzle_factor
    jetting_power = (
        nozzle_factor**3 * math.sqrt(2 * 100 * high_pressure / s_total) * math.pi / 4 * 100 * high_pressure * 
        ((nozzle_d1/1000)**2 + (nozzle_d2/1000)**2)
    )
    jetting_power_per_m = jetting_power * (withdrawl_rate / 60)
    spez_volume_power = jetting_power_per_m / (math.pi/4 * diameter_col**2)
    sv_value = jetting_volume * withdrawl_rate
    wb_value = math.pi * (diameter_col/2)**2 * (aufful / withdrawl_rate) * 10
    mit_value = wb_value * 1.2 * withdrawl_rate / 1000
    sixty_one_value = sv_value * s_cement / 1000

    # ---------------------------
    # Output Section
    # ---------------------------
    col3,col4 = st.columns(2)
    with col3:
        st.header("Results")
    
        results = {
            "Jetting Volume [l/min]": round(jetting_volume),
            "Jetting Power [kW]": round(jetting_power),
            "Jetting Power per meter [kWh/m]": round(jetting_power_per_m),
            "SV/JGV [l/mHDI]": round(sv_value),
            "WB-Auffüllrate [l/min]": round(wb_value),
            "mit W/Z ~0.5 [t/mHDI]": round(mit_value),
            "Spez. Volume Power [kWh/m³]": round(spez_volume_power),
            "~t/mHDI (Cement only)": round(sixty_one_value)
        }
    
        st.dataframe(pd.DataFrame(results.items(), columns=["Parameter", "Value"]))
    with col4:
        # ---------------------------
        # Load image (chart reference)
        st.image(img, caption="Spez. Volume Power Reference Chart")
