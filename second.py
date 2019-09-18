# Make a simple Bokeh line graph

from bokeh.plotting import figure 
from bokeh.io import output_file, show
import pandas

#prepare some data
df = pandas.read_csv('data.csv')
x = df['x']
y = df['y']

#prepare the output file

output_file('Line_from_csv.html')

#Create a figure object
f = figure()

#Create line plot

f.line(x,y)

show(f)