import streamlit as st
from PIL import Image

st.set_page_config(page_title = 'Phishing Guidelines', page_icon =":fish:", initial_sidebar_state  = "expanded")

def header(url):
     st.markdown(f'<p style="text-align: center; background-color:#50526F;color:#000000;font-size:1px;border-radius:2%;"><b>{url}</p>', unsafe_allow_html=True)
     
st.markdown("<h1 style='text-align: center; color: #727CDC;'>A GUIDE TO UNDERSTAND PHISHING</h1>", unsafe_allow_html=True)

st.markdown('<p style="text-align: center; background-color:#727CDC;color:#000000;font-size:1px;border-radius:2%;"><b>.</p>', unsafe_allow_html=True)

import base64
file_ = open('phishing_banner.gif', 'rb')
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<p align = "center"> <img src="data:image/gif;base64,{data_url}" alt="microsoft phishing report gif"  width=700> </p>',
    unsafe_allow_html=True,
)
#st.caption("Image source : Webroot.com")

pic = Image.open('icon.png', mode = 'r', formats = None)

st.markdown("<h2 style='color: #727CDC;'> &#128051 What is Phishing? </h2>", unsafe_allow_html=True)

st.write("""Phishing is the most common type of attack in cyber security today. 
         It is when a victim receives a link to a clone or phishing website of a trusted domain and 
         is tricked into providing login credentials. 
         The clone website looks the same as the legitimate one, 
         but with minor differences which go unnoticed in the process. 
         Details like credit card numbers, cvv, and banking details are compromised.""")
         
st.write ('There are several variations of phishing done today. A few of those are:')

st.subheader("1. Vishing :calling: 	:telephone_receiver:" )
st.write('      Vishing is the term used when an attacker impersonates a trustworthy individual over voice communications to obtain information. Smishing is the practice of doing the same through SMS or text messages. To trick the victim into disclosing valuable information, the attacker might pretend to be a trusted friend when calling or messaging the victim.')

st.subheader("2. Spear Phishing :mailbox_with_mail: :e-mail:  " )
st.write('      Spear phishing is the practice of an attacker sending emails to the victim and persuading him to click on a certain link and take an action, such as logging in or sharing personal information.')

st.subheader("3. Angler Phishing :iphone:" )
st.write('Angler Phishing is the act when an attacker approaches victims through social media platforms or accounts while posing as a customer support staff and tricking them into revealing details.')
st.write("")
header("\n .")
st.markdown("<h2 style='color: #727CDC;'> &#8986  Phishing Process </h2>", unsafe_allow_html=True)

pic = Image.open('phishingprocess.png', mode = 'r', formats = None)
st.image(pic, caption = "Phishing attack done is usually done through spamming phishing links to victims.")

st.write("")
header("\n .")


############################

def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    
##########

st.markdown("<h2 style='color: #727CDC;'> &#128274 <b> How to protect yourself from a phishing attack</h2>", unsafe_allow_html=True)

st.subheader("1. Learn to recognise phishing emails, messages and urls")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

with st.expander("The key to not falling prey to phishing attacks is awareness.      \nHere are some ways to recognize a phishing email:rr", expanded = True):
    st.markdown("""
                - When you recieve an email from someone for the first time, especially outside the organisation or your mailing 
                list, verify the source before acting on it.
                - If you find a lot spelling and grammatical errors, the chances of it being a scam/phishing email is high.
                - Mails starting with generic greetings like "Dear Sir/Ma'am",  is a warning sign that it might not be from 
                a trusted sender. Personalization of messages and emails is easy these days.
                - Be on a lookout for very subtle misspellings of the legitimate domain main. 
                Eg: xyz@microsoft vs. xyz@ricr0soft.
                - If the suspicious message has a link or any attachments, do not download it.
                - Install an antivirus or anti phishing softwares on your devices. 
                There are many open source options today that provide free service.
                """)

st.subheader("2. Report the suspicious website or email")

with st.expander("Google and Microsoft, along with the regional cybersecurity bodies, work towards providing a safe space to internet users. Reporting the threat can help prevent other users from being scammed or phished. Here are some ways to report phishing emails:", expanded = True):
    
    tab1, tab2 = st.tabs(['**MS OUTLOOK 365**', '**GMAIL**'])

    with tab1:
        st.write("**Follow these steps:**")
        st.write("""
                 - Open the mail.
                 - Choose **Report message** from the ribbon.
                 - Select **Report Phishing** . 
                \n   """)
         
        
        import base64
        file_ = open('microsoft_phishing.gif', 'rb')
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        
        st.markdown(
            f'<p align = "center"> <img src="data:image/gif;base64,{data_url}" alt="microsoft phishing report gif"  width=500> </p>',
            unsafe_allow_html=True,
        )
    
    with tab2:
        st.write("**Follow these steps:**")
        st.write("""
                 - Open the mail. 
                 - Click on the three dots on the right side of the sender address. 
                 - Click **Report Phishing.**""")
        
        import base64
        file_ = open('google report.gif', 'rb')
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        
        st.markdown(
            f'<p align = "center"> <img src="data:image/gif;base64,{data_url}" alt="microsoft phishing report gif"  width=500> </p>',
            unsafe_allow_html=True,
        )

st.subheader("3. Be updated with the recent trends in phishing attacks")

pressed = st.button('**CLICK TO READ THE RECENT STATISTICS AND REPORTS**', 
                    use_container_width=True)
if pressed:
   nav_to('https://phishingdetectionforurls.streamlit.app/Additional_Reading')

#######################
st.write("")
st.write("")
header("\n .")
st.markdown("<h2 style='color: #727CDC;'> &#128373 Phishing URL Detection Tool </h2>", unsafe_allow_html=True)
st.write("""
         You can also insert check if a URL sent to you is a phishing or legitimate link from our ML based Phishing Link Detection Tool.
         """)
         
pressed = st.button('**CLICK TO USE PHISHING DETECTION TOOL**', 
                    use_container_width=True, type = 'primary')
if pressed:
   nav_to('https://phishingdetectionforurls.streamlit.app/Phishing_URL_Detection_Tool')

st.write("")
st.write("")
header("\n .")
   
# color = st.color_picker('Pick A Color', '#00f900')
# st.write('The current color is', color)

