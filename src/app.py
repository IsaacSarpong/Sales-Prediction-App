# import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sn


# # Add custom CSS style 
# def set_custom_style():
#     # Defined  path to the background image 
#     background_image_path = "assets/background_image.jpg"

#     #  CSS code with the background image and additional styles
#     custom_style = f"""
#     <style>
#     body {{
#         background-image: url("{background_image_path}");
#         background-size: cover;
#     }}
#     .radio-border {{
#         border: 2px solid #e74c3c;
#         border-radius: 5px;
#         padding: 5px;
#         margin: 5px;
#     }}
#     .horizontal-radio {{
#         display: flex;
#         flex-direction: row;
#         align-items: center;
#     }}
#     h1 {{
#         color: #e74c3c;
#     }}
#     .stSelectbox label,
#     .stRadio label {{
#         color: red;
#     }}
#     .category-header {{
#         font-size: 24px;
#         color: #e74c3c;
#         margin-top: 20px;
#         margin-bottom: 10px;
#     }}
#     </style>
#     """
#     st.markdown(custom_style, unsafe_allow_html=True)

# # Create a dictionary to store the column names and their values
# column_values = {
#     'selected_store_nbr': ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
#     'selected_family': ['HOME_APPLIANCES', 'BABY_CARE', 'BREAD_BAKERY', 'FROZEN_FOODS', 'GROCERY_I', 'GROCERY_II', 'HOME_AND_KITCHEN_I', 'HOME_AND_KITCHEN_II', 'HOME_CARE', 'LAWN AND GARDEN', 'LIQUOR_WINE_BEER', 'PERSONAL CARE', 'PET SUPPLIES', 'PLAYERS_AND_ELECTRONICS', 'PREPARED_FOODS', 'SCHOOL AND OFFICE SUPPLIES'],
#     'on_promotion': ['True', 'False'],
#     'holiday': ['Yes', 'No'],
# }





# num_data_points = 1000
# store_numbers = np.random.choice(column_values['selected_store_nbr'], size=num_data_points).astype(int)
# families = np.random.choice(column_values['selected_family'], size=num_data_points)
# on_promotion = np.random.choice(column_values['on_promotion'], size=num_data_points)
# holiday = np.random.choice(column_values['holiday'], size=num_data_points)
# average_transaction = np.random.uniform(0.0, 1000.0, num_data_points)
# oil_price = np.random.uniform(0.0, 150.0, num_data_points)
# sales = np.random.uniform(0.0, 10000.0, num_data_points)


# # Create a DataFrame with the generated data
# dates = pd.date_range(start='2023-01-01', periods=num_data_points, freq='D')
# data = pd.DataFrame({
#     'date': dates,
#     'selected_store_nbr': store_numbers,
#     'selected_family': families,
#     'on_promotion': on_promotion,
#     'holiday': holiday,
#     'average_transaction': average_transaction,
#     'oil_price': oil_price,
#     'sales': sales
# })

# # Define data types for columns with specific types
# column_data_types = {
#     'date': 'datetime64[ns]',
#     'selected_store_nbr': int,
#     'selected_family':object,
#     'on_promotion': bool,
#     'holiday': bool,
#     'average_transaction': float,
#     'oil_price': float,
#     'sales': float
# }
# # Convert columns to specified data types
# data = data.astype(column_data_types)





# # Streamlit app header
# st.title(' Time Series Sales Prediction')

# st.write("This app allows you to analyze time series data and make predictions with aid of  various visualizations.")

# # Call the function to set the custom style
# set_custom_style()

# # Date range selection
# st.markdown('<p class="category-header">Date Range Selection</p>', unsafe_allow_html=True)
# st.write("select start date and end date to continue")
# start_date = st.date_input("Start Date", value=None)
# end_date = st.date_input("End Date", value=None)

# # Filter by Store Number and Family
# st.markdown('<p class="category-header">Filter by Store Number and Family</p>', unsafe_allow_html=True)
# st.write("select family and store number of choice")

# selected_store_nbr = st.selectbox('Select Store Number:', np.unique(data['selected_store_nbr']))
# selected_family = st.selectbox('Select Family:', np.unique(data['selected_family']))


# st.markdown('<p class="category-header">Additional Filters</p>', unsafe_allow_html=True)
# # select boxes for the rest of the columns
# average_transaction = st.slider('Average Transaction', min_value=0.0, max_value=1000.0, value=(0.0, 1000.0), step=1.0)
# on_promotion = st.selectbox('On Promotion:', ['True', 'False'])
# holiday = st.selectbox('holiday:', ['Yes', 'No'])
# oil_price = st.slider('oil_price', min_value=0.0, max_value=150.0, value=(0.0, 150.0), step=5.0)

# # Visualizations
# st.markdown('<p class="category-header">Visualizations</p>', unsafe_allow_html=True)
# st.write("visualize your graph as per the features selected above")
# # Add options for visualizations
# visualization_options = ['Line Chart', 'Bar Chart', 'Scatter Plot', 'Histogram', 'Heatmap']
# selected_visualization = st.selectbox('Select Visualization:', visualization_options)

# # Function to visualize data as a line chart


# # Function to visualize data as a line chart
# @st.cache_resource(experimental_allow_widgets=True)
# def visualize_line_chart(data):
#     # code for visualization using matplotlib
#     fig, ax = plt.subplots()
#     ax.plot(data['date'], data['sales'])
#     plt.xlabel('Date')
#     plt.ylabel('Sales')
#     plt.title('Sales Time Series')
#     return fig

