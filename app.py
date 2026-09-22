import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Education Analytics Dashboard",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 Education Analytics Dashboard")
st.write("Education Analytics and Predictive Modeling Project")

st.markdown("---")

# Project KPIs
st.header("📊 Project Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", "3,000")

with col2:
    st.metric("Total Courses", "60")

with col3:
    st.metric("Total Transactions", "10,000")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("Total Revenue", "₹911,323.47")

with col5:
    st.metric("Average Course Rating", "3.10")

with col6:
    st.metric("Average Student Spend", "₹303.77")

st.markdown("---")

# Most recommended courses
st.header("🎯 Most Recommended Courses")

course_data = pd.DataFrame({
    "Course Name": [
        "Digital Marketing",
        "Machine Learning Fundamentals",
        "Content Marketing",
        "Affiliate Marketing",
        "Advanced Python",
        "Data Encryption",
        "Full Stack Development",
        "Deep Learning",
        "Finance for Startups",
        "Data Analysis with Python"
    ],
    "Recommendations": [
        682, 566, 479, 418, 399,
        370, 365, 362, 358, 351
    ]
})

st.dataframe(course_data, use_container_width=True)

# Chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    course_data["Course Name"][::-1],
    course_data["Recommendations"][::-1]
)

ax.set_xlabel("Number of Recommendations")
ax.set_ylabel("Course Name")
ax.set_title("Top 10 Most Recommended Courses")

st.pyplot(fig)

st.markdown("---")

# Student Segmentation
st.header("👥 Student Segmentation")

st.write(
    "Student segmentation was performed using the K-Means clustering "
    "algorithm based on student-related analytical features."
)

col1, col2 = st.columns(2)

with col1:
    st.metric("Optimal Number of Clusters", "2")

with col2:
    st.metric("Silhouette Score", "0.73")

st.write(
    "The K-Means model was trained using the optimal cluster value "
    "identified through silhouette score analysis."
)

st.markdown("---")

# Project conclusion
st.header("📌 Key Findings")

st.write("""
- The dataset contains 3,000 students, 60 courses and 10,000 transactions.
- The total recorded revenue is ₹911,323.47.
- The average course rating is 3.10.
- Student segmentation was performed using K-Means clustering.
- The optimal number of clusters identified was 2.
- Course recommendation analysis was used to identify frequently recommended courses.
""")

st.markdown("---")

st.caption("Education Analytics Project | Unified Mentor Internship")
