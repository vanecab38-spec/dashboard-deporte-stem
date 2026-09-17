import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Dashboard Deportivo STEM", layout="wide")

st.title("🏃‍♂️ Dashboard Deportivo: Ambiente y Rendimiento")
st.caption("Proyecto Integrado: Biología, Físico-Química, Matemática y TIC")

# Menú lateral de navegación
opcion = st.sidebar.radio(
    "Seleccioná un Módulo:",
    [
        "1. Biología & Fisiología Ambiental",
        "2. Físico-Química (Calor y Temperatura)",
        "3. Matemática (Modelos Lineales)",
        "4. Registro de Datos de Campo"
    ]
)

# ==========================================
# MÓDULO 1: BIOLOGÍA Y FISIOLOGÍA AMBIENTAL
# ==========================================
if opcion == "1. Biología & Fisiología Ambiental":
    st.header("🧪 Módulo 1: Impacto del Ambiente en el Organismo")
    
    caso = st.selectbox(
        "Selecciona una situación de análisis:",
        ["Calor Extremo (Tenis)", "Altitud e Hipoxia (Fútbol)", "Contaminación e ICA (Ciclismo urbano)"]
    )
    
    if caso == "Calor Extremo (Tenis)":
        st.subheader("Situation A: El infierno en la cancha dura")
        temp = st.slider("Temperatura Ambiente (°C)", 20, 50, 41)
        st.write(f"**Sensación Térmica Estimada:** {temp + 7}°C")
        
        if temp >= 40:
            st.error("🚨 **Riesgo Severo:** Golpe de calor, deshidratación rápida y calambres severos.")
            st.info("💡 **Mecanismo Fisiológico:** El hipotálamo activa sudoración profusa. Pérdida masiva de agua y electrolitos.")
        else:
            st.success("Zona de esfuerzo tolerable con hidratación constante.")

    elif caso == "Altitud e Hipoxia (Fútbol)":
        st.subheader("Situation B: La Paz (3.600 msnm)")
        altitud = st.slider("Altitud (msnm)", 0, 5000, 3600)
        
        st.metric("Presión Atmosférica Relativa", f"{round(100 - (altitud/5000)*40)}%")
        if altitud > 2500:
            st.warning("⚠️ **Efecto de Hipoxia:** Menos densidad de aire. El corazón acelera el ritmo para compensar oxígeno.")
        else:
            st.success("Condiciones normóxicas habituales.")

    elif caso == "Contaminación e ICA (Ciclismo urbano)":
        st.subheader("Situation C: Calidad del Aire (ICA)")
        ica = st.slider("Índice de Calidad del Aire (ICA)", 0, 300, 120)
        
        if ica <= 50:
            st.success("Calidad del Aire: Buena (Verde)")
        elif ica <= 100:
            st.info("Calidad del Aire: Moderada (Amarillo)")
        elif ica <= 150:
            st.warning("Dañina para grupos sensibles (Naranja)")
        else:
            st.error("Dañina / Muy Peligrosa (Rojo/Púrpura): Irritación alveolar y fatiga prematura.")

# ==========================================
# MÓDULO 2: FÍSICO-QUÍMICA
# ==========================================
elif opcion == "2. Físico-Química (Calor y Temperatura)":
    st.header("🔥 Módulo 2: Intercambio Térmico y Conversiones")
    
    col1, col2 = st.col1_2() if hasattr(st, 'col1_2') else st.columns(2)
    
    with col1:
        st.subheader("Conversión de Escalas")
        temp_c = st.number_input("Temperatura en Celsius (°C)", value=25.0)
        temp_k = temp_c + 273.15
        temp_f = (temp_c * 9/5) + 32
        
        st.write(f"**Kelvin (Escala Absoluta):** {temp_k:.2f} K")
        st.write(f"**Fahrenheit:** {temp_f:.1f} °F")

    with col2:
        st.subheader("Cálculo de Calor Absorbido / Cedido")
        st.caption("Fórmula: $Q = m \\cdot c \\cdot \\Delta T$")
        
        masa = st.number_input("Masa de agua (kg)", value=1.0)
        delta_t = st.number_input("Variación de Temperatura ΔT (°C)", value=5.0)
        c_agua = 4184  # J/(kg·°C)
        
        q = masa * c_agua * delta_t
        st.metric("Calor Transferido (Q)", f"{q/1000:.2f} kJ")

# ==========================================
# MÓDULO 3: MATEMÁTICA (MODELOS LINEALES)
# ==========================================
elif opcion == "3. Matemática (Modelos Lineales)":
    st.header("📈 Módulo 3: Modelización del Rendimiento Deportivo")
    st.write("Analizá la función lineal $y = mx + b$ que relaciona variables ambientales y tiempo.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        m = st.slider("Pendiente (m)", -10.0, 10.0, 2.0, step=0.5)
        b = st.slider("Ordenada al origen (b)", -50, 100, 20)
        
        st.markdown(f"**Ecuación actual:** $y = {m}x + {b}$")
        
        if m != 0:
            raiz = -b / m
            st.write(f"**Raíz (Cero de la función):** $x = {raiz:.2f}$")
        else:
            st.write("**Raíz:** No tiene (recta horizontal)")
            
    with col2:
        x_vals = np.linspace(0, 35, 100)
        y_vals = m * x_vals + b
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f'y = {m}x + {b}', color='blue')
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
        ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.set_xlabel("Temperatura del agua (°C)")
        ax.set_ylabel("Tiempo de la nadadora (s)")
        ax.legend()
        st.pyplot(fig)

# ==========================================
# MÓDULO 4: REGISTRO DE DATOS DE CAMPO
# ==========================================
elif opcion == "4. Registro de Datos de Campo":
    st.header("📋 Módulo 4: Carga de Métricas Personales (TIC)")
    
    st.subheader("Ingreso de Frecuencia Cardíaca")
    atleta = st.text_input("Nombre del Atleta / Estudiante:", "Atleta 1")
    
    col1, col2 = st.columns(2)
    with col1:
        fc_reposo = st.number_input("Pulsaciones en Reposo (15 seg x 4)", value=70)
    with col2:
        fc_esfuerzo = st.number_input("Pulsaciones Post-Esfuerzo", value=140)
        
    variacion = fc_esfuerzo - fc_reposo
    st.metric("Variación del Pulso (ΔFC)", f"{variacion} ppm")
    
    # Simulación de exportación de datos
    st.subheader("Resumen de Registro")
    st.json({
        "Atleta": atleta,
        "FC Reposo": fc_reposo,
        "FC Esfuerzo": fc_esfuerzo,
        "Diferencia": variacion
    })
    st.success("Datos listos para sincronizar con la planilla de cálculo.")