# # Function to visualize data as a bar chart
# @st.cache_resource(experimental_allow_widgets=True)
# def visualize_bar_chart(data):
#     # code for visualization using matplotlib
#     fig, ax = plt.subplots()
#     ax.bar(data['selected_family'], data['sales'])
#     plt.xlabel('Family')
#     plt.ylabel('Sales')
#     plt.title('Sales by Family')
#     plt.xticks(rotation=45)
#     return fig

# # Function to visualize data as a scatter plot
# @st.cache_resource(experimental_allow_widgets=True)
# def visualize_scatter_plot(data):
#     # code for visualization using matplotlib
#     fig, ax = plt.subplots()
#     ax.scatter(data['average_transaction'], data['sales'])
#     plt.xlabel('Average Transaction')
#     plt.ylabel('Sales')
#     plt.title('Sales vs. Average Transaction')
#     return fig

# # Function to visualize data as a histogram
# @st.cache_resource(experimental_allow_widgets=True)
# def visualize_histogram(data):
#     # code for visualization using matplotlib
#     fig, ax = plt.subplots()
#     ax.hist(data['sales'], bins=20)
#     plt.xlabel('Sales')
#     plt.ylabel('Frequency')
#     plt.title('Sales Distribution')
#     return fig

# # Function to visualize data as a heatmap
# @st.cache_resource(experimental_allow_widgets=True)
# def visualize_heatmap(data):
#     # code for visualization using seaborn
#     fig, ax = plt.subplots()
#     sn.heatmap(data.corr(), annot=True)
#     plt.title('Correlation Heatmap')
#     return fig


# # Return the chart to be displayed as per the users input
# if st.button("Visualize"):
#     if selected_visualization == 'Line Chart':
#         fig = visualize_line_chart(data)
#         st.pyplot(fig)
#     elif selected_visualization == 'Bar Chart':
#         fig = visualize_bar_chart(data)
#         st.pyplot(fig)
#     elif selected_visualization == 'Scatter Plot':
#         fig = visualize_scatter_plot(data)
#         st.pyplot(fig)
#     elif selected_visualization == 'Histogram':
#         fig = visualize_histogram(data)
#         st.pyplot(fig)
#     elif selected_visualization == 'Heatmap':
#         fig = visualize_heatmap(data)
#         st.pyplot(fig)


# # Add the button for predictions
# st.markdown('<p class="category-header">Make Predictions</p>', unsafe_allow_html=True)
# prediction_button = st.button("Predict")
# st.write("your prediction output here")



import streamlit as st
import pandas as pd
from datetime import datetime
import pickle
import xgboost as xgb
import os

# Function to load the XGBoost model and other components
def load_model():
    with open('src/Asset/ML_Comp/exported_data.pkl', 'rb') as file:
        exported_data = pickle.load(file)

    model = exported_data['best_model']
    categorical_features = exported_data['categorical_imputer']
    numeric_features = exported_data['numerical_imputer']
    encoder = exported_data['encoder']
    scaler = exported_data['scaler']

    return model, categorical_features, numeric_features, encoder, scaler

# Function to preprocess input data
def preprocess_data(df, categorical_features, numeric_features, encoder, scaler):
    # Apply the encoder to categorical features
    df[categorical_features] = encoder.transform(df[categorical_features])

    # Scale the numeric features
    df[numeric_features] = scaler.transform(df[numeric_features])

    return df

# Streamlit app
def main():
    st.title('Time Series Sales Prediction')

    # Load the XGBoost model and other components
    model, categorical_features, numeric_features, encoder, scaler = load_model()

    # Input fields for date, store_nbr, and family
    min_date = pd.to_datetime('2013-01-01')
    max_date = pd.to_datetime('2023-07-30')
    date = st.date_input('Select Date', value=max_date, min_value=min_date, max_value=max_date)
    store_nbr = st.slider('Enter Store Number', min_value=1, max_value=9, value=1)
    family_options = ['HOME_APPLIANCES', 'BABY_CARE', 'BREAD_BAKERY', 'FROZEN_FOODS', 'GROCERY_I', 'GROCERY_II', 'HOME_AND_KITCHEN_I', 'HOME_AND_KITCHEN_II', 'HOME_CARE', 'LAWN AND GARDEN', 'LIQUOR_WINE_BEER', 'PERSONAL CARE', 'PET SUPPLIES', 'PLAYERS_AND_ELECTRONICS', 'PREPARED_FOODS', 'SCHOOL AND OFFICE SUPPLIES']
    family = st.selectbox('Select Family', family_options)

    if st.button('Predict Sales'):
        # Create a dictionary with the variable names and their values
        data_dict = {
            'Date': [date],
            'Store Number': [store_nbr],
            'Family': [family],
        }

        # Create a DataFrame from the dictionary
        df = pd.DataFrame(data_dict)

        # Preprocess the input data
        df = preprocess_data(df, categorical_features, numeric_features, encoder, scaler)

        # Convert the DataFrame to a DMatrix (required for XGBoost predictions)
        dmatrix = xgb.DMatrix(df)

        # Make predictions using the loaded XGBoost model
        prediction = model.predict(dmatrix)

        # Display the prediction
        st.success(f'Predicted Sales for {date}, Store: {store_nbr}, Family: {family}: {prediction[0]:.2f}')

if __name__ == '__main__':
    main()