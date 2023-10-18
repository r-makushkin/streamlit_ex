import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips.columns = ['Total_Bill', 'Tip', 'Sex', 'Is_smoker', 'Day', 'Time', 'Size']


st.title("""Visualisation of Data Set""")


st.header("""Шаг 2""")
st.subheader("""Data Frame Tips""")
st.write(tips)


st.header("""Шаг 4""")
st.subheader("""Histogram Total bill""")
st.bar_chart(tips['Total_Bill'])


st.header("""Шаг 5""")
st.subheader("""Total bill to Tip""")
st.scatter_chart(data=tips, x='Tip', y='Total_Bill')


st.header("""Шаг 7""")
st.subheader("""Total bill to Tip by Size""")
st.scatter_chart(data=tips, x='Tip', y='Total_Bill', size='Size')


st.header("""Шаг 9""")
st.subheader("""Tip to Day by Sex""")
st.scatter_chart(data=tips, x='Tip', y='Day', color='Sex')

st.header("""Шаг 10""")
st.subheader("""Tip to Day by Sex""")
fig = px.box(tips, x='Day', y='Total_Bill', color='Time')
st.plotly_chart(fig)

st.header("""Шаг 11""")
st.subheader("""Histogram Tip by Time""")

fig, axes = plt.subplots(2, 1, figsize=(12, 10))
sns.barplot(tips[tips['Time'] == 'Dinner']['Tip'].reset_index(drop=True), ax=axes[0])
axes[0].set_title("Dinner")
sns.barplot(tips[tips['Time'] == 'Lunch']['Tip'].reset_index(drop=True), ax=axes[1])
axes[1].set_title("Lunch")
st.pyplot(fig)

# Попытка вывести 2 интерактивные разом через плотли сделала больно и в какой-то момент устал. Ну и не понял, как убрать значения по оси Х графика.
# bar_1 = px.bar(tips[tips['Time'] == 'Dinner']['Tip'].reset_index(drop=True), title='Dinner')
# bar_2 = px.bar(tips[tips['Time'] == 'Lunch']['Tip'].reset_index(drop=True), title='Lunch')


st.header("""Шаг 12""")
st.subheader("""Total_Bill to Tip by Is_smoker""")
male = tips[tips['Sex'] == 'Male'][['Total_Bill', 'Tip', 'Is_smoker']]
female = tips[tips['Sex'] == 'Female'][['Total_Bill', 'Tip', 'Is_smoker']]
fig, axes = plt.subplots(2, 1, figsize=(12, 10))
sns.scatterplot(data=male, x='Total_Bill', y='Tip', hue='Is_smoker', ax=axes[0])
axes[0].set_title("Male")
sns.scatterplot(data=female, x='Total_Bill', y='Tip', hue='Is_smoker', ax=axes[1])
axes[1].set_title("Female")
st.pyplot(fig)

# Так и не понял, можно ли силами стримлита сделать две фигуры в горизонтали.
# Также не понял, почему при попытке построить скаттер по коду ниже выскакивала ошибка.
# Если есть прокомментируешь, то будет неплохо с:
# st.scatter_chart(data=male, x='Total_Bill', y='Tip', color='Is_smoker')
# st.scatter_chart(data=female, x='Total_Bill', y='Tip', color='Is_smoker')