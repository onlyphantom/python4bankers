import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from io import BytesIO
import base64


import matplotlib
matplotlib.use('Agg')


def plot_region(df):
    df.region = ______.str.title() ## (Task 3.1.1.)

    fig, ax = plt.subplots()
    plt_region = df.region.____.plot(kind=___,figsize = (8,6)) ## (Task 3.1.2.)

    # additional adjustment
    plt_region.yaxis.set_major_formatter(mtick.StrMethodFormatter('€{x:,.0f}'))
    plt_region.get_figure().suptitle('Total Loans by Region')
    plt.xticks(rotation = 0)

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    return(result)

def plot_term(df):
    fig, ax = plt.subplots()
    plt_term = df[_____].boxplot(by =____, figsize=(8,6)) ## (Task 3.2.1.)
    
    # additional adjustments
    plt.tight_layout()
    plt_term.yaxis.set_major_formatter(mtick.StrMethodFormatter('€{x:,.0f}'))
    plt_term.get_figure().suptitle('Loan Amounts by Term')
    plt_term.get_figure().gca().set_xlabel("")
    plt_term.get_figure().gca().set_title("")

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    return(result)


def plot_purpose(df):
    df.purpose = df.purpose.str.replace("_"," ").str.title()
    fig, ax = plt.subplots()
    plt_purpose = df.purpose.______.tail(8).plot(
        kind = _____, title = "Total Loans by Purpose",figsize = (8,6)
    )## Task (3.3.1.)

    # additional adjustments
    plt.tight_layout()
    plt_term.xaxis.set_major_formatter(mtick.StrMethodFormatter('€{x:,.0f}'))

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    return(result)
