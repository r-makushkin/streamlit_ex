import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

st.title("""Visualisation of Data Set""")


st.header("""Шаг 2""")
st.subheader("""Data Frame Tips""")
st.write(tips)


st.header("""Шаг 4""")
st.subheader("""Histogram Total bill""")
fig = plt.figure(figsize=(10,8))
sns.barplot(tips['total_bill'])
plt.title('Total Bill')
plt.xlabel('Bill')
plt.ylabel('Total')
plt.xticks([]);
st.pyplot(fig)


st.header("""Шаг 5""")
st.subheader("""Relation Total bill to Tip""")
fig = plt.figure(figsize=(10,8))
sns.scatterplot(data=tips, x='tip', y='total_bill', hue='size')
plt.title('Realtion Total bill to Tip to Size')
plt.xlabel('Tips')
plt.ylabel('Totals')
st.pyplot(fig)


st.header("""Шаг 7""")
st.subheader("""Relation Total bill to Tip to Size""")
fig = plt.figure(figsize=(10,4))
sns.scatterplot(data=tips, x='tip', y='day', hue='sex')
plt.title('Tips to Days by Sex')
plt.xlabel('Tips')
plt.ylabel('Days');
st.pyplot(fig)

# изначально использовал встроенные методы стримлита, но не понял, как с их помощью редачить подписи и создавать взаимосвязи по 3 трем переменным
# постараюсь завтра понять, насколько возможно это делать, т.к. графики перестали быть интерактивными, что такое себе