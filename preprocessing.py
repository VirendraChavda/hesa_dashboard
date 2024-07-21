#%% Data preprocessing
import numpy as np
import pandas as pd
import pip

try:
    import openpyxl
except:
    pip.main(['install', 'openpyxl'])
    import openpyxl

main_raw = pd.read_excel('University Benchmarking Dashboard - Formatted.xlsx', 'HE Dataset', header = 4)
main_raw.drop("Unnamed: 0", inplace = True, axis = 1)
main_raw = main_raw[main_raw['University'].notna()]

main_raw.reset_index(drop = True, inplace = True)


discard = ["Year"]
main = main_raw[~main_raw["University"].str.contains(' '.join(discard))]
 
main.reset_index(drop = True, inplace = True)


for cols in main.columns:
    if "Unnamed" in cols:
        main.drop(cols, axis = 1, inplace = True)
        
groups = pd.read_excel('University Benchmarking Dashboard - Formatted.xlsx', 'Grouping', header = 1)
#groups.dropna(axis=1, how='all', inplace = True)

#%% Grouping as per association

Russell = []
for i in range(len(groups["Russell Group"])):
    if type(groups["Russell Group"][i]) == str:
        Russell.append(groups["Russell Group"][i])
        
Post_1992_poly_roots = []
for i in range(len(groups["Post 1992 with Polytechnic roots"])):
    if type(groups["Post 1992 with Polytechnic roots"][i]) == str:
        Post_1992_poly_roots.append(groups["Post 1992 with Polytechnic roots"][i])

Post_1992_central_inst_roots = []
for i in range(len(groups["Post 1992 with Central Institution Roots"])):
    if type(groups["Post 1992 with Central Institution Roots"][i]) == str:
        Post_1992_central_inst_roots.append(groups["Post 1992 with Central Institution Roots"][i])
        
Post_1992_other = []
for i in range(len(groups["Post 1992 - Other"])):
    if type(groups["Post 1992 - Other"][i]) == str:
        Post_1992_other.append(groups["Post 1992 - Other"][i])
        
#%% Grouping as per establishment

ancient = []
for i in range(len(groups["Ancient Universities"])):
    if type(groups["Ancient Universities"][i]) == str:
        ancient.append(groups["Ancient Universities"][i])
        
red_brick = []
for i in range(len(groups["Red brick Universities"])):
    if type(groups["Red brick Universities"][i]) == str:
        red_brick.append(groups["Red brick Universities"][i])
        
glass_plate = []
for i in range(len(groups["Plate Glass"])):
    if type(groups["Plate Glass"][i]) == str:
        glass_plate.append(groups["Plate Glass"][i])
        
post_1992_all = []
for i in range(len(groups["Post 1992 All"])):
    if type(groups["Post 1992 All"][i]) == str:
        post_1992_all.append(groups["Post 1992 All"][i])
        
#%% Grouping as per location

in_london = []
for i in range(len(groups["London Subset"])):
    if type(groups["London Subset"][i]) == str:
        in_london.append(groups["London Subset"][i])
        
#%% Grouping as per funds

private = []
for i in range(len(groups["Private Placement"])):
    if type(groups["Private Placement"][i]) == str:
        private.append(groups["Private Placement"][i])
        
public = []
for i in range(len(groups["Public Bond"])):
    if type(groups["Public Bond"][i]) == str:
        public.append(groups["Public Bond"][i])
        
#%% Adding groups to in dataset
# As per association

main['Association'] = 'Other'

for i in range(len(main.index)):
    if main["University"][i] in Russell:
        main['Association'][i] = "Russell Group"
    elif main["University"][i] in Post_1992_poly_roots:
        main['Association'][i] = "Post 1992 with polytechnic roots"
    elif main["University"][i] in Post_1992_central_inst_roots:
        main['Association'][i] = "Post 1992 with central institution roots"
    elif main["University"][i] in Post_1992_other:
        main['Association'][i] = "Post 1992 - other"
    else:
        pass

# As per establishment

main['Established'] = 'Other'

for i in range(len(main.index)):
    if main["University"][i] in ancient:
        main['Established'][i] = "Ancient(pre 1860)"
    elif main["University"][i] in red_brick:
        main['Established'][i] = "Red Brick(1860-1960)"
    elif main["University"][i] in glass_plate:
        main['Established'][i] = "Glass Plate(1960-1992)"
    elif main["University"][i] in post_1992_all:
        main['Established'][i] = "Post 1992 - All"
    else:
        pass
    
# As per location

main['Location'] = 'Other'

for i in range(len(main.index)):
    if main["University"][i] in in_london:
        main['Location'][i] = "London"
    else:
        pass
    
# As per funds

main['Funding'] = 'Other'

for i in range(len(main.index)):
    if main["University"][i] in private:
        main['Funding'][i] = "Private Placement"
    elif main["University"][i] in public:
        main['Funding'][i] = "Public Bonds"
    else:
        pass
        
