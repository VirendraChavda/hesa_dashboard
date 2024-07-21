# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:48:45 2024

@author: viren
"""
#%% Csv read
import pip

try:
    import plotly.express as px
except:
    pip.main(['install', 'plotly.express'])
    import plotly.express as px

try:
    import streamlit as st
except:
    pip.main(['install', 'streamlit'])
    import streamlit as st
    
try:
    from googleapiclient.discovery import build
    from google.oauth2 import service_account
except:
    pip.main(['install', 'google-api-python-client'])
    
    
import pandas as pd
from datetime import datetime

from googleapiclient.http import MediaFileUpload

# Below line of code sets the notebook to not give warnings while running any code.
import warnings
warnings.filterwarnings('ignore')

sub_main = pd.read_csv('Data/updated.csv')

#%% Google Drive Setup
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = '1CaZvKjo4T6IXSFCxIGbK93Z_EoTc3MkC'

def start_service():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
    service = build('drive', 'v3', credentials = creds)
    return service
        
def upload_file(file_path):
    service = start_service()
    file_metadata = {
        'name' : "Comments",
        'parents' : [PARENT_FOLDER_ID],
        'mimeType': 'text/csv'
        }
    
    service.files().create(
        body = file_metadata,
        media_body = file_path
        ).execute()
    
def update_file(file_path):
    service = start_service()
    # Call the Drive v3 API
    results = service.files().list(q='name contains "Comments"').execute()
    # get the results
    item_list = results.get('files', [])
    item_to_replace = item_list[0]
    
    file_id = item_to_replace["id"]
    media = MediaFileUpload(file_path, mimetype="text/csv")
    
    service.files().update(
        fileId = file_id,
        media_body = media
        ).execute()
    

#%% Setting the page for streamlit

st.set_page_config(page_title = "HESA Data Analysis", page_icon = ":bar_chart:", layout = "wide")

page_title = st.radio("Mode", ["****Normal****", "****Comparison****"])
st.markdown(
    """<style>div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 22px;}
    </style>
    """, unsafe_allow_html=True)
st.title(":bar_chart: Higher education institutions in the UK")

st.markdown('<style>div.block-container{padding-top:1rem;} </style>', unsafe_allow_html = True)
    
if page_title == "****Normal****":
    line_id = "1"
else:
    line_id = "2"
    
# Create columns

if page_title == "****Normal****":
    col1, col2, col3 = st.columns([1, 2.25, 2.25])
else:
    col1, col2, col3, col4 = st.columns([1, 2.5, 2.5, 1])

#%% Filter 1
with col1:
    st.subheader("Filter")
    country = st.multiselect("Country", sorted(sub_main["Country"].unique()))
    if not country:
        df = sub_main.copy()
    else:
        df = sub_main[sub_main["Country"].isin(country)]
        line_id = line_id + 'a'
    
    region = st.multiselect("Region", sorted(df["Region"].unique()))
    if not region:
        df1 = df.copy()
    else:
        df1 = df[df["Region"].isin(region)]
        line_id = line_id + 'b'
        
    county = st.multiselect("County", sorted(df1["County"].unique()))
    if not county:
        df2 = df1.copy()
    else:
        df2 = df1[df1["County"].isin(county)]
        line_id = line_id + 'c'
        
    group = st.multiselect("Associated Group", sorted(df2["Association"].unique()))
    if not group:
        df3 = df2.copy()
    else:
        df3 = df2[df2["Association"].isin(group)]
        line_id = line_id + 'd'
        
    established = st.multiselect("Establishment Group", sorted(df3["Established"].unique()))
    if not established:
        df4 = df3.copy()
    else:
        df4 = df3[df3["Established"].isin(established)]
        line_id = line_id + 'e'
        
    funding = st.multiselect("Source of funding", sorted(df4["Funding"].unique()))
    if not funding:
        df5 = df4.copy()
    else:
        df5 = df4[df4["Funding"].isin(funding)]
        line_id = line_id + 'f'
        
    rank = st.multiselect("Ranking Group", sorted(df5["Rank_group"].unique()))
    if not rank:
        df6 = df5.copy()
    else:
        df6 = df5[df5["Rank_group"].isin(rank)]
        line_id = line_id + 'g'
        
    income = st.multiselect("Income Group", sorted(df6["Income_group"].unique()))
    if not income:
        df7 = df6.copy()
    else:
        df7 = df6[df6["Income_group"].isin(income)]
        line_id = line_id + 'h'
        
    size = st.multiselect("University Size", sorted(df7["Uni_size"].unique()))
    if not size:
        df8 = df7.copy()
    else:
        df8 = df7[df7["Uni_size"].isin(size)]
        line_id = line_id + 'i'
        
    uni_type = st.multiselect("Type of Courses", sorted(df8["Courses_type"].unique()))
    if not uni_type:
        df9 = df8.copy()
    else:
        df9 = df8[df8["Courses_type"].isin(uni_type)]
        line_id = line_id + 'j'
        
    accomodation = st.multiselect("University accomodation", sorted(df9["Accomodation"].unique()))
    if not accomodation:
        df10 = df9.copy()
    else:
        df10 = df9[df9["Accomodation"].isin(accomodation)]
        line_id = line_id + 'k'
        
    university = st.multiselect("Name of the University", sorted(df10["University"].unique()))
    if not university:
        df11 = df10.copy()
    else:
        df11 = df10[df10["University"].isin(university)]
        line_id = line_id + 'l'
        
    
filtered_df = df11.copy()
filtered_df = filtered_df.groupby(["Academic Year"]).sum()

percent_cols = ["Total Income", "Tuition fees and education contracts", "Funding body grants", "Research grants and contracts",
                "Other income", "Investment income", "Donations and endowments", "Total Expenditure", "Staff Costs",
                "Surplus/Deficit", "Staff Costs / Total Expenditure", "Fees_UK", "Fees_international", "Fees_EU",
                "Fees_total_other", "Total_students", "UK_students", "EU_students", "Non-EU_students"]

for i in percent_cols:
    value_list = []
    for each in range(len(filtered_df[i])):
        if filtered_df[i][each] == 0 or filtered_df[i][each] < 0:
            pass
        else:
            value_list.append(filtered_df[i][each])
    try:
        base_value = min(value_list)
    except:
        base_value = 0
    
    filtered_df[f"{i}%"] = 0
    for j in range(len(filtered_df[f"{i}%"])):
        filtered_df[f"{i}%"][j] = ((filtered_df[i][j] - base_value)/base_value) * 100
        
#%% Filter 2
if page_title =="****Comparison****":
    with col4:
        st.subheader("Filter")
        
        country_2 = st.multiselect("Country*", sorted(sub_main["Country"].unique()))
        if not country_2:
            dff = sub_main.copy()
        else:
            dff = sub_main[sub_main["Country"].isin(country_2)]
            line_id = line_id + 'm'
            
        region_2 = st.multiselect("Region*", sorted(dff["Region"].unique()))
        if not region_2:
            dff1 = dff.copy()
        else:
            dff1 = dff[dff["Region"].isin(region_2)]
            line_id = line_id + 'n'
            
        county_2 = st.multiselect("County*", sorted(dff1["County"].unique()))
        if not county_2:
            dff2 = dff1.copy()
        else:
            dff2 = dff1[dff1["County"].isin(county_2)]
            line_id = line_id + 'o'
            
        group_2 = st.multiselect("Associated Group*", sorted(dff2["Association"].unique()))
        if not group_2:
            dff3 = dff2.copy()
        else:
            dff3 = dff2[dff2["Association"].isin(group_2)]
            line_id = line_id + 'p'
        
        established_2 = st.multiselect("Establishment Group*", sorted(dff3["Established"].unique()))
        if not established_2:
            dff4 = dff3.copy()
        else:
            dff4 = dff3[dff3["Established"].isin(established_2)]
            line_id = line_id + 'q'
            
        funding_2 = st.multiselect("Source of funding*", sorted(dff4["Funding"].unique()))
        if not funding_2:
            dff5 = dff4.copy()
        else:
            dff5 = dff4[dff4["Funding"].isin(funding_2)]
            line_id = line_id + 'r'
            
        rank_2 = st.multiselect("Ranking Group*", sorted(dff5["Rank_group"].unique()))
        if not rank_2:
            dff6 = dff5.copy()
        else:
            dff6 = dff5[dff5["Rank_group"].isin(rank_2)]
            line_id = line_id + 's'
            
        income_2 = st.multiselect("Income Group*", sorted(dff6["Income_group"].unique()))
        if not income_2:
            dff7 = dff6.copy()
        else:
            dff7 = dff6[dff6["Income_group"].isin(income_2)]
            line_id = line_id + 't'
            
        size_2 = st.multiselect("University Size*", sorted(dff7["Uni_size"].unique()))
        if not size_2:
            dff8 = dff7.copy()
        else:
            dff8 = dff7[dff7["Uni_size"].isin(size_2)]
            line_id = line_id + 'u'
            
        uni_type_2 = st.multiselect("Type of Courses*", sorted(dff8["Courses_type"].unique()))
        if not uni_type_2:
            dff9 = dff8.copy()
        else:
            dff9 = dff8[dff8["Courses_type"].isin(uni_type_2)]
            line_id = line_id + 'v'
            
        accomodation_2 = st.multiselect("University accomodation*", sorted(dff9["Accomodation"].unique()))
        if not accomodation_2:
            dff10 = dff9.copy()
        else:
            dff10 = dff9[dff9["Accomodation"].isin(accomodation_2)]
            line_id = line_id + 'w'
            
        university_2 = st.multiselect("Name of the University*", sorted(dff10["University"].unique()))
        if not university_2:
            dff11 = dff10.copy()
        else:
            dff11 = dff10[dff10["University"].isin(university_2)]
            line_id = line_id + 'x'
        
    filtered_dff = dff11.copy()
    filtered_dff = filtered_dff.groupby(["Academic Year"]).sum()
    
    percent_cols = ["Total Income", "Tuition fees and education contracts", "Funding body grants", "Research grants and contracts",
                    "Other income", "Investment income", "Donations and endowments", "Total Expenditure", "Staff Costs",
                    "Surplus/Deficit", "Staff Costs / Total Expenditure", "Fees_UK", "Fees_international", "Fees_EU",
                    "Fees_total_other", "Total_students", "UK_students", "EU_students", "Non-EU_students"]
    
    for i in percent_cols:
        value_list = []
        for each in range(len(filtered_dff[i])):
            if filtered_dff[i][each] == 0 or filtered_dff[i][each] < 0:
                pass
            else:
                value_list.append(filtered_dff[i][each])
        
        try:
            base_value = min(value_list)
        except:
            base_value = 0
        
        filtered_dff[f"{i}%"] = 0
        for j in range(len(filtered_dff[f"{i}%"])):
            filtered_dff[f"{i}%"][j] = ((filtered_dff[i][j] - base_value)/base_value) * 100

#%% Graph 1
with col2:
    st.subheader("Trends")
    a = st.selectbox("Select from dropdown", ["Income", "Expense", "Surplus/Deficit", "No. of students"])
    if a == "Income":
        sub_col = st.selectbox("Select from dropdown", ["Total Income","Tuition fees and education contracts",
                                                        "Funding body grants", "Research grants and contracts",
                                                        "Other income", "Investment income","Donations and endowments"])
        
        if sub_col == "Total Income":
            trend_cols = ["Total Income%"]
            
        elif sub_col == "Tuition fees and education contracts":
            sub_col1 = st.selectbox("Select from dropdown", ["Total Tuition fees and education contracts", "Fees_UK",
                                                             "Fees_international", "Fees_EU", "Fees_total_other"])
            
            if sub_col1 == "Total Tuition fees and education contracts":
                trend_cols = ["Tuition fees and education contracts%"]
            elif sub_col1 == "Fees_UK":
                trend_cols = ["Fees_UK%"]
            elif sub_col1 == "Fees_international":
                trend_cols = ["Fees_international%"]
            elif sub_col1 == "Fees_EU":
                trend_cols = ["Fees_EU%"]
            elif sub_col1 == "Fees_total_other":
                trend_cols = ["Fees_total_other%"]
        elif sub_col == "Funding body grants":
            trend_cols = ["Funding body grants%"]
        elif sub_col == "Research grants and contracts":
            trend_cols = ["Research grants and contracts%"]
        elif sub_col == "Other income":
            trend_cols = ["Other income%"]
        elif sub_col == "Investment income":
            trend_cols = ["Investment income%"]
        elif sub_col == "Donations and endowments":
            trend_cols = ["Donations and endowments%"]
            
    elif a == "Expense":
        sub_col = st.selectbox("Select from dropdown", ["Total Expenditure","Staff Costs", "Staff Costs/Total Expenditure"])
        
        if sub_col == "Total Expenditure":
            trend_cols = ["Total Expenditure%"]
        elif sub_col == "Staff Costs":
            trend_cols = ["Staff Costs%"]
        elif sub_col == "Staff Costs/Total Expenditure":
            trend_cols = ["Staff Costs / Total Expenditure%"]
            
    elif a == "Surplus/Deficit":
        trend_cols = ["Surplus/Deficit%"]
            
    elif a == "No. of students":
        sub_col = st.selectbox("Select from dropdown", ["Total_students", "UK_students", "EU_students", "Non-EU_students"])
        
        if sub_col == "Total_students":
            trend_cols = ["Total_students%"]
        elif sub_col == "UK_students":
            trend_cols = ["UK_students%"]
        elif sub_col == "EU_students":
            trend_cols = ["EU_students%"]
        elif sub_col == "Non-EU_students":
            trend_cols = ["Non-EU_students%"]
        
    # Line plot code
    for i in trend_cols:
        j = i[:-1]
        fig = px.line(filtered_df, x = filtered_df.index, y=filtered_df[i])
        fig.update_layout(autosize=False, width=400, height=525)
        st.plotly_chart(fig, use_container_width = True)
        st.write(filtered_df[[j]])
        st.write("*Absolute values are in Millions(except for student numbers)")
      
        
if page_title == "****Comparison****":
    with col3:
        st.subheader("Trends")
        a = st.selectbox("Select from dropdown", ["Income*", "Expense*", "Surplus/Deficit*", "No. of students*"])
        if a == "Income*":
            sub_col = st.selectbox("Select from dropdown", ["Total Income*","Tuition fees and education contracts*",
                                                            "Funding body grants*", "Research grants and contracts*",
                                                            "Other income*", "Investment income*","Donations and endowments*"])
            
            if sub_col == "Total Income*":
                trend_cols = ["Total Income%"]
                
            elif sub_col == "Tuition fees and education contracts*":
                sub_col1 = st.selectbox("Select from dropdown", ["Total Tuition fees and education contracts*", "Fees_UK*",
                                                                 "Fees_international*", "Fees_EU*", "Fees_total_other*"])
                
                if sub_col1 == "Total Tuition fees and education contracts*":
                    trend_cols = ["Tuition fees and education contracts%"]
                elif sub_col1 == "Fees_UK*":
                    trend_cols = ["Fees_UK%"]
                elif sub_col1 == "Fees_international*":
                    trend_cols = ["Fees_international%"]
                elif sub_col1 == "Fees_EU*":
                    trend_cols = ["Fees_EU%"]
                elif sub_col1 == "Fees_total_other*":
                    trend_cols = ["Fees_total_other%"]
            elif sub_col == "Funding body grants*":
                trend_cols = ["Funding body grants%"]
            elif sub_col == "Research grants and contracts*":
                trend_cols = ["Research grants and contracts%"]
            elif sub_col == "Other income*":
                trend_cols = ["Other income%"]
            elif sub_col == "Investment income*":
                trend_cols = ["Investment income%"]
            elif sub_col == "Donations and endowments*":
                trend_cols = ["Donations and endowments%"]
                
        elif a == "Expense*":
            sub_col = st.selectbox("Select from dropdown", ["Total Expenditure*","Staff Costs*",
                                                            "Staff Costs/Total Expenditure*"])
            
            if sub_col == "Total Expenditure*":
                trend_cols = ["Total Expenditure%"]
            elif sub_col == "Staff Costs*":
                trend_cols = ["Staff Costs%"]
            elif sub_col == "Staff Costs/Total Expenditure*":
                trend_cols = ["Staff Costs / Total Expenditure%"]
                
        elif a == "Surplus/Deficit*":
            trend_cols = ["Surplus/Deficit%"]
                
        elif a == "No. of students*":
            sub_col = st.selectbox("Select from dropdown", ["Total_students*", "UK_students*", "EU_students*",
                                                            "Non-EU_students*"])
            
            if sub_col == "Total_students*":
                trend_cols = ["Total_students%"]
            elif sub_col == "UK_students*":
                trend_cols = ["UK_students%"]
            elif sub_col == "EU_students*":
                trend_cols = ["EU_students%"]
            elif sub_col == "Non-EU_students*":
                trend_cols = ["Non-EU_students%"]
            
        # Line plot code
        for i in trend_cols:
            j = i[:-1]
            fig = px.line(filtered_dff, x = filtered_dff.index, y=filtered_dff[i])
            fig.update_layout(autosize=False, width=400, height=525)
            st.plotly_chart(fig, use_container_width = True)
            st.write(filtered_dff[[j]])
            st.write("*Absolute values are in Millions(except for student numbers)")

#%% Graph 2
if page_title == "****Normal****":
    with col3:
        st.subheader("Share")
            
        b = st.selectbox("Select from dropdown", ["Income", "Fees", "Admissions"])
        
        year = st.multiselect("Academic Year", filtered_df.index)
        if not year:
            filtered_df = filtered_df.copy()
        else:
            filtered_df = filtered_df[filtered_df.index.isin(year)]
           
        if b == "Income":
            inc_share_cols = ["Tuition fees and education contracts", "Funding body grants",
                            "Research grants and contracts", "Other income", "Investment income",
                            "Donations and endowments"]
        elif b == "Fees":
            inc_share_cols = ["Fees_UK", "Fees_international", "Fees_EU", "Fees_total_other"]
        else:
            inc_share_cols = ["UK_students", "EU_students", "Non-EU_students"]
            
        b_values = filtered_df[inc_share_cols].mean()
        avg_df = pd.DataFrame(b_values, columns=['Mean'])
        avg_df.index.names = ['Component']
            
        # Pie chart code:
        fig = px.pie(filtered_df, values = b_values, names = inc_share_cols, hole = 0.35)
        fig.update_layout(autosize=False, width=425, height=525)
        #fig.update_traces(text = inc_share_cols, textposition = "outside")
        st.plotly_chart(fig, use_container_width = True)
        st.write(avg_df)
        st.write("*Absolute values are in Millions(except for student numbers)")
else:
    with col2:
        st.subheader("Share")
            
        b = st.selectbox("Select from dropdown", ["Income", "Fees", "Admissions"])
        
        year = st.multiselect("Academic Year", filtered_df.index)
        if not year:
            filtered_df = filtered_df.copy()
        else:
            filtered_df = filtered_df[filtered_df.index.isin(year)]
           
        if b == "Income":
            inc_share_cols = ["Tuition fees and education contracts", "Funding body grants",
                            "Research grants and contracts", "Other income", "Investment income",
                            "Donations and endowments"]
        elif b == "Fees":
            inc_share_cols = ["Fees_UK", "Fees_international", "Fees_EU", "Fees_total_other"]
        else:
            inc_share_cols = ["UK_students", "EU_students", "Non-EU_students"]
            

        b_values = filtered_df[inc_share_cols].mean()
        avg_df = pd.DataFrame(b_values, columns=['Mean'])
        avg_df.index.names = ['Component']
            
        # Pie chart code:
        fig = px.pie(filtered_df, values = b_values, names = inc_share_cols, hole = 0.35)
        fig.update_layout(autosize=False, width=425, height=525)
        st.plotly_chart(fig, use_container_width = True)
        st.write(avg_df)
        st.write("*Absolute values are in Million(except for student numbers)")
        
if page_title == "****Comparison****":
    with col3:
        st.subheader("Share")
        b = st.selectbox("Select from dropdown", ["Income*", "Fees*", "Admissions*"])
        
        year = st.multiselect("Academic Year*", filtered_dff.index)
        if not year:
            filtered_dff = filtered_dff.copy()
        else:
            filtered_dff = filtered_dff[filtered_dff.index.isin(year)]
           
        if b == "Income*":
            inc_share_cols = ["Tuition fees and education contracts", "Funding body grants",
                            "Research grants and contracts", "Other income", "Investment income",
                            "Donations and endowments"]
        elif b == "Fees*":
            inc_share_cols = ["Fees_UK", "Fees_international", "Fees_EU", "Fees_total_other"]
        else:
            inc_share_cols = ["UK_students", "EU_students", "Non-EU_students"]
            
            
        b_values = filtered_dff[inc_share_cols].mean()
        avg_df = pd.DataFrame(b_values, columns=['Mean'])
        avg_df.index.names = ['Component']
            
        # Pie chart code:
        fig = px.pie(filtered_dff, values = b_values, names = inc_share_cols, hole = 0.35)
        fig.update_layout(autosize=False, width=425, height=525)
        st.plotly_chart(fig, use_container_width = True)
        st.write(avg_df)
        st.write("*Absolute values are in Million(except for student numbers)")
    
#%% Read Comments
COMMENT_TEMPLATE_MD = """{} - {}
> {}"""

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")
        

with st.expander("💬 Open comments"):

    # Show comments
    url_to_read='https://drive.google.com/file/d/10ALOh03E85scs7npWlgx8IfVAuxrlLYR/view?usp=sharing'
    url_to_read='https://drive.google.com/uc?id=' + url_to_read.split('/')[-2]
    all_comments = pd.read_csv(url_to_read)
    
    if all_comments["Page ID"].dtype != object:
        if page_title == "****Normal****":
            comments_df = all_comments[(all_comments["Page ID"] == 1) | (all_comments["Page ID"] == line_id)]
        else:
            comments_df = all_comments[(all_comments["Page ID"] == 2) | (all_comments["Page ID"] == line_id)]

    else:
        if page_title == "****Normal****":
            comments_df = all_comments[(all_comments["Page ID"] == '1') | (all_comments["Page ID"] == line_id)]
        else:
            comments_df = all_comments[(all_comments["Page ID"] == '2') | (all_comments["Page ID"] == line_id)]
    
    st.write("**Comments:**")
    
    comments_df.reset_index(drop = True, inplace = True)
    
    if len(comments_df["Name"]) == 0:
        st.write("No comments to show.")
    else:
        for index, row in comments_df.iterrows():
            st.markdown(COMMENT_TEMPLATE_MD.format(row["Date"], row["Name"], row["Comment"]))
            
            if st.button("Delete", key = row["Comment ID"]):
                row_index = all_comments[(all_comments['Page ID'] == row['Page ID']) &
                                         (all_comments['Comment ID'] == row['Comment ID'])].index
                all_comments.drop(row_index , inplace=True)
                all_comments.to_csv('Comments/Comments.csv', index = False)

                update_file('Comments/Comments.csv')
                st.experimental_rerun()
            
    space(2)

#%% Insert Comments
def clear_form():
    st.session_state["text1"] = ""
    st.session_state["text2"] = ""

st.write("**Add your comment**")
form = st.form("comment")
name = form.text_input("Name", key="text1")
comment = form.text_area("Comment", key="text2")

submit = form.form_submit_button("Add comment")
#clear = form.form_submit_button(label="Clear", on_click = clear_form)

if len(all_comments["Name"]) == 0:
    comment_id = 1
else:
    comment_id = max(all_comments['Comment ID']) + 1
    
if submit:
    if not name or not comment:
        st.write("One or more fields missing")
    else:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        new_row = [line_id,comment_id, name, date, comment]
        temp_df = {'Page ID': line_id, 'Comment ID': comment_id, 'Name': name, 'Date': date, 'Comment': comment}
        all_comments = all_comments._append(temp_df, ignore_index = True)
        all_comments.reset_index(drop = True, inplace = True)
        all_comments.to_csv('Comments/Comments.csv', index = False)

        update_file('Comments/Comments.csv')
        st.experimental_rerun()
