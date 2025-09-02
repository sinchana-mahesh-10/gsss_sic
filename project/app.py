import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Patient Admissions Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply some styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<h1 class="main-header">🏥 Patient Admissions Dashboard</h1>', unsafe_allow_html=True)
st.write("Explore patient admission data, analyze trends, and view key metrics.")

# Load and process data
@st.cache_data
def load_data():
    # Load the dataset
    df = pd.read_csv('patient_admissions.csv')
    
    # Handle missing values
    df['Diagnosis'] = df['Diagnosis'].fillna('Unknown')
    
    today = pd.to_datetime('today').normalize()
    df['DischargeDate'] = df['DischargeDate'].fillna(today)
    
    # Convert date columns
    df['AdmissionDate'] = pd.to_datetime(df['AdmissionDate'])
    df['DischargeDate'] = pd.to_datetime(df['DischargeDate'])
    
    # Create derived column
    df['StayDuration'] = (df['DischargeDate'] - df['AdmissionDate']).dt.days
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['PatientID', 'AdmissionDate'])
    
    return df

# Load the data
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
department_filter = st.sidebar.multiselect(
    "Select Department(s):",
    options=df['Department'].unique(),
    default=df['Department'].unique()
)

stay_duration_filter = st.sidebar.slider(
    "Select Stay Duration Range (days):",
    min_value=int(df['StayDuration'].min()),
    max_value=int(df['StayDuration'].max()),
    value=(int(df['StayDuration'].min()), int(df['StayDuration'].max()))
)

# Apply filters
filtered_df = df[
    (df['Department'].isin(department_filter)) & 
    (df['StayDuration'] >= stay_duration_filter[0]) & 
    (df['StayDuration'] <= stay_duration_filter[1])
]

# Main content
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Total Patients", len(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Average Stay (days)", round(filtered_df['StayDuration'].mean(), 1))
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Departments", len(filtered_df['Department'].unique()))
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    ongoing = filtered_df[filtered_df['DischargeDate'] == pd.to_datetime('today').normalize()]
    st.metric("Ongoing Admissions", len(ongoing))
    st.markdown('</div>', unsafe_allow_html=True)

# Tabs for different views
tab1, tab2, tab3, tab4 = st.tabs(["Data Overview", "Department Analysis", "Trends Over Time", "Patient Details"])

with tab1:
    st.subheader("Patient Admissions Data")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Export button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_patient_data.csv",
        mime="text/csv"
    )

with tab2:
    st.subheader("Department-wise Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Admissions by department
        dept_counts = filtered_df['Department'].value_counts()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.pie(dept_counts.values, labels=dept_counts.index, autopct='%1.1f%%')
        ax.set_title('Admissions by Department')
        st.pyplot(fig)
    
    with col2:
        # Average stay by department
        avg_stay = filtered_df.groupby('Department')['StayDuration'].mean().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(avg_stay.index, avg_stay.values)
        ax.set_title('Average Stay Duration by Department')
        ax.set_ylabel('Days')
        plt.xticks(rotation=45)
        st.pyplot(fig)

with tab3:
    st.subheader("Admission Trends")
    
    # Admissions over time
    daily_admissions = filtered_df.set_index('AdmissionDate').resample('D').size()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(daily_admissions.index, daily_admissions.values)
    ax.set_title('Daily Admissions Over Time')
    ax.set_ylabel('Number of Admissions')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with tab4:
    st.subheader("Patient Details")
    
    # Search for specific patient
    patient_search = st.text_input("Search by Patient Name or ID:")
    
    if patient_search:
        patient_data = filtered_df[
            filtered_df['Name'].str.contains(patient_search, case=False) | 
            filtered_df['PatientID'].str.contains(patient_search, case=False)
        ]
        st.dataframe(patient_data, use_container_width=True)
    else:
        st.info("Enter a patient name or ID to search for specific records.")

# Show raw data option
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(df)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Patient Admissions Dashboard v1.0")