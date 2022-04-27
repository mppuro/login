import streamlit as st
import pandas as pd


names = ['Mehul Purohit','Arogya gallela']
usernames = ['mppuro','arogya']
passwords = ['123','456']
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Login','main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (name))
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
if st.session_state['authentication_status']:
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (st.session_state['name']))
    st.title('Some content')
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] == None:
    st.warning('Please enter your username and password')
