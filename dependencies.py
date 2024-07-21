# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:30:55 2024

@author: viren
"""

import pip

try:
    import plotly.express as px
except:
    pip.main(['install', 'plotly.express'])

try:
    import streamlit as st
except:
    pip.main(['install', 'streamlit'])
    
try:
    from googleapiclient.discovery import build
    from google.oauth2 import service_account
except:
    pip.main(['install', 'google-api-python-client'])
    
try:
    import openpyxl
except:
    pip.main(['install', 'openpyxl'])
    



    