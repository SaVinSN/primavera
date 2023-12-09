import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("new.csv")
def gr():
    fig, ax = plt.subplots()
    st1 = df.loc[df["day"] == "Sat"]
    st2 = df.loc[df["day"] == "Sun"]
    st3 = df.loc[df["day"] == "Thur"]
    st4 = df.loc[df["day"] == "Fri"]
    
    a1 = st1["tip_%_bill"].mean()
    a2 = st2["tip_%_bill"].mean()
    a3 = st3["tip_%_bill"].mean()
    a4 = st3["tip_%_bill"].mean()
    
    x = ['Thur', 'Fri', 'Sat', 'Sun']
    y = [a3, a4, a1, a2]
    
    plt.bar(x, y, alpha=0.5, color=['blue', 'green', 'red', 'orange'])
    plt.xlabel('day')
    plt.plot(x, y, color='purple', marker='o', markersize=7)
    plt.ylabel('%_of_bill')
    return fig


st.title('Web applications with Streamlit, Pandas and Matplotlib')
st.header('DataSet:')
st.dataframe(df, height=300)

if st.button('Show graph'):
    st.pyplot(gr())
else:
    st.info('Click on the button above to display the graph.')

st.text('Made by Savin Sergei.')
