# import pdfplumber
# with pdfplumber.open(r"c:\Users\HP\Downloads\ASER-2023-Report-1-beyond basics.pdf") as pdf:
#     for page_num in range(80,189):
#         text= pdf.pages[page_num].extract_text()
#         print(f"---Page {page_num +1}:---")
#         print(text[150:450])
#         print("--")

# import pdfplumber
# import pandas as pd

# with pdfplumber.open(r"C:\Users\HP\Downloads\ASER_2024_Final-Report_13_2_24-1.pdf") as pdf:
#     page = pdf.pages[68] 
#     tables= page.extract_text()
#     print("Number of tables found:", len(tables))
#     if tables: 
#         for row in tables[0][:5]:
#             print(row)

# states=["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
#     "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
#     "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Meghalaya",
#     "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
#     "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
#     "West Bengal"]


# with pdfplumber.open(r"C:\Users\HP\Downloads\ASER_2024_Final-Report_13_2_24-1.pdf") as pdf:
#      text = pdf.pages[68].extract_text()

# data=[]
# for line in text.split('\n'):
#      for state in states:
#           if line.startswith(state):
#                numbers=line.replace(state,' ').split()
#                if len(numbers)>=24:
#                     data.append({
#                          'State': state,
#                          'Std_V_Reading_2024': float(numbers[17]),
#                          'Std_VIII_Reading_2024': float(numbers[20]),
#                          'Std_VIII_Arthmetic_2024': float(numbers[23])
#                     })
# df= pd.DataFrame(data)
# print(df)

# import pdfplumber

# with pdfplumber.open(r"c:\Users\HP\Downloads\ASER-2023-Report-1-beyond basics.pdf") as pdf:
#     for page_num in range(80, 89):
#         text = pdf.pages[page_num].extract_text()
#         # if text and "state" in text.lower() and "%" in text:
#         print(f"--- Page {page_num + 1} ---")
#         print(text[:500])
#         print()

import pdfplumber
import pandas as pd

with pdfplumber.open(r"D:\work\1st research project\ASER-2023-Report-1-beyond basics.pdf") as pdf:
    text=pdf.pages[81].extract_text()

data=[]
for line in text.split('\n'):
    if ':' in line and any(char.isdigit() for char in line):
        parts=line.split(' ')
        state_district=[]
        numbers=[]
        for part in parts:
            try:
                numbers.append(float(part))
            except ValueError:
                if not numbers:
                    state_district.append(part)
        if numbers and len(numbers)>=2:
            state=' '.join(state_district).split(':')[0].strip()
            data.append({
                'State':state,
                'Reading_%':numbers[0],
                'Division_%':numbers[1],
                'Applied_Reading_%': numbers[8],
                'Unitary_Method_%': numbers[7]
            })
df=pd.DataFrame(data)


# for line in text.split('\n'):
#     if 'Andhra' in line:
#         print(repr(line))

    # for page_num in range(78,88):
    #     text=pdf.pages[page_num].extract_text()
    #     if text:
    #         print(f"PDF index{page_num} → {text[:200]}")
    #         print()

df_clean=df.groupby('State').agg({
    'Reading_%':'mean',
    'Division_%':'mean',
    'Applied_Reading_%': 'mean',
    'Unitary_Method_%': 'mean'
}).reset_index()
print(df_clean)
print(f'\nToatal States:{len(df_clean)}')
# df_clean.to_csv(r"c:\Users\HP\Downloads\aser_learning_2023.csv",index=False)
# print("Saved Successfully")
import pandas as pd
df_data= pd.read_csv(r"D:\work\1st research project\final_merged_data.csv")
print("Revise!!!!")
print(df_data.head())
print(df_data.columns)


s=df_data.sort_values('Applied_Reading_%', ascending=False)
result=s[['State','Applied_Reading_%']]
print(result.head(3))


import pandas as pd
df= pd.read_csv(r"D:\work\1st research project\final_merged_data.csv")
print("WPR Here on")
rural_male_WPR=df['Applied_Reading_%'].corr(df['Rural_Male_WPR'])
print("Correlation between Applied reading and rural male wpr is",rural_male_WPR)
rural_female_WPR=df['Applied_Reading_%'].corr(df['Rural_Female_WPR'])
print("Correlation between Applied reading and rural female wpr is: ", rural_female_WPR)
rural_total_WPR=df['Applied_Reading_%'].corr(df['Rural_Person_WPR'])
print("Correlation between Applied reading and rural total wpr is: ", rural_total_WPR)
print("LFPR Here on")
rural_male_LFPR=df['Applied_Reading_%'].corr(df['Rural_Male_LFPR'])
print("Correlation between Applied reading and rural male lfpr is: ", rural_male_LFPR)
rural_female=df['Applied_Reading_%'].corr(df['Rural_Female_LFPR'])
print("Correlation between Applied reading and rural female lfpr is: ", rural_female)
rural_total_LFPR=df['Applied_Reading_%'].corr(df['Rural_Person_LFPR'])
print("Correlation between Applied reading and rural total lfpr is: ", rural_total_LFPR)
print("UR Here on")
rural_male_UR=df['Applied_Reading_%'].corr(df['Rural_Male_UR'])
print("Correlation between Applied reading and rural male UR is: ", rural_male_UR)
rural_female_UR=df['Applied_Reading_%'].corr(df['Rural_Female_UR'])
print("Correlation between Applied reading and rural female UR is: ", rural_female_UR)
rural_total_UR=df['Applied_Reading_%'].corr(df['Rural_Person_UR'])
print("Correlation between Applied reading and rural total UR is: ", rural_total_UR)







