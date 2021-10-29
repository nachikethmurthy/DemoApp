import streamlit as st

#Text/ Title
st.title('Streamlit - Edureka')

#Header/ Sub-Header
st.header('This is a Header')
st.subheader('This is a Sub-Header')

#Text
st.text('This is a Text')

#Markdown
st.markdown("### This is a Markdown")

#Working with Colorful Text and Error Messages

st.success("Successful")

st.info("Info.")

st.warning("This is a warning")

st.error("This is an error message")

#Getting Help Information about Python

st.help(range)

#Widgets: Checkbox,Selectbox,Radio button,etc

# Checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")


# Radio Buttons
status = st.radio("What's the capital of India?",("Mumbai","Delhi"))

if status == 'Delhi':
	st.success("You are Right")
else:
	st.warning("You are Wrong")

# SelectBox

work = st.selectbox("Your Work",["Programmer","Data Analyst","Doctor"])
st.write("You selected this option ",work)


# MultiSelect
location = st.multiselect("Where do you work?",("Boston","New York","Moscow","Sydney","New Jersey"))
st.write("You selected",len(location),"locations")

# Slider
level = st.slider("What is your level",1,5)


# Buttons
st.button("A Simple Button")

if st.button("About"):
	st.text("Streamlit is Awesome")

#Using the write function
# Writing Text Functions
st.write("Text with write")

st.write(range(20))

#Working with Functions

# Normal Function
def run_fxn():
    return range(20)

st.write(run_fxn())

# To Improve Performance/Speed via caching
@st.cache
def run_fxn():
    return range(20)

st.write(run_fxn())

# Plot
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
st.pyplot(fig)

# DataFrames
import pandas as pd
DATA_URL = (
    "IBM.csv"
)
@st.cache(persist=True)
def load_data():
    df = pd.read_csv(DATA_URL)
    
    return df

df = load_data()
st.dataframe(df)

# Tables
st.table(df.head())

#Showing Sidebars
st.sidebar.header("About")
st.sidebar.text("This is Streamlit")


