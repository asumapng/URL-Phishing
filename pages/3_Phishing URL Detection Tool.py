import pandas as pd
import numpy as np
#import urllib
import re
from tld import get_tld
from math import log
from re import compile
from pyquery import PyQuery
from requests import get
#from urllib.parse import urlparse
import validators

import streamlit as st
st.set_page_config(page_title = 'Phishing Detection Tool', page_icon =":fish:", initial_sidebar_state  = "expanded")

st.markdown("<h1 style='text-align: center; color:#727CDC;'> &#128373 PHISHING URL DETECTION TOOL </h1>", unsafe_allow_html=True)
st.markdown('<p style="text-align: center; background-color:#727CDC;color:#000000;font-size:1px;border-radius:2%;"><b>.</p>', unsafe_allow_html=True)

import bz2file as bz2
import pickle

def decompress_pickle(file):
    model2 = bz2.BZ2File(file, 'rb')
    model2 = pickle.load(model2)
    return model2

model = decompress_pickle('comp_rf_final.pbz2')


# Functions 
try:
    # python2
    from urlparse import urlparse
except:
    # python3
    from urllib.parse import urlparse

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False
    
def suspicious_words(url):
    match = re.search('PayPal|login|signin|bank|urgency|account|update|free|registered|lucky|service|bonus|ebayisapi|webscr|security|billing', 
                      url)
    if match:
        return 1
    else:
        return 0

def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits

def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters

def Uppercase_letter_count(url):
        caps =len(re.findall(r'[A-Z]',url))
        return caps
    

def Smallcase_letter_count(url):
        caps =len(re.findall(r'[a-z]',url))
        return caps

import urllib.parse as urlparse

from urllib.parse import urlparse
def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')

from urllib.parse import urlparse
def no_of_embed(url):
    urldir = urlparse(url).path
    return urldir.count('//')

import re
def shortening_service(url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      url)
    if match:
        return 1
    else:
        return 0

import urllib.parse
def scheme(self):
    url=self
    o = urllib.parse.urlsplit(url)
    return o.scheme

#convert to text and run
from re import compile
def get_entropy( text):
        text = text.lower()
        probs = [text.count(c) / len(text) for c in set(text)]
        entropy = -sum([p * log(p) / log(2.0) for p in probs])
        return entropy

