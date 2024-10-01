import streamlit as st
import pandas as pd


df = pd.read_csv('full_data.csv')


dataset_description = """
This dataset contains order details from a fictitious company that sells different products. 
Each order includes customer and product details, shipping information, and employee details.
"""

column_descriptions = {
    'OrderID': 'Unique identifier for each order.',
    'CustomerID': 'Unique identifier for each customer.',
    'EmployeeID': 'Unique identifier for each employee who processed the order.',
    'OrderDate': 'Date when the order was placed.',
    'RequiredDate': 'Date when the customer requires the order to be delivered.',
    'ShippedDate': 'Date when the order was shipped.',
    'Freight': 'Cost of shipping the order.',
    'ShipAddress': 'Address where the order is to be shipped.',
    'ShipCity': 'City where the order is to be shipped.',
    'ShipCountry': 'Country where the order is to be shipped.',
    'ProductID': 'Unique identifier for each product.',
    'UnitPrice_x': 'Price per unit of the product at the time of the order.',
    'Quantity': 'Number of units ordered.',
    'Discount': 'Discount applied to the order.',
    'ProductName': 'Name of the product ordered.',
    'SupplierID': 'Unique identifier for the supplier of the product.',
    'CategoryID': 'Unique identifier for the product category.',
    'QuantityPerUnit': 'Quantity of the product per unit sold.',
    'UnitPrice_y': 'Current price per unit of the product.',
    'UnitsInStock': 'Number of units available in stock.',
    'UnitsOnOrder': 'Number of units currently on order.',
    'ReorderLevel': 'Minimum number of units in stock before a new order should be placed.',
    'Discontinued': 'Indicates whether the product is discontinued (1) or not (0).',
    'CategoryName': 'Name of the product category.',
    'Description': 'Description of the product.',
    'CompanyName_x': 'Name of the company that sold the product.',
    'ContactName_x': 'Contact person at the selling company.',
    'ContactTitle_x': 'Job title of the contact person.',
    'Address_x': 'Address of the selling company.',
    'City_x': 'City where the selling company is located.',
    'Region': 'Region where the selling company is located.',
    'PostalCode_x': 'Postal code of the selling company.',
    'Country_x': 'Country of the selling company.',
    'Phone': 'Phone number of the selling company.',
    'Fax': 'Fax number of the selling company.',
    'CompanyName_y': 'Name of the company that supplied the product.',
    'ContactName_y': 'Contact person at the supplying company.',
    'ContactTitle_y': 'Job title of the contact person.',
    'Address_y': 'Address of the supplying company.',
    'City_y': 'City where the supplying company is located.',
    'Country_y': 'Country of the supplying company.',
    'LastName': 'Last name of the employee processing the order.',
    'FirstName': 'First name of the employee processing the order.',
    'Title': 'Job title of the employee.',
    'TitleOfCourtesy': 'Courtesy title of the employee.',
    'BirthDate': 'Birth date of the employee.',
    'HireDate': 'Hire date of the employee.',
    'Address': 'Address of the employee.',
    'City': 'City where the employee is located.',
    'PostalCode_y': 'Postal code of the employee.',
    'Country': 'Country where the employee is located.',
    'HomePhone': 'Home phone number of the employee.',
    'Extension': 'Extension number of the employee.',
    'Notes': 'Notes about the employee.',
    'ReportsTo': 'ID of the employee to whom this employee reports.',
    'Full Name': 'Full name of the employee.',
}


st.markdown("<h1 style= 'text-align : Center ; 'color: #4CAF50;'>Sales Analysis Project</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #4CAF50;'>Dataset Description</h3>", unsafe_allow_html=True)
st.write(dataset_description)

st.markdown("<h3 style='color: #4CAF50;'>Column Descriptions</h3>", unsafe_allow_html=True)

# Create a table for column descriptions
for column, description in column_descriptions.items():
    st.markdown(f"**{column}:** {description}")

# Button to show sample data
if st.button('Show Sample Data'):
    # Display a sample from the dataset
    st.markdown("<h3 style='color: #4CAF50;'>Sample Data</h3>", unsafe_allow_html=True)
    st.dataframe(df.sample(5))  # Change 5 to the number of samples you want to show

# Customize the page's appearance
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)
