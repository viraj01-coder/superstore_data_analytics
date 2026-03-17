import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(
    page_title="Superstore Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

# --- Data Load ---
@st.cache_data
def load_data():
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Profit Margin %'] = round((df['Profit'] / df['Sales']) * 100, 2)
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.title("🔎 Filters")

years = sorted(df['Year'].unique())
selected_years = st.sidebar.multiselect(
    "Year", years, default=years
)

regions = sorted(df['Region'].unique())
selected_regions = st.sidebar.multiselect(
    "Region", regions, default=regions
)

categories = sorted(df['Category'].unique())
selected_cats = st.sidebar.multiselect(
    "Category", categories, default=categories
)

# --- Filter Apply ---
df_filtered = df[
    (df['Year'].isin(selected_years)) &
    (df['Region'].isin(selected_regions)) &
    (df['Category'].isin(selected_cats))
]

# --- Title ---
st.title("🛒 Superstore Sales Dashboard")
st.markdown("**US Retail Store | 2014–2017 | Source: Tableau Sample Data**")
st.divider()

# --- KPI Cards ---
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Sales",
    f"${df_filtered['Sales'].sum():,.0f}")
col2.metric("Total Profit",
    f"${df_filtered['Profit'].sum():,.0f}")
col3.metric("Total Orders",
    f"{df_filtered['Order ID'].nunique():,}")
col4.metric("Total Customers",
    f"{df_filtered['Customer ID'].nunique():,}")
col5.metric("Avg Profit Margin",
    f"{df_filtered['Profit Margin %'].mean():.1f}%")

st.divider()

# --- Row 1: Yearly Trend + Region Pie ---
col1, col2 = st.columns([1.6, 1])

with col1:
    yearly = df_filtered.groupby('Year')['Sales']\
             .sum().reset_index()
    fig1 = px.line(yearly, x='Year', y='Sales',
                   title='Yearly Sales Trend',
                   markers=True,
                   color_discrete_sequence=['#1f77b4'])
    fig1.update_layout(height=320)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    region_df = df_filtered.groupby('Region')['Sales']\
                .sum().reset_index()
    fig2 = px.pie(region_df, names='Region', values='Sales',
                  title='Sales by Region',
                  hole=0.4)
    fig2.update_layout(height=320)
    st.plotly_chart(fig2, use_container_width=True)

# --- Row 2: Category Bar + Sub-Category Profit ---
col1, col2 = st.columns(2)

with col1:
    cat_df = df_filtered.groupby('Category').agg(
        Sales=('Sales','sum'),
        Profit=('Profit','sum')
    ).reset_index()
    fig3 = px.bar(cat_df, x='Category',
                  y=['Sales','Profit'],
                  barmode='group',
                  title='Sales vs Profit by Category')
    fig3.update_layout(height=350)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    sub_df = df_filtered.groupby('Sub-Category')['Profit']\
             .sum().reset_index()\
             .sort_values('Profit')
    fig4 = px.bar(sub_df, x='Profit', y='Sub-Category',
                  orientation='h',
                  color='Profit',
                  color_continuous_scale='RdYlGn',
                  title='Profit by Sub-Category')
    fig4.update_layout(height=350)
    st.plotly_chart(fig4, use_container_width=True)

# --- Row 3: Discount vs Profit + Shipping ---
col1, col2 = st.columns(2)

with col1:
    fig5 = px.scatter(df_filtered, x='Discount', y='Profit',
                      color='Category',
                      title='Discount vs Profit Impact',
                      opacity=0.5)
    fig5.update_layout(height=320)
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    ship_df = df_filtered.groupby('Ship Mode')['Shipping Days']\
              .mean().reset_index().round(1)
    fig6 = px.bar(ship_df, x='Ship Mode', y='Shipping Days',
                  title='Avg Shipping Days by Mode',
                  color='Ship Mode')
    fig6.update_layout(height=320)
    st.plotly_chart(fig6, use_container_width=True)

# --- Row 4: Top 10 Products ---
st.subheader("🏆 Top 10 Products by Profit")
top10 = df_filtered.groupby('Product Name')['Profit']\
        .sum().nlargest(10).reset_index().round(2)
top10.columns = ['Product', 'Profit ($)']
st.dataframe(top10, use_container_width=True, hide_index=True)

# --- Row 5: Raw Data ---
st.divider()
with st.expander("📄 Raw Data Table"):
    st.dataframe(df_filtered, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.caption("Made with Streamlit | Data: Tableau Sample Superstore")