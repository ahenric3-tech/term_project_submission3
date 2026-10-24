import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ------------------------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Synapse Workspace: AI Analytics Report",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------------------------------------
# 1. TITLE AND BRIEF INTRODUCTION
# ------------------------------------------------------------------------------
st.title("📊 Synapse Workspace: AI Product Strategy & Analytics Report")
st.caption("Executive Product Management Perspective | Enterprise AI Feature Analysis")

st.markdown("""
### Executive Introduction
**Synapse Workspace** is an enterprise collaboration platform that recently introduced a suite of AI-powered productivity features:
*Writing Assistance, Meeting Summaries, Intelligent Knowledge Search, Workflow Automation,* and *Task Recommendations*.

As enterprise adoption continues to grow, executive leadership requested an evidence-based analysis of **how customers engage with these AI capabilities**, **how complexity impacts user retention**, and **where product engineering should focus future sprint investments**.

This web report synthesizes 12 months of organizational usage logs, customer sentiment metrics, and feedback data to deliver actionable strategic insights and evidence-based recommendations for Product Management and Executive leadership.
""")

st.divider()

# ------------------------------------------------------------------------------
# DATASET PREVIEW
# ------------------------------------------------------------------------------
st.header("📂 Data Overview")
st.write("Below is a summary preview of the 12-month feature usage and performance metrics analyzed for this report:")

usage_data = pd.DataFrame({
    'FeatureName': ['Meeting Summary', 'Writing Assistant', 'Knowledge Search', 'Workflow Automation', 'Task Recommendation'],
    'ComplexityLevel': ['Low', 'Low', 'Medium', 'Medium', 'Medium'],
    'LaunchMonth': [1, 2, 3, 4, 5],
    'Mean_MAU': [73.55, 65.05, 59.90, 51.50, 50.48],
    'RetentionRate_Pct': [82.68, 82.10, 80.52, 80.38, 80.57],
    'AvgSessionMinutes': [8.79, 11.65, 8.32, 12.60, 6.95],
    'AvgRating': [4.01, 3.82, 3.83, 4.09, 4.08],
    'NetSentimentIndex': [0.492, 0.456, 0.476, 0.536, 0.523]
})

st.dataframe(usage_data, use_container_width=True)

st.divider()

# ------------------------------------------------------------------------------
# 2. VISUALIZATIONS & BRIEF EXPLANATIONS
# ------------------------------------------------------------------------------
st.header("📈 Visualizations & Explanations")

tab1, tab2, tab3 = st.tabs([
    "1. Adoption vs. Retention", 
    "2. Engagement vs. Satisfaction", 
    "3. Customer Friction Taxonomy"
])

