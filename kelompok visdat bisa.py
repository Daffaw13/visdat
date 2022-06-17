import pandas as pd

from bokeh.plotting import figure, show
from bokeh.io import output_file, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models.widgets import Tabs, Panel

df = pd.read_csv("data/stock_market.csv") 
df

"""# Level 1

visualisasi data interaktif untuk menampilkan nilai “Adj Close” untuk setiap indeks 
pasar saham. Aspek interaktif minimum yang harus dimunculkan adalah 
1. default toolbar
dan
2. hover. 
---
Teks yang muncul pada saat kursor diletakkan di atas titik data adalah 
1.  nama 
indeks pasar saham, dan 
2. nilai parameter.
"""

condition1 = (df['Name'] == 'HANG SENG') | (df['Name'] == 'NASDAQ') | (df['Name']== 'NIKKEI')
df1 = df[condition1]
df1 = df1.loc[:, ['Date', 'Adj Close', 'Name']]
df1 = df1.sort_values(['Name','Date'])
df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d')
df1.head()

# Output to file
output_notebook()

hang1 = df1[df1['Name'] == 'HANG SENG']
nas1 = df1[df1['Name'] == 'NASDAQ']
nik1 = df1[df1['Name'] == 'NIKKEI']

# Menyimpan data pada ColumnDataSource
hang_cds1 = ColumnDataSource(hang1)
nas_cds1 = ColumnDataSource(nas1)
nik_cds1 = ColumnDataSource(nik1)

# Configure the figure
fig1 = figure(x_axis_type='datetime',
             plot_height=550, plot_width=1100,
             title='Nilai “Adj Close” untuk setiap indeks pasar saham pada Dataset Stock Market',
             x_axis_label='Date', y_axis_label='Value=Adj Close')

# Render the race as step lines
hangseng1 = fig1.line('Date', 'Adj Close', 
         color='blue', legend_label='HANG SENG', 
         source=hang_cds1)
nasdaq1 = fig1.line('Date', 'Adj Close', 
         color='red', legend_label='NASDAQ', 
         source=nas_cds1)
nikkei1 = fig1.line('Date', 'Adj Close', 
         color='green', legend_label='NIKKEI', 
         source=nik_cds1)


tooltips = [
            ('Name','@Name'),
            ('Value', '@{Adj Close}')
           ]
           
fig1.add_tools(HoverTool(tooltips=tooltips,renderers=[hangseng1]))
fig1.add_tools(HoverTool(tooltips=tooltips,renderers=[nasdaq1]))
fig1.add_tools(HoverTool(tooltips=tooltips,renderers=[nikkei1]))

# Meletakkan legend di atas kanan
fig1.legend.location = 'top_right'


# Show the plot
show(fig1)

"""# Level 2

semua instruksi pada kasus level 1. Ditambahkan aspek interaktif yang 
memungkinkan user memilih parameter yang akan ditampilkan: 
1.  Adj Close, 
2.  Volume,
3. Day_Perc_Change. 
---
Nilai parameter yang muncul pada hover tool harus disesuaikan dengan 
parameter yang dipilih
"""

condition2 = (df['Name'] == 'HANG SENG') | (df['Name'] == 'NASDAQ') | (df['Name']== 'NIKKEI')
df2 = df[condition2]
df2 = df2.loc[:, ['Date', 'Volume', 'Name']]
df2 = df2.sort_values(['Name','Date'])
df2['Date'] = pd.to_datetime(df2['Date'], format='%Y-%m-%d')
df2.head()

# Output to file
output_notebook()

hang2 = df2[df2['Name'] == 'HANG SENG']
nas2 = df2[df2['Name'] == 'NASDAQ']
nik2 = df2[df2['Name'] == 'NIKKEI']

# Store the data in a ColumnDataSource
hang_cds2 = ColumnDataSource(hang2)
nas_cds2 = ColumnDataSource(nas2)
nik_cds2 = ColumnDataSource(nik2)

# Configure the figure
fig2 = figure(x_axis_type='datetime',
             plot_height=550, plot_width=1100,
             title='Volume pada dataset Stock Market',
             x_axis_label='Date', y_axis_label='Value=Volume')

# Render the race as step lines
hangseng2 = fig2.line('Date', 'Volume', 
         color='blue', legend_label='HANG SENG', 
         source=hang_cds2)
nasdaq2 = fig2.line('Date', 'Volume', 
         color='red', legend_label='NASDAQ', 
         source=nas_cds2)
nikkei2 = fig2.line('Date', 'Volume', 
         color='green', legend_label='NIKKEI', 
         source=nik_cds2)


tooltips = [
            ('Name','@Name'),
            ('Value', '@{Volume}')
           ]
           
fig2.add_tools(HoverTool(tooltips=tooltips,renderers=[hangseng2]))
fig2.add_tools(HoverTool(tooltips=tooltips,renderers=[nasdaq2]))
fig2.add_tools(HoverTool(tooltips=tooltips,renderers=[nikkei2]))

# Move the legend to the upper right corner
fig2.legend.location = 'top_right'

# Show the plot
show(fig2)

"""# Level 3"""

condition3 = (df['Name'] == 'HANG SENG') | (df['Name'] == 'NASDAQ') | (df['Name']== 'NIKKEI')
df3 = df[condition3]
df3 = df3.loc[:, ['Date', 'Day_Perc_Change', 'Name']]
df3 = df3.sort_values(['Name','Date'])
df3['Date'] = pd.to_datetime(df3['Date'], format='%Y-%m-%d')

# Output to file
output_notebook()

hang3 = df3[df3['Name'] == 'HANG SENG']
nas3 = df3[df3['Name'] == 'NASDAQ']
nik3 = df3[df3['Name'] == 'NIKKEI']

# Store the data in a ColumnDataSource
hang_cds3 = ColumnDataSource(hang3)
nas_cds3 = ColumnDataSource(nas3)
nik_cds3 = ColumnDataSource(nik3)

# Configure the figure
fig3 = figure(x_axis_type='datetime',
             plot_height=550, plot_width=1100,
             title='Day_Perc_Change pada dataset Stock Market',
             x_axis_label='Date', y_axis_label='Day_Perc_Change')

# Render the race as step lines
hangseng3 = fig3.line('Date', 'Day_Perc_Change', 
         color='blue', legend_label='HANG SENG', 
         source=hang_cds3)
nasdaq3 = fig3.line('Date', 'Day_Perc_Change', 
         color='red', legend_label='NASDAQ', 
         source=nas_cds3)
nikkei3 = fig3.line('Date', 'Day_Perc_Change', 
         color='green', legend_label='NIKKEI', 
         source=nik_cds3)


tooltips = [
            ('Name','@Name'),
            ('Value', '@{Day_Perc_Change}')
           ]
           
fig3.add_tools(HoverTool(tooltips=tooltips,renderers=[hangseng3]))
fig3.add_tools(HoverTool(tooltips=tooltips,renderers=[nasdaq3]))
fig3.add_tools(HoverTool(tooltips=tooltips,renderers=[nikkei3]))

# Move the legend to the upper left corner
fig3.legend.location = 'top_right'
fig3.legend.click_policy="hide"

# Show the plot
show(fig3)

#Menambah widget panel  dan tabx

adj_panel = Panel(child=fig1, title='Adj Close')
volume_panel = Panel(child=fig2, title='Volume')
day_panel = Panel(child=fig3, title='Day_Perc_Change')

tabs = Tabs(tabs=[adj_panel, volume_panel,day_panel])

# Show tabs
show(tabs)