#Use of IP or not in domain
def is_ip(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        return 1
    else:
        return 0

#Importing dependencies
from urllib.parse import urlparse
from tld import get_tld

#First Directory Length
def fd_length(url):
    urlpath= urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

import urllib.parse
def domain(self):
    url=self
    o = urllib.parse.urlsplit(url)
    return o.netloc

import validators
def is_valid_domain(domain):
    
    if validators.domain(domain):
        return 1
    else:
        return 0
    
import urllib.parse
def domain_length(self):
    url=self
    o = urllib.parse.urlsplit(url)
    return len(o.netloc)

from tld import get_tld
def get_url_tld(url):
    try:
        res =get_tld(url, as_object = True)
        return res
    except:
        return 'none'

suspecious_tlds = ['fit','tk', 'gp', 'ga', 'work', 'ml', 'date', 'wang', 'men', 'icu', 'online', 'click',  
    'country', 'stream', 'download', 'xin', 'racing', 'jetzt',
    'ren', 'mom', 'party', 'review', 'trade', 'accountants', 
    'science', 'work', 'ninja', 'xyz', 'faith', 'zip', 'cricket', 'win',
    'accountant', 'realtor', 'top', 'christmas', 'gdn', 
    'link', 'asia', 'club', 'la', 'ae', 'exposed', 'pe', 'go.id', 'rs', 'k12.pa.us', 'or.kr',
    'ce.ke', 'audio', 'gob.pe', 'gov.az', 'website', 'bj', 'mx', 'media', 'sa.gov.au' 
    ]

def suspecious_tld(tld):
    suspecious_tlds = ['fit','tk', 'gp', 'ga', 'work', 'ml', 'date', 'wang', 'men', 'icu', 'online', 'click',  
        'country', 'stream', 'download', 'xin', 'racing', 'jetzt',
        'ren', 'mom', 'party', 'review', 'trade', 'accountants', 
        'science', 'work', 'ninja', 'xyz', 'faith', 'zip', 'cricket', 'win',
        'accountant', 'realtor', 'top', 'christmas', 'gdn', 
        'link', 
        'asia', 'club', 'la', 'ae', 'exposed', 'pe', 'go.id', 'rs', 'k12.pa.us', 'or.kr',
        'ce.ke', 'audio', 'gob.pe', 'gov.az', 'website', 'bj', 'mx', 'media', 'sa.gov.au' 
        ]
    if tld in suspecious_tlds:
         return 1
    else:
        return 0
    
import urllib.parse
# if the page is linked to a page
def is_linked(url):
    o = urllib.parse.urlsplit(url)
    links =   len(o.fragment)
    if links >0:
        return 1
    else:
        return 0

import urllib.parse
def len_path(self):
    url=self
    o = urllib.parse.urlsplit(url)
    return len(o.path)

import urllib.parse
def query(self):
    url=self
    o = urllib.parse.urlsplit(url)
    return len(o.query)

def add_slash_to_url(url):
    if re.search(r'\.[a-zA-Z]{2,}$', url):  # Check if TLD is present in URL
        if url[-1] != '/':
            url += '/'
    return url

import requests
def valid_link(url):
    try:
        page = requests.get(url)
        response_code = str(page.status_code) # Get the response code of given URL
        return 1
    except:
        return 0
 
# final extraction
data = pd.DataFrame()
def extract(url):
    link = add_slash_to_url(url)
    data = pd.DataFrame([link], columns = ['url'])
    data['url']=data['url'].astype(str)
    data['count-https'] = data['url'].apply(lambda i : i.count('https'))
    data['count-http'] = data['url'].apply(lambda i : i.count('http'))
    data['count%'] = data['url'].apply(lambda i: i.count('%'))
    data['count?'] = data['url'].apply(lambda i: i.count('?'))
    data['count-'] = data['url'].apply(lambda i: i.count('-'))
    data['count='] = data['url'].apply(lambda i: i.count('='))
    data['count-https'] = data['url'].apply(lambda i : i.count('https'))
    data['count%20'] =data['url'].apply(lambda i: i.count('%20'))
    data['count?'] = data['url'].apply(lambda i: i.count('?'))
    data['count-'] = data['url'].apply(lambda i: i.count('-'))
    data['count='] = data['url'].apply(lambda i: i.count('='))
    data['count-www'] = data['url'].apply(lambda i: i.count('www'))
    data['count@'] = data['url'].apply(lambda i: i.count('@'))
    data['count$'] = data['url'].apply(lambda i: i.count('$'))
    data['count_dots'] = data['url'].apply(lambda i: i.count('.'))
    data['count_&'] = data['url'].apply(lambda i: i.count('&'))
    data['count_Underscore'] = data['url'].apply(lambda i: i.count('_'))
    data['count_/'] = data['url'].apply(lambda i: i.count('/'))
    data['count_//'] = data['url'].apply(lambda i: i.count('//'))
    data['count_tilde'] = data['url'].apply(lambda i: i.count('~'))
    data['count_star'] = data['url'].apply(lambda i: i.count('*'))
    data['count_colon'] = data['url'].apply(lambda i: i.count(':'))
    data['count_comma'] = data['url'].apply(lambda i: i.count(','))
    data['count_semicolon'] = data['url'].apply(lambda i: i.count(';'))
    data['count_tilde'] = data['url'].apply(lambda i: i.count('~'))
    data['count_space'] = data['url'].apply(lambda i: i.count(' '))
    data['count_com'] = data['url'].apply(lambda i: i.count('com'))
    data['count_!'] = data['url'].apply(lambda i: i.count('!'))
    data['count_zeros'] = data['url'].apply(lambda i: i.count('0'))
    data['PayPal'] = data['url'].apply(lambda i: i.count('PayPal'))
    data['login'] = data['url'].apply(lambda i: i.count('login'))
    data['signin'] = data['url'].apply(lambda i: i.count('signin'))
    data['bank'] = data['url'].apply(lambda i: i.count('bank'))
    data['account'] = data['url'].apply(lambda i: i.count('account'))
    data['update'] = data['url'].apply(lambda i: i.count('update'))
    data['free'] = data['url'].apply(lambda i: i.count('free'))
    data['lucky'] = data['url'].apply(lambda i: i.count('lucky'))
    data['service'] = data['url'].apply(lambda i: i.count('service'))
    data['bonus'] = data['url'].apply(lambda i: i.count('bonus'))
    data['ebayisapi'] = data['url'].apply(lambda i: i.count('ebayisapi'))
    data['webscr'] = data['url'].apply(lambda i: i.count('webscr'))
    data['security'] = data['url'].apply(lambda i: i.count('security'))
    data['billing'] = data['url'].apply(lambda i: i.count('billing'))
    data['urgency'] = data['url'].apply(lambda i: i.count('urgency'))
    data['sus_url'] = data['url'].apply(lambda i: suspicious_words(i))
    data['count-digits']= data['url'].apply(lambda i: digit_count(i))
    data['count-letters']= data['url'].apply(lambda i: letter_count(i))
    data['Uppercase_letter_count']= data['url'].apply(lambda i: Uppercase_letter_count(i))
    data['Smallcase_letter_count']= data['url'].apply(lambda i: Smallcase_letter_count(i))        
    data['no_of_dir'] = data['url'].apply(lambda i: no_of_dir(i))
    data['no_of_embed'] = data['url'].apply(lambda i: no_of_embed(i))
    data['short_url'] = data['url'].apply(lambda i: shortening_service(i))
    data['url_scheme'] = data['url'].apply(lambda i: scheme(i))
    data['get_entropy']= data['url'].apply(lambda i: get_entropy(i))
    data['is_ip']= data['url'].apply(lambda i: is_ip(i))
    data['fd_length']= data['url'].apply(lambda i: fd_length(i))
    data['domain']=data['url'].apply(lambda i: domain(i))
    data['is_valid_domain']=data['domain'].apply(lambda i: is_valid_domain(i))
    data['count_dots_in_domain'] = data['domain'].apply(lambda i: i.count('.'))
    data['domain_length']=data['url'].apply(lambda i: domain_length(i))
    data['get_url_tld'] = data['url'].apply(lambda i: get_url_tld(i))
    data['suspecious_tld'] = data['get_url_tld'].apply(lambda i: suspecious_tld(i))
    data['is_linked'] = data['url'].apply(lambda i: is_linked(i))
    data['len_path'] = data['url'].apply(lambda i: len_path(i))
    data['query'] = data['url'].apply(lambda i: query(i))

    data['tld']=(np.where(data['get_url_tld'].str.contains('com', re),'com',
                          np.where(data['get_url_tld'].str.contains('co'),'co',
                                   np.where(data['get_url_tld'].str.contains('org'),'org',
                                            np.where(data['get_url_tld'].str.contains('edu'),'edu',
                                                     np.where(data['get_url_tld'].str.contains('net'),'net', 'others'))))))

    data['tld_others'] = np.where(data['get_url_tld']=='com', 0, 1)
    data['url_scheme_http']=np.where(data['url_scheme']=="http",1,0)
    data['url_scheme_https']=np.where(data['url_scheme']=="https",1,0)
    data['url_scheme_news']=np.where(data['url_scheme']=="news",1,0)
    data['url_scheme_sherlock']=np.where(data['url_scheme']=="sherlock",1,0)
    data['url_scheme_gopher']=np.where(data['url_scheme']=="gopher",1,0)


#     return data
    X = data[['count-https', 'count-', 'count-www', 'count_dots', 'count_/',
       'sus_url', 'count-digits', 'count-letters', 'Uppercase_letter_count',
       'Smallcase_letter_count', 'no_of_dir', 'get_entropy', 'fd_length',
       'count_dots_in_domain', 'domain_length', 'len_path', 'url_scheme_http',
       'url_scheme_https', 'tld_others']]
    prediction = model.predict(X)
    return prediction

st.write("      ")

def htmlstring(txt, colour):
    htmlstr1=f"""<p style='background-color:{colour};
                                               color:white;
                                               font-size:18px;
                                               border-radius:3px;
                                               line-height:60px;
                                               padding-left:17px;
                                               opacity:100'>
                                               {txt}</style>
                                               <br></p>"""
    return st.markdown(htmlstr1, unsafe_allow_html=True)


st.subheader(' Use our phishing detection tool that uses ML techniques to check whether a link is phishing link or not.')
with st.form("my_form"):
   url = st.text_input(label = "", placeholder = "ENTER THE URL HERE", key = 'Link')
   
   def local_css(file_name):
       with open(file_name) as f:
           st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
           
   def clear_text():
       st.session_state["Link"] = "" 

   local_css("button_style.css")
   
   f3, f4 = st.columns([2.4, 0.6])
   
   with f3:
           
       submitted = st.form_submit_button("**CHECK THE LINK**", use_container_width=True, type='primary')
       
       st.markdown("   ")
       st.markdown("   ")
    
       phish = ""
    
   with f4:
        clear = st.form_submit_button(label="**CLEAR**", on_click=clear_text, use_container_width=True)
        


if submitted:
    if url == "":
        phish = "PLEASE PASTE THE LINK TO PROCEED."
        st.warning(phish)
    
    else: 
        a = valid_link(url)
        if a == 1:
            try:
                result = extract(url)
                if result == 1:
                    phish = "THIS URL MAY BE A PHISHING LINK. DO NOT CLICK."
                    st.error(phish)
                else:
                   if result == 0:
                       phish = "THIS IS A SAFE URL."
                       st.success(phish)
                   else: 
                       phish = "PLEASE ENTER A VALID LINK."
                       st.warning(phish) 
            except:
                 phish = "ENTER A VALID LINK"
                 st.warning(phish)
        else:
            phish = "THE ABOVE ENTERED IS A BROKEN LINK OR MAY NOT BE AN URL. PLEASE ENTER A VALID URL."
            st.warning(phish)
       




    

              
   
