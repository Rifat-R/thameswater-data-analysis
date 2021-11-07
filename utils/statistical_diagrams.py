import matplotlib.pyplot as plt
import pandas as pd

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

    def generate_list(self) -> list:
        """Displays list of column fields in thames.xlsx file

        Kwargs:
            sheet_name (string): The sheet name you want to extract data from.
            year (string): Year of data, currently available is 2016,2019,2020.        
        Returns:
            list : Returns a list of string column fields.
        """
        excel_object = pd.read_excel(open("thames.xlsx", "rb"), sheet_name= self.sheet_name, usecols= self.col_list)
        cleaned_list = [i for i in excel_object[f"{self.year}-Daily-Flow"].tolist() if pd.isna(i) is not True]
        cleaned_list.pop(0)
        return cleaned_list

    @classmethod
    def sheet_name_list(cls) -> list:
        """Returns the list of sheet names in the thames.xlsx file

        Returns:
            List:str: List of sheet names (string data-type)
        """
        sheet_names_object = pd.ExcelFile("thames.xlsx")
        return sheet_names_object.sheet_names