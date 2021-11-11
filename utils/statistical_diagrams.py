import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class diagrams:
    def __init__(self, sheet_name, year):
        self.sheet_name = sheet_name
        self.year = year
        self.col_list = ['2016-Date', '2016-Daily-Flow','2019-Date', '2019-Daily-Flow','2020-Date', '2020-Daily-Flow']

    def generate_boxplot(self):
        """Generates a boxplot from excel spreadsheet with given parameters.
        
        Returns:
            None

        """
        excel_object = pd.read_excel(open("thames.xlsx", "rb"), sheet_name=self.sheet_name, usecols=self.col_list)
        #This line also removes any NaN values from the list
        field_list = [i for i in excel_object[f"{self.year}-Daily-Flow"].tolist() if pd.isna(i) is not True]
        field_list.pop(0)
        cleaned_list = []

        #Removes any negative numbers from the list as they are errors.
        for i in field_list:
            if int(i) > 0:
                cleaned_list.append(i)

        plt.get_current_fig_manager().canvas.set_window_title('Boxplot')
        plt.title(f"Sheet name: {self.sheet_name} / Year: {self.year} - Daily flow boxplot")
        plt.boxplot(cleaned_list, vert=False)
        plt.show()

    def generate_all_boxplot(self):
        """Generates a boxplot from excel spreadsheet with given parameters.
        
        Returns:
            None

        """
        excel_object = pd.read_excel(open("thames.xlsx", "rb"), sheet_name=self.sheet_name, usecols=self.col_list)
        #This line also removes any NaN values from the list
        field_list = [i for i in excel_object[f"2016-Daily-Flow"].tolist() if pd.isna(i) is not True]
        field_list2 = [i for i in excel_object[f"2019-Daily-Flow"].tolist() if pd.isna(i) is not True]
        field_list3 = [i for i in excel_object[f"2020-Daily-Flow"].tolist() if pd.isna(i) is not True]
        field_list.pop(0)
        field_list2.pop(0)
        field_list3.pop(0)
        cleaned_list = []
        cleaned_list2 = []
        cleaned_list3 = []

        #Removes any negative numbers from the list as they are errors.
        for i in field_list:
            if int(i) > 0:
                cleaned_list.append(i)

        for i in field_list2:
            if int(i) > 0:
                cleaned_list2.append(i)

        for i in field_list3:
            if int(i) > 0:
                cleaned_list3.append(i)

        all_boxplots = [cleaned_list,cleaned_list2,cleaned_list3]

        plt.get_current_fig_manager().canvas.set_window_title('Boxplot')
        plt.title(f"Sheet name: {self.sheet_name} / All years 2016/2019/2020 - Daily flow boxplot")
        plt.boxplot(all_boxplots, vert=False)
        plt.show()

    def generate_list(self) -> list:
        """Displays list of column fields in thames.xlsx file

        Kwargs:
            sheet_name (string): The sheet name you want to extract data from.
            year (string): Year of data, currently available is 2016,2019,2020.        
        Returns:
            list : Returns a list of string column fields.
        """
        excel_object = pd.read_excel(open("thames.xlsx", "rb"), sheet_name= self.sheet_name, usecols=self.col_list)
        cleaned_list = [i for i in excel_object[f"{self.year}-Daily-Flow"].tolist() if pd.isna(i) is not True]
        cleaned_list.pop(0)
        return cleaned_list

    def generate_scatter_plot(self):
        """Generates a scatter plot diagram using matplotlib

        Returns:
            None
        """
        excel_object = pd.read_excel(open("thames.xlsx", "rb"), sheet_name= self.sheet_name, usecols=self.col_list)
        daily_flow_list = [i for i in excel_object[f"{self.year}-Daily-Flow"].tolist() if pd.isna(i) is not True]
        daily_flow_list.pop(0)
        
        date_list = [i for i in excel_object[f"{self.year}-Date"].tolist() if pd.isna(i) is not True]
        date_list.pop(0)

        x_axis = np.arange(len(daily_flow_list))
        plt.scatter(date_list, daily_flow_list)
        plt.gcf().autofmt_xdate()
        plt.show()



    @classmethod
    def sheet_name_list(cls) -> list:
        """Returns the list of sheet names in the thames.xlsx file

        Returns:
            List:str: List of sheet names (string data-type)
        """
        sheet_names_object = pd.ExcelFile("thames.xlsx")
        return sheet_names_object.sheet_names