#%% Column creation
cash_cols = ["University", "Country", "Academic Year", "Total Income", "Total Expenditure", "Operating surplus/ (deficit)",
            "Tuition fees and education contracts", "Funding body grants", "Research grants and contracts",
            "Other income", "Investment income", "Donations and endowments", "UK", "International",
             "EU", "Other (Research)", "Other (Non-Credit Bearing Course Fees)", "Other - FE Course Fees",
             "Total Other", "Staff Costs", "Staff Costs / Total Expenditure", 
             "Total UK  ", "European Union", "Non-European Union", "Total", "Association", 
             "Established", "Location", "Funding", "Times Ranking 2023"]

sub_main = main[cash_cols]

sub_main.rename(columns={"Operating surplus/ (deficit)": "Surplus/Deficit", "UK": "Fees_UK",
                         "International": "Fees_international", "EU": "Fees_EU", "Other (Research)": "Fees_research/other",
                         "Other (Non-Credit Bearing Course Fees)": "Fees_non_credit_bearing_courses/other",
                         "Other - FE Course Fees": "Fees_FE_course/other", "Other - FE Course Fees" : "Fees_FE_courses/other",
                         "Total Other" : "Fees_total_other", "Total UK  ": "UK_students", "European Union": "EU_students",
                         "Non-European Union": "Non-EU_students", "Total": "Total_students"}, inplace = True)

sub_main["UK_fps"] =  sub_main["Fees_UK"]/sub_main["UK_students"]
sub_main["EU_fps"] =  sub_main["Fees_EU"]/sub_main["EU_students"]
sub_main["Non-EU_fps"] =  sub_main["Fees_international"]/sub_main["Non-EU_students"]

#%% Data Scaling

columns_to_scale = ["Total Income", "Total Expenditure", "Surplus/Deficit", "Tuition fees and education contracts",
                    "Funding body grants", "Research grants and contracts", "Other income", "Investment income",
                    "Donations and endowments", "Fees_UK", "Fees_international", "Fees_EU", "Fees_research/other",
                    "Fees_non_credit_bearing_courses/other", "Fees_FE_courses/other", "Fees_total_other", "Staff Costs"]

sub_main[columns_to_scale] = sub_main[columns_to_scale]/1000000

sub_main = sub_main[sub_main["Academic Year"] != "2015/16"]

#%% Details from website

sheet = pd.read_excel('University Benchmarking Dashboard - Formatted.xlsx', 'More details', header = 0)
sheet.dropna(axis=1, how='all', inplace = True)

sub_main["Courses_type"] = ""
sub_main["County"] = ""
sub_main["Region"] = ""
sub_main["Accomodation"] = ""

for i in range(len(sub_main.index)):
    for j in range(len(sheet.index)):
        if sub_main["University"][i] == sheet["Name of the University"][j]:
            sub_main["Courses_type"][i] = sheet["Courses_type"][j]
            sub_main["County"][i] = sheet["County"][j]
            sub_main["Region"][i] = sheet["Region"][j]
            sub_main["Accomodation"][i] = sheet["Accomodation"][j]
            
sub_main = sub_main[(sub_main["Total Income"] != 0)]
sub_main = sub_main[sub_main["University"] != "Heriot-Watt University"]
sub_main.reset_index(drop = True, inplace = True)   
            
#%% Creating income group

sub_main_latest = sub_main[sub_main["Academic Year"] == "2021/22"]
sub_main_latest.reset_index(drop = True, inplace = True)

sub_main_latest["Income_group"] = ""

for i in range(len(sub_main_latest.index)):
    if sub_main_latest["Total Income"][i] > 1500:
        sub_main_latest["Income_group"][i] = "> 1500 millions"
    elif sub_main_latest["Total Income"][i] < 1500 and sub_main_latest["Total Income"][i] > 1000:
        sub_main_latest["Income_group"][i] = "1000-1500 millions"
    elif sub_main_latest["Total Income"][i] < 1000 and sub_main_latest["Total Income"][i] > 750:
        sub_main_latest["Income_group"][i] = "750-1000 millions"
    elif sub_main_latest["Total Income"][i] < 750 and sub_main_latest["Total Income"][i] > 500:
        sub_main_latest["Income_group"][i] = "500-750 millions"
    elif sub_main_latest["Total Income"][i] < 500 and sub_main_latest["Total Income"][i] > 400:
        sub_main_latest["Income_group"][i] = "400-500 millions"
    elif sub_main_latest["Total Income"][i] < 400 and sub_main_latest["Total Income"][i] > 300:
        sub_main_latest["Income_group"][i] = "300-400 millions"
    elif sub_main_latest["Total Income"][i] < 300 and sub_main_latest["Total Income"][i] > 200:
        sub_main_latest["Income_group"][i] = "200-400 millions"
    elif sub_main_latest["Total Income"][i] < 200 and sub_main_latest["Total Income"][i] > 100:
        sub_main_latest["Income_group"][i] = "100-200 millions"
    elif sub_main_latest["Total Income"][i] < 100:
        sub_main_latest["Income_group"][i] = "< 100 millions"
            
