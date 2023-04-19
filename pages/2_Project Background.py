import streamlit as st

st.set_page_config(page_title = 'Project Background', page_icon =":fish:", initial_sidebar_state  = "expanded")

st.markdown("<h1 style='text-align: center; color: #727CDC;'> PROJECT BACKGROUND</h1>", unsafe_allow_html=True)
st.markdown('<p style="text-align: center; background-color:#727CDC;color:#000000;font-size:1px;border-radius:2%;"><b>.</p>', unsafe_allow_html=True)

def header(url):
     st.markdown(f'<p style="text-align: center; background-color:#50526F;color:#000000;font-size:1px;border-radius:2%;"><b>{url}</p>', unsafe_allow_html=True)

st.write('''
         Phishing is one of the most common types of cybercrime committed today. 
         The victims of this type of attack are not only individuals but also big corporations. 
         In the 'Cost of Data Breach 2022' report by IBM, we can clearly understand the consequences and cost of a data breach for a corporation. 
         Corporations spend millions of dollars to prevent such data breaches, on advanced tools and techniques and yet phishing attacks are on the rise. 

         \nIn 2022, 255 million phishing attacks were reported to a cyber security solutions provider, the SlashNext Organization. 
         This number is projected to increase exponentially in 2023.
         Most of the phishing cases today go unreported because the victims are unaware of being attacked. 
         
         \nAnother recent trend identified is the increase in 'Zero-Hour' phishing threats.
         These are attacks by using links that are new and not yet present in the existing databases. 
         It would take some time before these links get detectes and starts appearing on the blacklist.
         
         \nThe current technology used to detect phishing websites is the Google Safe Browsing service, which is adopted by most web browsers.
         It is a tool that blocks the website access to users based on a blacklist given to it. 
         This tool fails in identifying Zero-Hour threats. Our project aims to solve this issue using ML techniques.
         
         \n :jigsaw: **So the objectives of our project are:**
         ''')
         
st.write('''
            1. Build a phishing URL detection model using multiple ML techniques
            2. Build an interactive web application for users to check phishing urls.
        ''')
        
st.write('''
         \n We have successfully met both our objectives. 
         8 ML models were trained and tested.
         The machine learning model used on our detection tool is Random Forest. 
         This technique was picked as the final model as it provided us the maximum accuracy in detecting phishing links.
         We are currently using only the heuristics and domain based information from the URLs.
         
         ''')

pressed = st.button('**CLICK TO USE THE PHISHING DETECTION TOOL**', 
                    use_container_width=True, type = "primary")


def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    
if pressed:
   nav_to('https://url-phishing-detector-using-ml-suma-srushti.streamlit.app/Phishing_URL_Detection_Tool')
