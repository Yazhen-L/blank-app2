import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns #if it is yellow, you need to manually install in the terminal
import streamlit as st
import pandas as pd

## Step 01-Introduction
st.title("California - Real Estate Agency 🏡")

st.write("Explore the portofolio of our real estate agency in a nice way >>")

st.image("real_estate.jpg")

st.write("  ")
st.write("  ")
st.write("  ")

## Step 02-Load Dataset
st.subheader("01 Data Exploration")

st.markdown("#### Display dataset")
df = pd.read_csv("housing.csv")
st.dataframe(df)

st.markdown("#### Statistic about the dataset")
st.dataframe(df.describe())

## Step 03-Data viz
st.subheader("02 Data Viz")

st.markdown("#### Bar Chart - Seaborn")

# start with creating the empty frame that receives the plot
fig_bar, ax_bar = plt.subplots(figsize=(8,6)) #we need to specify the size of our plot, length = 8, height =6
# create the plot, in this case with searborn
sns.barplot(data=df, x="ocean_proximity", y="median_house_value")
# render提供 the plot in streamlit
st.pyplot(fig_bar)

st.markdown("#### Bar Chart - Streamlit")
st.bar_chart(data=df, x="ocean_proximity", y="median_house_value")


st.markdown("#### Correlation matrix")

corr_df = df.drop("ocean_proximity", axis=1) # as this column is not in number type
fig, ax = plt.subplots(figsize=(18,14))
sns.heatmap(corr_df.corr(),annot=True,fmt=".2f",cmap='coolwarm')
st.pyplot(fig)

st.write(list(df.columns))

user_selection = st.multiselect("Select the variables you want for the corr matix", list(df.columns),["latitude","longitude"])
st.write(user_selection)

corr_user_selection = corr_df[user_selection]

## start with creating the empty frame that receives the plot
fig_corr, ax_corr = plt.subplots(figsize=(18,14))
## create the plot, in this case with seaborn 
sns.heatmap(corr_user_selection.corr(),annot=True,fmt=".2f",cmap='coolwarm')
## render the plot in streamlit 
st.pyplot(fig_corr)
