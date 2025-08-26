import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


# This decorator prevents the app from reloading the CSV file every time the user
@st.cache_data
def read_data(path):
    """
    Reads a CSV file into a pandas DataFrame.
    """

    df = pd.read_csv(path)
    return df


def main():
    """
    Configures the Streamlit app's UI and handles user input.
    """
    df = read_data('kiva_sample.csv')

    # Creates a sidebar select box for the user to choose which chart to display.
    option = st.sidebar.selectbox(
        '*Select chart*', ('Line Plot', 'Pie chart', 'Scatter Plot', 'Map'))

    # An if/elif/else block checks the user's selection and calls the
    # appropriate plotting function, then displays the resulting chart.
    if option == 'Line Plot':

        # st.pyplot() is used to render plots created with Matplotlib and Seaborn.
        st.pyplot(fig=line_plot(df))
    elif option == 'Pie chart':

        # st.plotly_chart() is used to render interactive plots from Plotly.
        st.plotly_chart(pie_chart(df))
    elif option == 'Scatter Plot':
        st.pyplot(fig=scatter_plot(df))
    elif option == 'Map':
        st.plotly_chart(map_plot(df))


def line_plot(df):
    """
    Generates and returns a Matplotlib line plot.
    """

    st.title('Line Plot')
   
    # Creates a figure and an axes object to draw the plot on.
    fig, ax = plt.subplots()
    
    # Uses Seaborn to create a line plot. The `ax` parameter specifies the
    # subplot where the plot should be drawn.
    sns.lineplot(data=df, x='funded_amount', y='loan_amount', ax=ax)
    
    # Sets the labels for the axes and the title for better readability.
    ax.set_xlabel('Funded Amount')
    ax.set_ylabel('Loan Amount')
    ax.set_title('Loan Amount vs Funded Amount')
    return fig


def pie_chart(df):
    """
    Generates and returns an interactive Plotly pie chart.
    """

    st.title('Pie Chart')

    # Uses Plotly Express for a high-level interface to create the chart.
    fig = px.pie(df, values='loan_amount', names='region', title='Loan Amount among Regions')
    
    # Updates the plot's layout, for example, changing the background color.
    fig.update_layout(
        paper_bgcolor='rgb(245, 245, 245)'
    )
    return fig


def scatter_plot(df):
    """
    Generates and returns a Matplotlib scatter plot.
    """

    st.title('Scatter Plot')
    fig, ax = plt.subplots()

    # Uses Seaborn to create the scatter plot.
    sns.scatterplot(data=df, x='funded_amount', y='loan_amount', ax=ax)
    ax.set_xlabel('Funded Amount')
    ax.set_ylabel('Loan Amount')
    ax.set_title('Loan Amount vs Funded Amount')
    return fig


def map_plot(df):
    """
    Generates and returns an interactive Plotly scatter map.
    """

    st.title('Plot on the map')

    # Plotly Express is used to create a scatter map. Points are placed using
    # latitude and longitude, and their size is determined by the 'funded_amount'.
    fig = px.scatter_map(df, lat='lat', lon='lon', size='funded_amount', zoom=7, 
    title='Funded Amount among Regions')
    return fig


if __name__ == '__main__':
    main()