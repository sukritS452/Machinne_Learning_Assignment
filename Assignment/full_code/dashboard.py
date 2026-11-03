# Interactive Agro-Climatic and Crop Yield Machine Learning Dashboard
# Student: Sukriti Sapkota | ID: 260180 | Module: STW7072CEM Machine Learning
# Softwarica College of IT and E-Commerce / Coventry University

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

st.set_page_config(
    page_title="Agro-Climatic ML Analytics Dashboard",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header { font-size: 2.3rem; font-weight: 800; color: #1E3A8A; margin-bottom: 0px; }
    .sub-header { font-size: 1.05rem; color: #64748B; margin-bottom: 25px; }
    .metric-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 20px;
        border-left: 5px solid #2563EB;
        box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    }
    .metric-title { font-size: 0.85rem; color: #64748B; text-transform: uppercase; font-weight: 700; }
    .metric-value { font-size: 1.8rem; font-weight: 800; color: #1E293B; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🌾 Crop Yield & Agro-Climatic Dynamics Analysis Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Author: <b>Sukriti Sapkota</b> (ID: 260180) | MSc Data Science & Computational Intelligence | STW7072CEM</div>', unsafe_allow_html=True)

# Top KPI Metric Cards
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.markdown('<div class="metric-card"><div class="metric-title">Temporal Horizon</div><div class="metric-value">32 Years</div><span style="color:#059669;font-size:0.8rem;">1982 – 2013</span></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="metric-card"><div class="metric-title">Total Records</div><div class="metric-value">11,210</div><span style="color:#059669;font-size:0.8rem;">75 Districts / 5 Crops</span></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="metric-card"><div class="metric-title">Optimal Clusters</div><div class="metric-value">k = 3</div><span style="color:#2563EB;font-size:0.8rem;">Sil: 0.3298 | DB: 1.145</span></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="metric-card"><div class="metric-title">Top Classifier</div><div class="metric-value">Random Forest</div><span style="color:#059669;font-size:0.8rem;">Acc: 63.63% | AUC: 0.817</span></div>', unsafe_allow_html=True)
with c5:
    st.markdown('<div class="metric-card"><div class="metric-title">Linear Baseline</div><div class="metric-value">R² = 0.384</div><span style="color:#D97706;font-size:0.8rem;">RMSE: 624 kg/ha</span></div>', unsafe_allow_html=True)

st.write("")

# Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Exploratory Data Analysis",
    "🌀 Unsupervised Clustering & PCA",
    "🎯 Supervised Classification",
    "📈 Linear Regression & Baseline",
    "⚡ Time & Space Complexity Benchmark"
])

# Tab 1: EDA
with tab1:
    st.subheader("Data Overview & Agro-Meteorological Distributions")
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.info("**Dataset Properties:** Sourced from multi-district meteorological observations across 32 years. Includes 14 engineered climate and agronomic features.")
        st.write("Cleaned records breakdown: Paddy (2,256), Maize (2,284), Wheat (2,240), Millet (2,228), Barley (2,202).")
    with col_b:
        st.success("**Feature Engineering Highlights:** Thermal Range (Tmax - Tmin), De Martonne Aridity Index, and Moisture Stress interaction.")

# Tab 2: Clustering
with tab2:
    st.subheader("K-Means Clustering Diagnostics & PCA Projection")
    c_left, c_right = st.columns([1, 1])
    with c_left:
        st.write("### Optimal Cluster Selection (k=3)")
        st.write("Evaluated across k=2 to k=6 using Within-Cluster Sum of Squares, Silhouette Width, and Davies-Bouldin Index.")
    with c_right:
        st.write("### 3 Distinct Agro-Climatic Zones")
        st.write("Cluster 0: Lowland Sub-Tropical (Warm, High Yield)\nCluster 1: Mid-Hills Temperate (Moderate, Medium Yield)\nCluster 2: Highland Alpine (Cold, Low Yield)")

# Tab 3: Classification
with tab3:
    st.subheader("Multi-Class Supervised Classification Benchmark")
    st.write("Predicting Yield Productivity Tiers: Low (<1150 kg/ha), Medium (1150-1800 kg/ha), High (>1800 kg/ha).")
    st.dataframe(pd.DataFrame({
        'Model': ['Random Forest', 'Decision Tree', 'Logistic Regression', 'Support Vector Machine'],
        'Accuracy (%)': [63.63, 61.13, 56.67, 53.90],
        'Macro F1 (%)': [63.62, 60.83, 54.21, 44.82],
        'Weighted F1 (%)': [63.67, 60.88, 54.55, 45.96],
        'AUC-ROC': [0.8168, 0.7932, 0.7288, 0.7556]
    }))

# Tab 4: Regression
with tab4:
    st.subheader("Multiple Linear Regression Modeling (OLS/Ridge)")
    st.write("Linear parametric baseline modeling continuous Yield (kg/ha) against 14 meteorological and physical covariates.")
    st.write("R²: 0.3842 | MAE: 489.15 kg/ha | RMSE: 624.38 kg/ha")

# Tab 5: Complexity
with tab5:
    st.subheader("Computational Complexity & Memory Profiling")
    st.dataframe(pd.DataFrame({
        'Model': ['Random Forest', 'Support Vector Machine', 'Decision Tree', 'Logistic Regression', 'Linear Regression'],
        'Theoretical Training Time': ['O(B · M · N log N)', 'O(C_cls · E · N · M)', 'O(M · N log N)', 'O(E · N · M · C_cls)', 'O(M² · N + M³)'],
        'Theoretical Inference Time': ['O(B · D)', 'O(C_cls · M)', 'O(D)', 'O(M · C_cls)', 'O(M)'],
        'Theoretical Space Complexity': ['O(B · 2^D · M)', 'O(C_cls · M)', 'O(2^D · M)', 'O(M · C_cls)', 'O(M)'],
        'Empirical Training Time (s)': [18.42, 3.12, 0.65, 0.48, 0.02],
        'Inference Latency (ms/sample)': [0.082, 0.003, 0.002, 0.002, 0.001],
        'Model Size (KB)': [5068.09, 0.66, 44.09, 0.67, 0.40]
    }))
