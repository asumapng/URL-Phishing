import streamlit as st
import pandas as pd

from PIL import Image
st.set_page_config(page_title = 'Additional Reading', page_icon =":fish:", initial_sidebar_state  = "expanded")

st.markdown("<h1 style='text-align: center; color:#727CDC;'>ADDITIONAL READING</h1>", unsafe_allow_html=True)
st.markdown('<p style="text-align: center; background-color:#727CDC;color:#000000;font-size:1px;border-radius:2%;"><b>.</p>', unsafe_allow_html=True)

st.header(":bar_chart: Phishing Statistics")

st.markdown(""" 
            - According to Verizon, 82% of data breaches involve a human element, including phishing and use of stolen credentials.
            - Email remains the number one method by which attackers phish their victims.
            - 91% of the bait emails are sent using a Gmail account, with the remaining 9% via other domains. 
            - A report from ESET mentions that the windows executables, script files, and office documents are the top 3 common types of malicious files attackes to phishing emails.
            - Yahoo is the most impersonated brand globally, when it comes to phishing attempts.
            - IBM reports that the average cost of data breach is 4.35 million USD.
            - IC3 found that social engineering scams are the common as well as the most costly attacks.
            """)
def header(url):
     st.markdown(f'<p style="text-align: center; background-color:#50526F;color:#000000;font-size:1px;border-radius:2%;"><b>{url}</p>', unsafe_allow_html=True)

header(" .")
st.header(":memo: Reports")
#st.bar_chart(data = attack_vector, x = 'Attack', y = ['2021', '2022'])
#st.bar_chart(attack_growth)
#st.bar_chart(data = attack_identify, x = 'Attack Type', y = 'Days')
#st.bar_chart(data = cloud_breach, x = 'Type', y = 'Proportion')
# st.write(attack_vector)
# st.write(attack_vector.melt("Attack", var_name = "Year", value_name = "Percent"))



st.subheader("1. ANTI-PHISHING WORKING GROUP - Phishing Activity Trends")
st.write(""" APWG is a non-profit industry association focused on eliminating the identify theft and frauds that result from the increasing phishing, crimeware and email spoofing crimes.
         APWG Phishing Activity Trends Report analyses phishing attacks and other identity theft techniques, as reported to the APWG by its member companies. """)

filo = open('downloadfiles/apwg_trends_report_q3_2022.pdf', 'rb')
st.download_button("**DOWNLOAD 2022 REPORT**", 
#st.download_button("**DOWNLOAD APWG REPORT [3RD QUARTER] 2022 REPORT**", 
                   data = filo, 
                   file_name = 'APWG_phishing_trends_report.pdf',
                   use_container_width=False)

st.subheader("2. IBM SECURITY - X-Force Threat Intelligence Index")
st.write("""IBM Security offers one of the most advanced enterprise security products and services.
         The report provides insights on the top attack types, geographics and industry trends, along with the risk mitigation recommendations.
         """)

filo = open('downloadfiles/X-Force Threat Intelligence Index 2022 Full Report.pdf', 'rb')
st.download_button("**DOWNLOAD 2022 REPORT**", 
#st.download_button("**DOWNLOAD IBM - X-FORCE THREAT INTELLIGENCE INDEX 2022 REPORT**", 
                   data = filo, 
                   file_name = 'XForce_threat_intelligence_report.pdf',
                   use_container_width=False)

st.subheader("3. SLASH NEXT - The State of Phishing")
st.write("""The SlashNext is a cybersecurity solution provider that uses AI to detect phishing and human hacking threats.
         The technology employed has the lowest false positive rate in the industry.
         The report consists of information of the next big trends in phishing, 
         top 10 services hackers use for attacks and how organizations can prevent such attacks.
         
         """)

filo = open('downloadfiles/SlashNext-The-State-of-Phishing-2022.pdf', 'rb')
#st.download_button("**DOWNLOAD THE STATE OF PHISHING 2022 REPORT**", 
st.download_button("**DOWNLOAD 2022 REPORT**", 
                   data = filo, 
                   file_name = 'SlashNext_the_state_of_phishing_2022.pdf',
                   use_container_width=False)

st.subheader("4. IBM SECURITY - Cost of Data Breach")

st.write("""IBM Security offers one of the most advanced enterprise security products and services.
         It publishes an annual report on the data breaches happening around the world. 
         The report estimates the average cost borne by an organization when a data breach occured.
         Researchers collect an in depth qualitative data through 
         interviews with individuals from various organizations that suffered a data breach. 
         The cost is calculated on both direct and indect expenses incurred by the organization.
         """)

filo = open('downloadfiles/IBM_Cost of Data Breach.pdf', 'rb')
#st.download_button("**DOWNLOAD COST OF DATA BREACH 2022 REPORT**", 
st.download_button("**DOWNLOAD 2022 REPORT**", 
                   data = filo, 
                   file_name = 'Cost_Of_Data_Breach_2022.pdf',
                   use_container_width=False)
st.write("")
header(" .")