"""
This script comprises the extract system for the Tamales_inc project, and is
in charge of processing datasets and homologate them and refers to script 1
"received data cleaning script"
"""

import os
import sys
import pandas as pd
from pathlib import Path

report_date = "20200801"
file_names_tamales_inc = ["Centro","E._Privados", "Norte","Sur"]
file_names_teinvento_inc = ["fact_table", "product_dim", "region_dim"]
BASE_DIR = str(Path(__file__).resolve().parent)

def extract():
    """
    Extract files from
    "./tamales_inc/ventas_mensuales_tamales_inc/mx/20200801/csv":
        and unifies in only one "df"
    """
    print('extracting files from tamales_inc db.....')
    try:
        for name in file_names_tamales_inc:
            file_path_tamales_inc = (BASE_DIR
                                     + "/tamales_inc/ventas_mensuales_tamales_inc/mx/"
                                     + report_date + '/csv/' + name + '/ventas_mensuales_'
                                     + name + ".csv")

            if name == "Centro":
                df = pd.read_csv(file_path_tamales_inc, header=None, 
                                 names=['Year','Month','Country',
                                 'Calorie_type','Flavor','Zone',
                                 'Resellers_id','Combo_type','Sales'])
            else:
                df_2 = pd.read_csv(file_path_tamales_inc, header=None,
                                   names=['Year','Month','Country',
                                   'Calorie_type','Flavor','Zone',
                                   'Resellers_id','Combo_type','Sales'])
                df = df.append(df_2, ignore_index=True)

        print('Gathering files ......')
        df['Month'] = pd.to_datetime(df['Month'], errors='coerce', format="%b")
        df['Month'] = df['Month'].dt.strftime('%m')
        df.convert_dtypes().dtypes

    except FileNotFoundError as err:
        print('Something went wrong, verify your files: ', err)
    else:
        print('Successful extraction')

    return df


def run():
    extract()


if __name__ == "__main__":
    run()
