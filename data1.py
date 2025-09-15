import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_csv(df):
    st.write('Data Preview')
    st.dataframe(df.head())
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_columns) == 0:
        st.info('No numeric columns available for plotting.')
        return
    chart_type = st.selectbox('Select chart type', ['Line', 'Scatter', 'Bar', 'Histogram', 'Box'])
    if chart_type in ['Line', 'Scatter']:
        x_col = st.selectbox('X Axis', numeric_columns)
        y_col = st.selectbox('Y Axis', numeric_columns)
        fig, ax = plt.subplots()
        if chart_type == 'Line':
            sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
        else:
            sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        st.pyplot(fig)
    elif chart_type == 'Bar':
        x_col = st.selectbox('Category/Index', df.columns)
        y_col = st.selectbox('Values', numeric_columns)
        fig, ax = plt.subplots()
        sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
        st.pyplot(fig)
    elif chart_type == 'Histogram':
        col = st.selectbox('Select column', numeric_columns)
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), ax=ax)
        st.pyplot(fig)
    elif chart_type == 'Box':
        y_col = st.selectbox('Values', numeric_columns)
        fig, ax = plt.subplots()
        sns.boxplot(data=df, y=y_col, ax=ax)
        st.pyplot(fig)

def visualize_audio(uploaded_file):
    st.audio(uploaded_file)

def app():
    st.title('📊DATA VISUALIZATION')
    file_types = ['csv', 'xlsx', 'xls', 'mp3', 'wav']  # Removed 'png', 'jpg', 'jpeg', 'pdf'
    uploaded_file = st.file_uploader("Upload your file", type=file_types)
    if uploaded_file is not None:
        file_name = uploaded_file.name.lower()
        if file_name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            visualize_csv(df)
        elif file_name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
            visualize_csv(df)
        elif file_name.endswith(('.mp3', '.wav')):
            visualize_audio(uploaded_file)
        else:
            st.warning('Unsupported file type.')
            
if __name__ == "__main__":
    app()
