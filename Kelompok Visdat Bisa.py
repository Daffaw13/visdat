# Import library
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, Select
from bokeh.layouts import row, column
from bokeh.io import output_notebook
output_notebook()

# Membaca Dataset
data_market = pd.read_csv('stock_market.csv')
data_market.head()

# Merubah nama kolom Adj Close menjadi Adj_Close
data_market.rename(columns = {'Adj Close':'Adj_Close'}, inplace = True)
data_market.head()

# Merubah format type kolom date
data_market['Date'] = pd.to_datetime(data_market['Date'])
data_market.dtypes

# Membuat variabel untuk perusahaan HANG SENG
df_hangseng = pd.DataFrame(data_market[data_market["Name"] == 'HANG SENG'])
df_hangseng.head()

# Membuat variabel untuk perusahaan NASDAQ
df_nasdaq = pd.DataFrame(data_market[data_market["Name"] == 'NASDAQ'])
df_nasdaq.head()

# Membuat variabel untuk perusahaan NIKKEI
df_nikkei = pd.DataFrame(data_market[data_market["Name"] == 'NIKKEI'])
df_nikkei.head()

# Menyimpan data pada ColumnDataSource
source_hangseng = ColumnDataSource(df_hangseng)
source_nasdaq = ColumnDataSource(df_nasdaq)
source_nikkei = ColumnDataSource(df_nikkei)

# Membuat file Output berbentun html
output_file('Hasil Analisis Adj Close.html', title='Adj Close Pasar Saham')

# Membuat tooltips dan hover
tooltips = [('Nama','@Name'), ('Adj Close','@Adj_Close')]
tooltips1 = [('Nama','@Name'), ('Adj Close', '@Adj_Close')]
tooltips2 = [('Nama','@Name'), ('Volume', '@Volume')]
tooltips3 = [('Nama','@Name'), ('Day_Perc_Change', '@Day_Perc_Change')]

# Membuat Figure Analisis
fig = figure(plot_height=600, plot_width=800, x_axis_type='datetime', x_axis_label='Date', y_axis_label='Adj Close',
             title='Adj Close Pasar Saham')

fig.add_tools(HoverTool(tooltips=tooltips))

fig.line(x='Date', y='Adj_Close', source=source_hangseng, legend_label='Hang Seng', color='red')
fig.line(x='Date', y='Adj_Close', source=source_nasdaq, legend_label='Nasdaq', color='green')
fig.line(x='Date', y='Adj_Close', source=source_nikkei, legend_label='Nikkei', color='yellow')

options = [tooltips, tooltips1, tooltips2, tooltips3]

# Membuat callback untuk mengupdate tooltips
callback = CustomJS (args=dict(tt=fig.hover, opts=options), code="""
    if (cb_obj.value=='Normal') {
        tt[0].tooltips=opts[0]
    } else if (cb_obj.value=='Adj Close') {
      tt[0].tooltips=opts[1]
    } else if (cb_obj.value=='Volume') {
      tt[0].tooltips=opts[2]
    } else {
        tt[0].tooltips=opts[3]
    }
    """)

# Membuat menu dropdown parameter
stat_select = Select(options=['Adj Close', 'Volume', 'Day_Perc_Change'], title='Macam-Macam Parameter:')
stat_select.js_on_change("value", callback)

# Visualisasi
fig.legend.location = "top_left"
fig.legend.click_policy="hide"
show(column(stat_select,fig))

