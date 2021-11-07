import pandas as pd

col_list = ['2016-Date', '2016-Daily-Flow','2019-Date', '2019-Daily-Flow','2020-Date', '2020-Daily-Flow']

ok = pd.read_excel(open("thames.xlsx", "rb"), sheet_name="Longreach", usecols=col_list)
sheet_names_object = pd.ExcelFile("thames.xlsx")
print(sheet_names_object.sheet_names)
print(ok["2016-Daily-Flow"].head().tolist())
cleaned_list = [i for i in ok["2016-Daily-Flow"].tolist() if pd.isna(i) is not True]