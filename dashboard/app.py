##########################################
# Caleb Sellinger
# Cont Intel 44630
# Dr. Case
# 11-24-2024
##########################################

################
# Imports
################
from shiny import reactive
from shiny.express import render, ui
from shinywidgets import render_plotly
import plotly.express as px
import pandas as pd
from pathlib import Path
import jinja2

#############################
# Reactive Calc Function(s)
#############################


##################
# Page Options
##################
ui.page_opts(title="Module 6: Custom App", fillable=True)


########################
# UI Sidebar Components
########################
with ui.sidebar(open="open"):
    ui.h1("Placeholder [Bottom Text]",class_="text-center")
    ui.input_dark_mode(mode="dark")
    ui.hr()

#############
# Body
#############
file = Path(__file__).parent/ "../State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"

@reactive.file_reader(file)
def read_file():
    return pd.read_csv(file)

with ui.layout_columns():
    with ui.card(full_screen=True):
        @render.table
        def file_grid():
            return read_file()