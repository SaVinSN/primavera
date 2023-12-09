import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/sergeybudygin/PycharmProjects/pythonProject1/streamlite/new.csv")
def gr():
    st1 = df.loc[df["sex"] == "Female"]
    st = st1.sort_values(by=["total_bill", "tip", "tip_%_bill", "tip_per_person"], ascending=True)
    st2 = df.loc[df["sex"] == "Male"]
    stI = st2.sort_values(by=["total_bill", "tip", "tip_%_bill", "tip_per_person"], ascending=True)
    fig, ax = plt.subplots()
    plt.plot(st["total_bill"], st1["tip"], color='purple')
    plt.plot(stI["total_bill"], st2["tip"], color='blue')
    plt.xlabel("total_bill")
    plt.ylabel("tip")
    plt.axhline(y=df['tip'].mean(), color='green', linestyle='--', linewidth=1.2)

    k1 = str(st1['tip'].mean())
    k2 = str(st2['tip'].mean())

    plt.subplot(15, 2, 4)
    plt.axis(False)
    plt.text(0, 0.5, 'Female : ' + k2[:6] + '(purple)')
    plt.subplot(10, 2, 4)
    plt.axis(False)
    plt.text(0, 0.5, 'Male : ' + k1[:6] + '(blue)')
    return fig


st.title('Web applications with Streamlit, Pandas and Matplotlib')
st.header('DataSet:')
st.dataframe(df, height=300)

if st.button('Show graph'):
    st.pyplot(gr())
else:
    st.info('Click on the button above to display the graph.')

st.text('Made by Savin Sergei.')
