import os
import pandas as pd


def read_excel(excel_file, sheet_name, excel_dir='excel', engine='openpyxl'):
    return pd.read_excel(
        os.path.join(os.path.dirname(__file__), excel_dir, excel_file),
        sheet_name=sheet_name,
        engine=engine,
    )


def filter_deg(df):
    return (df.assign(LFC=lambda x: round(x['Log2 fold change'], 2),
                      pval=lambda x: x['Adjusted p-value'].apply(lambda x: '%.1E' % x))
            .filter(['Gene ID', 'LFC', 'pval', 'Gene symbol', 'Gene name'])
            .rename(columns={'pval':'Adj p-val'}))


def write_csv(pd, ofile_name, data_dir='_data'):
    pd.to_csv(
        os.path.join(os.path.dirname(__file__), "..", data_dir, ofile_name),
        index=False
    )


def generate_csv(excel_file, sheet_name, filter_func, ofile_name):
    (read_excel(excel_file, sheet_name)
     .pipe(filter_func)
     .pipe(write_csv, ofile_name=ofile_name))


# DEG L2:L1
excel_file = 'Dataset_01_DEG.xlsx'
sheet_name = 'L2L1'
ofile_name = 'degl2l1.csv'

generate_csv(excel_file, sheet_name, filter_deg, ofile_name)


# DEG L2:L1
excel_file = 'Dataset_01_DEG.xlsx'
sheet_name = 'L3L1'
ofile_name = 'degl3l1.csv'

generate_csv(excel_file, sheet_name, filter_deg, ofile_name)
