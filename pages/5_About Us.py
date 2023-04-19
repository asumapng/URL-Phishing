import streamlit as st

st.set_page_config(page_title = 'About Us', page_icon =":fish:", initial_sidebar_state  = "expanded")


st.markdown("<h1 style='text-align: center; color:#727CDC;'> &#128105;&#8205;&#127891; ABOUT US</h1>", unsafe_allow_html=True)
st.markdown('<p style="text-align: center; background-color:#727CDC;color:#000000;font-size:1px;border-radius:2%;"><b>.</p>', unsafe_allow_html=True)

st.write("""We are Suma and Srushti, students of Mount Carmel College, Autonomous, Bangalore.
         We are in our final year of Bachelor's in Vocation (Data Science and Analytics) course. 
         This website is our final semester project.
         We are working on building a URL phishing detector tool using AI/ML Techniques and creating a web application for public use.
         """)
def header(url):
     st.markdown(f'<p style="text-align: center; background-color:#50526F;color:#000000;font-size:1px;border-radius:2%;"><b>{url}</p>', unsafe_allow_html=True)

header(" .")

st.markdown("<h2 style='color: #727CDC;'><b> &#128231  Contact Details </h2>", unsafe_allow_html=True)
st.markdown(""" Suma N  : suma.nadakkannu@gmail.com  
             Srushti D  : srusti19d@gmail.com""")

st.markdown(""" College : Mount Carmel College, Autonomous  
                         Location : Bangalore, IN""")

st.write("")
header(" .")