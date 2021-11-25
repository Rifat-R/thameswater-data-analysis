import pandas as pd
import numpy as np
from utils import statistical_diagrams as diagram
import matplotlib.pyplot as plt
from tkinter import *

root = Tk()
root.title("Thames water data analysis")
# root.geometry("200x200")


#All matplotlib functions-----------
def boxplot():
    diagram.diagrams(sheet_name_clicked.get(),year_clicked.get()).generate_boxplot()

def all_boxplots():
    diagram.diagrams(sheet_name_clicked.get(),year_clicked.get()).generate_all_boxplot()

def stats():
    rounded_mean_2016 = str(round(np.mean(diagram.diagrams(sheet_name_clicked.get(),"2016").generate_list())))
    rounded_median_2016 = str(round(np.median(diagram.diagrams(sheet_name_clicked.get(),"2016").generate_list())))
    rounded_range_2016 = str(round(np.ptp(diagram.diagrams(sheet_name_clicked.get(),"2016").generate_list())))

    rounded_mean_2019 = str(round(np.mean(diagram.diagrams(sheet_name_clicked.get(),"2019").generate_list())))
    rounded_median_2019 = str(round(np.median(diagram.diagrams(sheet_name_clicked.get(),"2019").generate_list())))
    rounded_range_2019 = str(round(np.ptp(diagram.diagrams(sheet_name_clicked.get(),"2019").generate_list())))

    rounded_mean_2020 = str(round(np.mean(diagram.diagrams(sheet_name_clicked.get(),"2020").generate_list())))
    rounded_median_2020 = str(round(np.median(diagram.diagrams(sheet_name_clicked.get(),"2020").generate_list())))
    rounded_range_2020 = str(round(np.ptp(diagram.diagrams(sheet_name_clicked.get(),"2020").generate_list())))

    mean_label_2016.config(text=f"Mean: {rounded_mean_2016}")
    median_label_2016.config(text=f"Median: {rounded_median_2016}")
    range_label_2016.config(text=f"Range: {rounded_range_2016}")

    mean_label_2019.config(text=f"Mean: {rounded_mean_2019}")
    median_label_2019.config(text=f"Median: {rounded_median_2019}")
    range_label_2019.config(text=f"Range: {rounded_range_2019}")

    mean_label_2020.config(text=f"Mean: {rounded_mean_2020}")
    median_label_2020.config(text=f"Median: {rounded_median_2020}")
    range_label_2020.config(text=f"Range: {rounded_range_2020}")

def scatter_plot():
    sheet_name = sheet_name_clicked.get()
    year = year_clicked.get()
    diagram.diagrams(sheet_name,year).generate_scatter_plot()

sheet_names:list = diagram.diagrams.sheet_name_list()
year_list:list = ["2016","2019","2020"]

#All StringVar() variables-----------
sheet_name_clicked = StringVar()
sheet_name_clicked.set("Select a sheet name")

year_clicked = StringVar()
year_clicked.set("Select a year")


#All dropdowns---------------
sheet_name_drop = OptionMenu(root, sheet_name_clicked, *sheet_names)
sheet_name_drop.grid(row=0,column=0)

year_drop = OptionMenu(root, year_clicked, *year_list)
year_drop.grid(row=1,column=0)


#All buttons --------------
boxplot_button = Button(root, text="Create boxplot!", command=boxplot)
boxplot_button.grid(row=2,column=0)

all_boxplot_button = Button(root, text="Create all boxplots!", command=all_boxplots)
all_boxplot_button.grid(row=3,column=0)

scatter_button = Button(root, text="Create scatter graph", command=scatter_plot)
scatter_button.grid(row=4,column=0)

stats_button = Button(root, text="Generate stats", command=stats)
stats_button.grid(row=5,column=0)


#STATS Labels -------------
label_title_2016 = Label(root, text="2016")
label_title_2016.grid(row=0,column=1,padx=(50,10))

mean_label_2016 = Label(root, text="Mean:")
mean_label_2016.grid(row=1,column=1,padx=(50,10))

median_label_2016 = Label(root, text="Median:")
median_label_2016.grid(row=2,column=1,padx=(50,10))

range_label_2016 = Label(root, text="Range:")
range_label_2016.grid(row=3,column=1,padx=(50,10))

#2019
label_title_2019 = Label(root, text="2019")
label_title_2019.grid(row=0,column=2,padx=(50,10))

mean_label_2019 = Label(root, text="Mean:")
mean_label_2019.grid(row=1,column=2,padx=(50,10))

median_label_2019 = Label(root, text="Median:")
median_label_2019.grid(row=2,column=2,padx=(50,10))

range_label_2019 = Label(root, text="Range:")
range_label_2019.grid(row=3,column=2,padx=(50,10))

#2020
label_title_2020 = Label(root, text="2020")
label_title_2020.grid(row=0,column=3,padx=(50,10))

mean_label_2020 = Label(root, text="Mean:")
mean_label_2020.grid(row=1,column=3,padx=(50,10))

median_label_2020 = Label(root, text="Median:")
median_label_2020.grid(row=2,column=3,padx=(50,10))

range_label_2020 = Label(root, text="Range:")
range_label_2020.grid(row=3,column=3,padx=(50,10))

root.mainloop()


