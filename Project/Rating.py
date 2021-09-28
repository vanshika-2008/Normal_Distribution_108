import csv
import plotly.figure_factory as pxfig
import pandas as pds

df = pds.read_csv('Project/data.csv')
plot = pxfig.create_distplot([df['Avg Rating'].tolist()],["Mobile Brands' Avg. Rating on Amazon"],show_hist=False)
plot.show()