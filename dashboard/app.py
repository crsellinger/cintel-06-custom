##########################################
# Caleb Sellinger
# Cont Intel 44630
# Dr. Case
# 12-02-2024
##########################################

################
# Imports
################
from shiny import reactive
from shiny.express import render, ui, input, output
from shinywidgets import render_plotly, render_widget
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
from pathlib import Path
import jinja2
import plotly.graph_objects as go

# File contains typical home value across all homes per state within the 35th and 65th percentile
file = Path(__file__).parent/ "data/State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"

@reactive.file_reader(file)
def read_file():
    input_file = pd.read_csv(file)
    df = pd.DataFrame(input_file)
    return df

# def max_price():
#     table = read_file()
#     max_column=table.max(axis=0)
#     print(max_column)

# List for all dates in data set
list_dates = [
               "2000-01-31","2000-02-29","2000-03-31","2000-04-30","2000-05-31","2000-06-30","2000-07-31","2000-08-31","2000-09-30","2000-10-31","2000-11-30","2000-12-31","2001-01-31","2001-02-28"
              ,"2001-03-31","2001-04-30","2001-05-31","2001-06-30","2001-07-31","2001-08-31","2001-09-30","2001-10-31","2001-11-30","2001-12-31","2002-01-31","2002-02-28","2002-03-31","2002-04-30"
              ,"2002-05-31","2002-06-30","2002-07-31","2002-08-31","2002-09-30","2002-10-31","2002-11-30","2002-12-31","2003-01-31","2003-02-28","2003-03-31","2003-04-30","2003-05-31","2003-06-30"
              ,"2003-07-31","2003-08-31","2003-09-30","2003-10-31","2003-11-30","2003-12-31","2004-01-31","2004-02-29","2004-03-31","2004-04-30","2004-05-31","2004-06-30","2004-07-31","2004-08-31"
              ,"2004-09-30","2004-10-31","2004-11-30","2004-12-31","2005-01-31","2005-02-28","2005-03-31","2005-04-30","2005-05-31","2005-06-30","2005-07-31","2005-08-31","2005-09-30","2005-10-31"
              ,"2005-11-30","2005-12-31","2006-01-31","2006-02-28","2006-03-31","2006-04-30","2006-05-31","2006-06-30","2006-07-31","2006-08-31","2006-09-30","2006-10-31","2006-11-30","2006-12-31"
              ,"2007-01-31","2007-02-28","2007-03-31","2007-04-30","2007-05-31","2007-06-30","2007-07-31","2007-08-31","2007-09-30","2007-10-31","2007-11-30","2007-12-31","2008-01-31","2008-02-29"
              ,"2008-03-31","2008-04-30","2008-05-31","2008-06-30","2008-07-31","2008-08-31","2008-09-30","2008-10-31","2008-11-30","2008-12-31","2009-01-31","2009-02-28","2009-03-31","2009-04-30"
              ,"2009-05-31","2009-06-30","2009-07-31","2009-08-31","2009-09-30","2009-10-31","2009-11-30","2009-12-31","2010-01-31","2010-02-28","2010-03-31","2010-04-30","2010-05-31","2010-06-30"
              ,"2010-07-31","2010-08-31","2010-09-30","2010-10-31","2010-11-30","2010-12-31","2011-01-31","2011-02-28","2011-03-31","2011-04-30","2011-05-31","2011-06-30","2011-07-31","2011-08-31"
              ,"2011-09-30","2011-10-31","2011-11-30","2011-12-31","2012-01-31","2012-02-29","2012-03-31","2012-04-30","2012-05-31","2012-06-30","2012-07-31","2012-08-31","2012-09-30","2012-10-31"
              ,"2012-11-30","2012-12-31","2013-01-31","2013-02-28","2013-03-31","2013-04-30","2013-05-31","2013-06-30","2013-07-31","2013-08-31","2013-09-30","2013-10-31","2013-11-30","2013-12-31"
              ,"2014-01-31","2014-02-28","2014-03-31","2014-04-30","2014-05-31","2014-06-30","2014-07-31","2014-08-31","2014-09-30","2014-10-31","2014-11-30","2014-12-31","2015-01-31","2015-02-28"
              ,"2015-03-31","2015-04-30","2015-05-31","2015-06-30","2015-07-31","2015-08-31","2015-09-30","2015-10-31","2015-11-30","2015-12-31","2016-01-31","2016-02-29","2016-03-31","2016-04-30"
              ,"2016-05-31","2016-06-30","2016-07-31","2016-08-31","2016-09-30","2016-10-31","2016-11-30","2016-12-31","2017-01-31","2017-02-28","2017-03-31","2017-04-30","2017-05-31","2017-06-30"
              ,"2017-07-31","2017-08-31","2017-09-30","2017-10-31","2017-11-30","2017-12-31","2018-01-31","2018-02-28","2018-03-31","2018-04-30","2018-05-31","2018-06-30","2018-07-31","2018-08-31"
              ,"2018-09-30","2018-10-31","2018-11-30","2018-12-31","2019-01-31","2019-02-28","2019-03-31","2019-04-30","2019-05-31","2019-06-30","2019-07-31","2019-08-31","2019-09-30","2019-10-31"
              ,"2019-11-30","2019-12-31","2020-01-31","2020-02-29","2020-03-31","2020-04-30","2020-05-31","2020-06-30","2020-07-31","2020-08-31","2020-09-30","2020-10-31","2020-11-30","2020-12-31"
              ,"2021-01-31","2021-02-28","2021-03-31","2021-04-30","2021-05-31","2021-06-30","2021-07-31","2021-08-31","2021-09-30","2021-10-31","2021-11-30","2021-12-31","2022-01-31","2022-02-28"
              ,"2022-03-31","2022-04-30","2022-05-31","2022-06-30","2022-07-31","2022-08-31","2022-09-30","2022-10-31","2022-11-30","2022-12-31","2023-01-31","2023-02-28","2023-03-31","2023-04-30"
              ,"2023-05-31","2023-06-30","2023-07-31","2023-08-31","2023-09-30","2023-10-31","2023-11-30","2023-12-31","2024-01-31","2024-02-29","2024-03-31","2024-04-30","2024-05-31","2024-06-30"
              ,"2024-07-31","2024-08-31","2024-09-30","2024-10-31"
              ]

