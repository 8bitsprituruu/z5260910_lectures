""" yf_example3.py is a module that has the purpose of downloading stock price data and saving it to a csv file
"""
import yf_example2

def qan_prc_to_csv(year):
    """ Download Qantas stock prices for a given year into a CSV file"""

    if __name__ == "__main__":
        import os
        import toolkit_config as cfg
        tic = 'QAN.AX'
        pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')

    yf_example2.yf_prc_to_csv(tic, pth, f"{year}-01-01", f"{year}-12-31")

qan_prc_to_csv(year=2020)

