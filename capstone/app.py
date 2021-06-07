from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from io import BytesIO
import base64


import matplotlib
matplotlib.use('Agg')

from loans import *


app = Flask(__name__)

# Read data (Task 1)
_____________ = pd.read_csv(_____________)

@app.route('/')
def index():
    # generate values for cards (Task 2)
    num_applicants = _____________ ## (Task 2.1.)
    avg_loan_amounts = _____________ ## (Task 2.2.)

    ## Task (2.3.)
    cond = pd.crosstab(
        index = _____________,
        columns = "percent",
        normalize=_____________
    )*100
    good_loan = round(_____________,2)
    bad_loan = round(_____________,2)

    ## compile values as dictionary (Task 2.4.)
    card_data = dict(
        num_applicants =  f'{____:,}',
        avg_loan_amounts = f'{____:,}',
        good_loan = f'{____:,}%',
        bad_loan = f'{____:,}%'
    )

    # generate plot
    plot_region_res = plot_region(df)
    plot_term_res = plot_term(df)
    plot_purpose_res = plot_purpose(df)

    return render_template(
        "index.html",
        card_data = card_data,
        plot_region_res = plot_region_res,
        plot_term_res = plot_term_res,
        plot_purpose_res = plot_purpose_res
    )

if __name__ == "__main__": 
    app.run(debug=True)