# State 2 letter abbreviation for choropleth map
state_code={
            "Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO","Connecticut":"CT","Delaware":"DE","Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID",
            "Illinois":"IL","Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN",
            "Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV","New Hampshire":"NH","New Jersey":"NJ","New Mexico":"NM","New York":"NY","North Carolina":"NC",
            "North Dakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","Rhode Island":"RI","South Carolina":"SC","South Dakota":"SD","Tennessee":"TN","Texas":"TX",
            "Utah":"UT","Vermont":"VT","Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY"
            }

#############################
# Reactive Calc Function(s)
#############################

# For Bar Graph
@reactive.calc
def filter():
    filtered = input.select_date()
        # for i in filtered:
        #     if filtered[i] > input.select_price()[0] & filtered[i] < input.select_price()[1]:
        #         price_range = filtered

    return filtered

@reactive.calc
def price_range():
    range = input.select_price()
    return range

##################
# Page Options
##################
ui.page_opts(title="Zillow Home Prices Thoughout the Years", fillable=True)


########################
# UI Sidebar Components
########################
with ui.sidebar(open="open"):
    ui.h1("Discover Home Values in Your State",class_="text-center")
    ui.input_dark_mode(mode="dark")
    ui.hr()
    ui.input_slider("select_price","Price (Does not work)",0,1000000,step=10000,pre="$",value=1000000)
    ui.input_select("select_date","Select Date", choices=list_dates,selected="2024-10-31")

#############
# Body
#############

with ui.layout_columns():
    with ui.card(full_screen=True):
        @render.data_frame
        def file_grid():
            return render.DataGrid(read_file())
        
    with ui.card(full_screen=True):
        @render_widget
        def map():
            # Choropleth map does not contain D.C. as state, so we have to drop this column in order for map to be colored correctly
            df = read_file()[read_file()['RegionName'] != 'District of Columbia']

            # price = price_range()
            # ser = df[filter()]
            # filtered_state_code = list(state_code.values())
            # for i,value in ser.items():
            #     print(i)
            #     if value < price:
            #         filtered_state_code.pop(i)
            
            # print(filtered_state_code)

            # Must provide locations param with 2 letter code of states, else no worky
            # Also df must be sorted identical to state code dict above, else values do not match proper state
            return px.choropleth(df.sort_values(by="RegionName"),
                                 locations=state_code,
                                 locationmode="USA-states",
                                 color=filter(),
                                 scope="usa",
                                 labels={filter():"Price (USD)"},
                                 title="United State of America",
                                 )
        

with ui.layout_columns():
    with ui.card():
        @render_plotly
        def bar():
            fig = px.bar(
                read_file().sort_values(by="RegionName"),
                x="RegionName",y=filter(),
                color=filter(),
                title="Average Home Price by State",
                labels={"RegionName":"State",filter():"Price (USD)"},
                hover_name=filter(),
                hover_data={"RegionName":False,filter():False}
                )
            
            # fig.update_traces(marker_color='coral')

            return fig