# --- TAB 1: Adoption vs Retention ---
with tab1:
    st.subheader("Visualization 1: Adoption Scale vs. Retention Stability by Feature Complexity")
    
    categories = ['Low Complexity\n(Meeting Summary, Writing Asst.)', 'Medium Complexity\n(Search, Automation, Task Rec.)']
    mau_vals = [69.30, 53.96]
    ret_vals = [82.39, 80.49]

    fig1 = go.Figure()

    fig1.add_trace(go.Bar(
        x=categories,
        y=mau_vals,
        name='Mean Monthly Active Users (MAU)',
        marker_color='#2b5c8f',
        text=[f"{v:.2f} MAU" for v in mau_vals],
        textposition='auto'
    ))

    fig1.add_trace(go.Bar(
        x=categories,
        y=ret_vals,
        name='12-Month Retention Rate (%)',
        marker_color='#d95f02',
        text=[f"{v:.2f}%" for v in ret_vals],
        textposition='auto'
    ))

    fig1.update_layout(
        title='Monthly Active Users (MAU) vs. 12-Month Retention Rate by Complexity',
        barmode='group',
        xaxis_title='Feature Complexity Level',
        yaxis_title='Metric Value',
        legend=dict(x=0.01, y=0.99),
        template='plotly_white',
        height=450
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("""
    **Brief Explanation:**  
    This grouped bar chart compares active monthly usage (MAU) and 12-month user retention rates across feature complexity levels. It demonstrates that while low-complexity tools capture significantly higher top-of-funnel reach (**69.30 vs. 53.96 MAU**, $p < 0.0001$), medium-complexity tools maintain virtually identical long-term retention rates (**80.49% vs. 82.39%**, $p = 0.2254$).
    """)

# --- TAB 2: Engagement vs Satisfaction ---
with tab2:
    st.subheader("Visualization 2: Feature Engagement Depth vs. Satisfaction Index")

    fig2 = px.scatter(
        usage_data,
        x='AvgSessionMinutes',
        y='AvgRating',
        size=[1958, 1497, 1188, 1045, 690],
        color='ComplexityLevel',
        text='FeatureName',
        color_discrete_map={'Low': '#2b5c8f', 'Medium': '#d95f02'},
        labels={
            'AvgSessionMinutes': 'Average Session Duration (Minutes)',
            'AvgRating': 'Average Rating (1-5 Stars)',
            'ComplexityLevel': 'Complexity'
        },
        title='Session Duration vs. Customer Rating (Bubble Size = Usage Volume)'
    )

    fig2.update_traces(textposition='top center', marker=dict(sizeref=3))
    fig2.update_layout(
        yaxis_range=[3.70, 4.22],
        xaxis_range=[5.5, 14.0],
        template='plotly_white',
        height=480
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    **Brief Explanation:**  
    This scatter plot maps average session duration against customer satisfaction scores across all five AI capabilities. It reveals that **Workflow Automation** achieves peak satisfaction (**4.09 rating**) and the deepest session length (**12.60 minutes**), whereas high-volume tools like **Writing Assistant** suffer lower overall ratings (**3.82 rating**) despite high usage volume.
    """)

# --- TAB 3: Friction Taxonomy ---
with tab3:
    st.subheader("Visualization 3: Strategic Engineering Taxonomy of Customer Friction")

    friction_data = pd.DataFrame({
        'Feature': ['Meeting Summary', 'Knowledge Search', 'Writing Assistant', 'Workflow Automation', 'Task Recommendation'],
        'Category': ['Backend AI Model', 'Backend AI Model', 'UX/UI Controls', 'UX/UI Controls', 'UX/UI Controls'],
        'Issue': ['Accuracy (Nuance)', 'Relevance (Noise)', 'Formatting (Tone Control)', 'Integrations (Connectors)', 'Personalization (Role-Based)'],
        'Complaints': [62, 57, 61, 42, 37]
    }).sort_values(by='Complaints', ascending=True)

    fig3 = px.bar(
        friction_data,
        x='Complaints',
        y='Feature',
        color='Category',
        orientation='h',
        text='Issue',
        color_discrete_map={'Backend AI Model': '#2b5c8f', 'UX/UI Controls': '#d95f02'},
        title='Customer Complaints Categorized by Engineering Domain'
    )

    fig3.update_layout(
        xaxis_title='Total Negative Feedback Items (12-Month Period)',
        yaxis_title='AI Capability',
        template='plotly_white',
        height=420
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("""
    **Brief Explanation:**  
    This horizontal bar chart separates user complaints into two distinct operational categories: **Backend AI Model Fixes** (**119 total complaints**) versus **Frontend UX/UI Controls** (**140 total complaints**).
    """)

st.divider()

# ------------------------------------------------------------------------------
# 3. CLEAR INTERPRETATION OF FINDINGS
# ------------------------------------------------------------------------------
st.header("🔍 Clear Interpretation of Analytical Findings")

st.markdown("""
Our statistical and qualitative analysis yields three core interpretations:

1. **Retention Neutrality Across Feature Complexity:**
   - Statistical testing confirms that while low-complexity tools attract higher initial reach ($p < 0.0001$), the difference in 12-month retention rates between low-complexity tools (82.39%) and medium-complexity tools (80.49%) is **statistically insignificant** ($p = 0.2254$).
   - *Interpretation:* Technical complexity does **not** drive user churn. Users who adopt complex features stick with them at virtually the same rate as simple tools.

2. **Reach vs. Satisfaction Dynamics:**
   - High-volume tools like *Writing Assistant* suffer from formatting and tone control friction, driving down their average rating (3.82 rating).
   - Specialized tools like *Workflow Automation* generate lower overall volume but command the highest session depth (12.60 mins) and net sentiment (+0.536 NSI).
   - *Interpretation:* High-volume tools need user control options, whereas deep workflow integration creates maximum customer value.

3. **Engineering Friction Division:**
   - Categorizing negative customer feedback shows that **54.1%** of complaints (140 items) stem from **Frontend UX/UI Controls** (formatting, tone sliders, connectors), while **45.9%** (119 items) stem from **Backend AI Model Limitations** (accuracy, relevance, noise).
""")

st.divider()

# ------------------------------------------------------------------------------
# 4. KEY BUSINESS INSIGHTS
# ------------------------------------------------------------------------------
st.header("💡 Key Business Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Insight 1: Avoid Over-Simplification**  
    Simplifying complex features to prevent churn is an unnecessary strategy. Users accept technical complexity when features automate meaningful business tasks.
    """)

with col2:
    st.success("""
    **Insight 2: Flagship Enterprise Asset**  
    Workflow Automation achieves peak session duration (12.60 min) and customer sentiment (+0.536 NSI), making it the single best capability for driving enterprise retention.
    """)

with col3:
    st.warning("""
    **Insight 3: Interface Controls Matter Most**  
    More customer friction is caused by UI formatting and integration controls (140 complaints) than underlying AI model accuracy (119 complaints).
    """)

st.divider()

# ------------------------------------------------------------------------------
# 5. EVIDENCE-BASED RECOMMENDATIONS
# ------------------------------------------------------------------------------
st.header("🎯 Evidence-Based Recommendations")

st.markdown("""
Based on our findings, we recommend three strategic actions:

### 1. Implement a 50/50 Engineering Sprint Allocation
- **Backend Model Track (50% Capacity):** Focus engineering sprints on prompt tuning, context window expansion, and search relevance algorithms for *Meeting Summary* and *Knowledge Search*.
- **Frontend UI & Controls Track (50% Capacity):** Build custom tone sliders and template controls for *Writing Assistant* and expand API connectors for *Workflow Automation*.

### 2. Focus Onboarding Support on Months 1–2
- Because user retention stabilizes after Month 2 across all complexity levels, deploy targeted customer success templates and interactive onboarding during the first 60 days to build user habits.

### 3. Position Workflow Automation as the Primary Sales Asset
- Highlight *Workflow Automation* in enterprise marketing and sales demos. Its high session length and top satisfaction score make it our strongest driver of expansion revenue.
""")

st.divider()
st.caption("Report prepared by Product Management Consulting Team | AI in Business")