#%% Creating university size

sub_main_latest["Uni_size"] = ""

for i in range(len(sub_main_latest.index)):
    if sub_main_latest["Total_students"][i] > 50000:
        sub_main_latest["Uni_size"][i] = "> 50k students"
    elif sub_main_latest["Total_students"][i] < 50000 and sub_main_latest["Total_students"][i] > 40000:
        sub_main_latest["Uni_size"][i] = "40k-50k students"
    elif sub_main_latest["Total_students"][i] < 40000 and sub_main_latest["Total_students"][i] > 30000:
        sub_main_latest["Uni_size"][i] = "30k-40k students"
    elif sub_main_latest["Total_students"][i] < 30000 and sub_main_latest["Total_students"][i] > 20000:
        sub_main_latest["Uni_size"][i] = "20k-30k students"
    elif sub_main_latest["Total_students"][i] < 20000 and sub_main_latest["Total_students"][i] > 15000:
        sub_main_latest["Uni_size"][i] = "15k-20k students"
    elif sub_main_latest["Total_students"][i] < 15000 and sub_main_latest["Total_students"][i] > 10000:
        sub_main_latest["Uni_size"][i] = "10k-15k students"
    elif sub_main_latest["Total_students"][i] < 10000 and sub_main_latest["Total_students"][i] > 5000:
        sub_main_latest["Uni_size"][i] = "5k-10k students"
    elif sub_main_latest["Total_students"][i] < 5000 and sub_main_latest["Total_students"][i] > 1000:
        sub_main_latest["Uni_size"][i] = "1k-5k students"
    elif sub_main_latest["Total_students"][i] < 1000:
        sub_main_latest["Uni_size"][i] = "< 1k students"
        
sub_main["Income_group"] = ""
sub_main["Uni_size"] = ""

for i in range(len(sub_main.index)):
    for j in range(len(sub_main_latest.index)):
        if sub_main["University"][i] == sub_main_latest["University"][j]:
            sub_main["Income_group"][i] = sub_main_latest["Income_group"][j]
            sub_main["Uni_size"][i] = sub_main_latest["Uni_size"][j]

#%% Creating ranking group
rank_df = sub_main[sub_main["Academic Year"] == "2022/23"][["University", "Times Ranking 2023"]]
rank_df.sort_values("Times Ranking 2023")

rank_df["Rank_group"] = ""

for i in range(len(rank_df.index)):
    if rank_df["Times Ranking 2023"][i] < 6 and rank_df["Times Ranking 2023"][i] > 0:
        rank_df["Rank_group"][i] = "Rank 1-5"
    elif rank_df["Times Ranking 2023"][i] < 11 and rank_df["Times Ranking 2023"][i] > 5:
        rank_df["Rank_group"][i] = "Rank 6-10"
    elif rank_df["Times Ranking 2023"][i] < 21 and rank_df["Times Ranking 2023"][i] > 10:
        rank_df["Rank_group"][i] = "Rank 11-20"
    elif rank_df["Times Ranking 2023"][i] < 31 and rank_df["Times Ranking 2023"][i] > 20:
        rank_df["Rank_group"][i] = "Rank 21-30"
    elif rank_df["Times Ranking 2023"][i] < 41 and rank_df["Times Ranking 2023"][i] > 30:
        rank_df["Rank_group"][i] = "Rank 31-40"
    elif rank_df["Times Ranking 2023"][i] < 51 and rank_df["Times Ranking 2023"][i] > 40:
        rank_df["Rank_group"][i] = "Rank 41-50"
    elif rank_df["Times Ranking 2023"][i] < 76 and rank_df["Times Ranking 2023"][i] > 50:
        rank_df["Rank_group"][i] = "Rank 50-75"
    elif rank_df["Times Ranking 2023"][i] < 101 and rank_df["Times Ranking 2023"][i] > 75:
        rank_df["Rank_group"][i] = "Rank 76-100"
    elif rank_df["Times Ranking 2023"][i] > 100:
        rank_df["Rank_group"][i] = "Rank above 100"
    else:
        rank_df["Rank_group"][i] = "Unranked"

sub_main["Rank_group"] = ""


for i in range(len(sub_main.index)):
    for j in range(len(rank_df.index)):
        if sub_main["University"][i] == rank_df["University"][j]:
            sub_main["Rank_group"][i] = rank_df["Rank_group"][j]

for i in range(len(sub_main.index)):
    if sub_main["Rank_group"][i] == '':
        sub_main["Rank_group"][i] = "Unranked"
        
sub_main.replace(np.inf, 0, inplace = True)
sub_main.drop('Times Ranking 2023', axis=1, inplace=True)

#%% Saving csv

sub_main.to_csv("Data/updated.csv")





