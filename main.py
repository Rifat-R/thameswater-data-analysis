import pandas as pd
import numpy as np
from utils import statistical_diagrams as diagram
import matplotlib.pyplot as plt
from tkinter import *

root = Tk()
root.title("Boxplot")
root.geometry("200x200")
h1 = diagram.diagrams("Riverside","2016")

def boxplot():
    diagram.diagrams(sheet_name_clicked.get(),year_clicked.get()).generate_boxplot()

def stats():
    rounded_mean = str(round(np.mean(diagram.diagrams(sheet_name_clicked.get(),year_clicked.get()).generate_list())))
    rounded_median = str(round(np.median(diagram.diagrams(sheet_name_clicked.get(),year_clicked.get()).generate_list())))
    rounded_range = str(round(np.ptp(diagram.diagrams(sheet_name_clicked.get(),year_clicked.get()).generate_list())))

    mean_label.config(text=f"Mean: {rounded_mean}")
    median_label.config(text=f"Median: {rounded_median}")
    range_label.config(text=f"Range: {rounded_range}")


sheet_name_clicked = StringVar()
sheet_name_clicked.set("Select a sheet name")

year_clicked = StringVar()
year_clicked.set("Select a year")

mean_text = StringVar()
mean_text.set("Bogos")

sheet_names:list = diagram.diagrams.sheet_name_list()
year_list:list = ["2016","2019","2020"]

drop = OptionMenu(root , sheet_name_clicked , *sheet_names)
drop.pack()

drop2 = OptionMenu(root , year_clicked , *year_list)
drop2.pack()

boxplot_button = Button(root, text="Create boxplot!", command=boxplot)
boxplot_button.pack()
stats_button = Button(root, text="Generate stats", command=stats)
stats_button.pack()

mean_label = Label(root, text="Mean:")
mean_label.pack()

median_label = Label(root, text="Median:")
median_label.pack()

range_label = Label(root, text="Range:")
range_label.pack()


root.mainloop()


