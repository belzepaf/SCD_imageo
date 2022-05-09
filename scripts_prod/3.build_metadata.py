# -*- coding: utf-8 -*-
# PYTHON 3
#----------------------------------------------------------------------------
# Created By  : Mélanie Aubry - aubry.melanie33@gmail.com
# Created Date: April 03, 2022
# ---------------------------------------------------------------------------

import pandas as pd
import openpyxl
import re
from definitions import INPUT_DIR, OUTPUT_DIR
from datetime import date

MD = pd.read_excel(f'{OUTPUT_DIR}/parse_sudoc_20220426.xlsx')

GL = pd.read_excel(f'{INPUT_DIR}/global_save_test_2.xlsx')

matching_ppn = GL.PPN.isin(MD.PPN)

new_df = pd.merge(MD,GL, on='PPN')

new_df['PPN'].astype(str)

new_df['title'] = new_df['title'].str.replace('#',' ')

new_df['creatorentity'] = new_df['creatorentity'].str.replace('#',', ')

new_df['date'] = new_df['datefull']

new_df['date'] = new_df.datefull.str.split().str.get(0)

new_df['date'] = new_df['date'].str.slice(9,13)

new_df['extent'] = '1:' + new_df['extent'].astype(str)

new_df=new_df.assign(type='http://purl.org/coar/resource_type/c_12cd')

def dms_to_dd(x):
    dir = str(x[:1])
    deg = int(x[1:-4])
    min = int(x[4:-2])
    sec = float(x[6:])
    dd = float(deg) + float(min)/60 + float(sec)/(60*60)
    if dir == 'S' or dir == 'W':
        dd *= -1
    return dd

new_df['westlimit'] = new_df['westlimit'].map(dms_to_dd).astype(str)
new_df['eastlimit'] = new_df['eastlimit'].map(dms_to_dd).astype(str)
new_df['northlimit'] = new_df['northlimit'].map(dms_to_dd).astype(str)
new_df['southlimit'] = new_df['southlimit'].map(dms_to_dd).astype(str)

new_df['spatial'] = "northlimit=" + new_df['northlimit'] + "; " + "southlimit=" + new_df['southlimit'] + "; " + "westlimit=" + new_df['westlimit'] + "; " + "eastlimit" + new_df['eastlimit']

new_df.drop(columns=['Unnamed: 0','westlimit','eastlimit', 'northlimit', 'southlimit','datefull', 'Lot', 'titre', 'nom de fichier attendu v2', 'Nalaka (JP2)', 'poids (MB)', 'georef', 'poids (MB).1', 'continent', 'continent_geonames' , 'pays', 'pays_geonames', 'Notes'], inplace=True)

out_path = f'{OUTPUT_DIR}/metadata_{date.today().strftime("%Y%m%d")}.xlsx'

writer = pd.ExcelWriter(out_path , engine='openpyxl')
new_df.to_excel(writer, sheet_name='Sheet1')
writer.save()

new_df.to_csv(f'{OUTPUT_DIR}/metadata_{date.today().strftime("%Y%m%d")}.csv', index=None, header=True)

print('MERGE DONE. .XLSX/.CSV CREATED')