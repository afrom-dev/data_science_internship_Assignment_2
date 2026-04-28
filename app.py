import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# PAGE CONFIG
st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
.main { background-color: #f0f2f6; }
.kpi-card {
    background: white; border-radius: 12px; padding: 20px 24px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    border-left: 5px solid #1f77b4; margin-bottom: 16px;
}
.kpi-title { font-size: 13px; color: #888; font-weight: 600; }
.kpi-value { font-size: 28px; font-weight: 800; color: #1a1a2e; }
.section-header {
    font-size: 18px; font-weight: 700; color: #1a1a2e;
    margin: 24px 0 12px 0; padding-bottom: 6px;
    border-bottom: 2px solid #1f77b4;
}
</style>
""", unsafe_allow_html=True)


# LOAD AND PREPROCESS DATA

@st.cache_data
def load_data():
    for enc in ['latin-1', 'utf-8', 'cp1252']:
        try:
            df = pd.read_csv("superstore.csv", encoding=enc)
            break
        except:
            continue

    df.columns = df.columns.str.strip()

    df['Order.Date'] = pd.to_datetime(df['Order.Date'], dayfirst=True, errors='coerce')
    df.dropna(subset=['Order.Date'], inplace=True)

    for col in ['Sales', 'Profit', 'Quantity', 'Discount']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    df['Year'] = df['Order.Date'].dt.year
    df['Month'] = df['Order.Date'].dt.to_period('M').astype(str)

    return df

df = load_data()

# SIDEBAR
st.sidebar.title("🔍 Filters")

all_regions = sorted(df['Region'].dropna().unique())
selected_regions = st.sidebar.multiselect("Region", all_regions, all_regions)

all_categories = sorted(df['Category'].dropna().unique())
selected_categories = st.sidebar.multiselect("Category", all_categories, all_categories)

sub_df = df[df['Category'].isin(selected_categories)]
all_subcats = sorted(sub_df['Sub.Category'].dropna().unique())
selected_subcats = st.sidebar.multiselect("Sub-Category", all_subcats, all_subcats)

all_years = sorted(df['Year'].unique())
selected_years = st.sidebar.multiselect("Year", all_years, all_years)

# FILTER DATA
filtered = df[
    df['Region'].isin(selected_regions) &
    df['Category'].isin(selected_categories) &
    df['Sub.Category'].isin(selected_subcats) &
    df['Year'].isin(selected_years)
]

if filtered.empty:
    st.warning("No data found")
    st.stop()

# TITLE
st.title("🏪 Global Superstore Dashboard")

# KPI
total_sales = filtered['Sales'].sum()
total_profit = filtered['Profit'].sum()
total_orders = filtered['Order.ID'].nunique()
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
avg_discount = filtered['Discount'].mean() * 100

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Sales", f"${total_sales:,.0f}")
col2.metric("Profit", f"${total_profit:,.0f}")
col3.metric("Orders", f"{total_orders}")
col4.metric("Margin", f"{profit_margin:.1f}%")
col5.metric("Discount", f"{avg_discount:.1f}%")

# CHARTS
st.subheader("Sales Over Time")
monthly = filtered.groupby('Month')['Sales'].sum().reset_index()
st.plotly_chart(px.area(monthly, x='Month', y='Sales'))

st.subheader("Sales by Category")
cat = filtered.groupby('Category')['Sales'].sum().reset_index()
st.plotly_chart(px.pie(cat, names='Category', values='Sales'))

st.subheader("Region Performance")
region = filtered.groupby('Region')[['Sales','Profit']].sum().reset_index()
st.plotly_chart(px.bar(region, x='Region', y=['Sales','Profit'], barmode='group'))

st.subheader("Sub-Category Sales")
subcat = filtered.groupby('Sub.Category')['Sales'].sum().reset_index()
st.plotly_chart(px.bar(subcat, x='Sales', y='Sub.Category', orientation='h'))

st.subheader("Top Customers")
top_customers = filtered.groupby('Customer.Name')['Sales'].sum().reset_index().sort_values('Sales', ascending=False).head(5)
st.plotly_chart(px.bar(top_customers, x='Sales', y='Customer.Name', orientation='h'))

st.subheader("Shipping Mode")
ship = filtered.groupby('Ship.Mode')['Sales'].sum().reset_index()
st.plotly_chart(px.pie(ship, names='Ship.Mode', values='Sales'))

# RAW DATA
st.subheader("Raw Data")
st.dataframe(filtered[['Order.ID','Order.Date','Customer.Name','Segment',
                       'Region','Category','Sub.Category','Sales','Profit','Quantity','Discount']])

# DOWNLOAD
csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "filtered_data.csv", "text/csv")
