import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
st.set_page_config(layout="wide")

full_df = pd.read_csv('\\full_data.csv')
st.markdown(
    "<h1 style='text-align: center; color: green;'> Products Insights</h1>", unsafe_allow_html=True
)
st.image('https://blog.thecenterforsalesstrategy.com/hs-fs/hubfs/analytics.gif?width=400&name=analytics.gif',use_column_width=True)

col1, col2, col3 = st.columns([4,1,4])
with col1:
    st.markdown("<h3 style='text-align: center; color: Green ;'> What category has the least shortage? </h3>",unsafe_allow_html=True)
    category_shortage = full_df.groupby(['CategoryID','CategoryName'])['Category Shortage'].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(category_shortage, x='CategoryName', y='Category Shortage', labels={'Category Shortage':'Shortage'}, color='CategoryName',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig)

    st.markdown("<h3 style='text-align: center; color: Green ;'> What product  has the most shartage? </h3>",unsafe_allow_html=True)
    products_shortage_bottom = full_df.groupby('ProductName')['Category Shortage'].sum().sort_values(ascending=True).reset_index().head(10)
    fig = px.bar(products_shortage_bottom, x='ProductName', y='Category Shortage', labels={'Category Shortage':'Shortage'}, color='ProductName',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig)

    st.markdown("<h3 style='text-align: center; color: Green ;'> Most popular products around world </h3>",unsafe_allow_html=True)
    prod_viral = full_df.groupby('ProductName')['Country_x'].nunique().sort_values(ascending=False).reset_index().head(10)  
    fig = px.bar(prod_viral, x='ProductName', y='Country_x', labels={'Country_x':'Countries'}, color='ProductName',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig)
    

with col3:
    st.markdown("<h3 style='text-align: center; color: Green ;'> What product has the least shortage? </h3>",unsafe_allow_html=True)
    products_shortage_top = full_df.groupby('ProductName')['Category Shortage'].sum().sort_values(ascending=False).reset_index().head(10)
    fig = px.bar(products_shortage_top, x='ProductName', y='Category Shortage', labels={'Category Shortage':'Shortage'}, color='ProductName',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig)


    st.markdown("<h3 style='text-align: center; color: Green ;'> Which category is the most ordered? </h3>",unsafe_allow_html=True)
    catonorder = full_df.groupby(['CategoryID','CategoryName'])['UnitsOnOrder'].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(catonorder, x='CategoryName', y='UnitsOnOrder', labels={'UnitsOnOrder':'Units on Order'}, color='CategoryName',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig)
    
    st.markdown("<h3 style='text-align: center; color: Green ;'> Least popular products around world </h3>",unsafe_allow_html=True)
    prod_viral_bottom = full_df.groupby('ProductName')['Country_x'].nunique().sort_values(ascending=True).reset_index().head(10)
    fig = px.bar(prod_viral_bottom, x='ProductName', y='Country_x', labels={'Country_x':'Countries'}, color='ProductName',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig)
