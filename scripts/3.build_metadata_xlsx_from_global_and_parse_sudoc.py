# -*- coding: utf-8 -*-
# PYTHON 3
#----------------------------------------------------------------------------
# Created By  : Mélanie Aubry - aubry.melanie33@gmail.com
# Created Date: April 03, 2022
# ---------------------------------------------------------------------------

from tokenize import Ignore
import pandas as pd
import math
from definitions import INPUT_DIR, OUTPUT_DIR
from datetime import date

#Key error T-T
# Ne pas oublier de changer !
parse_sudoc = pd.read_excel(f'{OUTPUT_DIR}/parse_sudoc_20220513.xlsx')

global_save = pd.read_excel(f'{INPUT_DIR}/global_save.xlsx')

matching_ppn = global_save.PPN.isin(parse_sudoc.PPN)

md_nakala_import = pd.merge(parse_sudoc, global_save, on='PPN')

md_nakala_import['PPN'].astype(str)

md_nakala_import['title'] = md_nakala_import['title'].str.replace('#',' ')

md_nakala_import['creatorentity'] = md_nakala_import['creatorentity'].str.replace('#',', ')

md_nakala_import['date'] = md_nakala_import['datefull']
md_nakala_import['date'] = md_nakala_import.datefull.str.split().str.get(0)
md_nakala_import['date'] = md_nakala_import['date'].str.slice(9,13)
md_nakala_import['date'] = md_nakala_import['date'].str.replace('X', '')
md_nakala_import['date'] = md_nakala_import['date'].astype(str).str.ljust(4, '0')

md_nakala_import['extent'] = '1:' + md_nakala_import['extent'].astype(str)

md_nakala_import=md_nakala_import.assign(type='http://purl.org/coar/resource_type/c_12cd')

def conversion_dms_to_dd(dms):
    if isinstance(dms, float) and math.isnan(dms) or len(dms) != 8:
        return
    dir = str(dms[:1])
    deg = int(dms[1:-4])
    min = int(dms[4:-2])
    sec = float(dms[6:])
    dd = float(deg) + float(min)/60 + float(sec)/(60*60)
    if dir == 'S' or dir == 'W':
        dd *= -1
    return dd

md_nakala_import['westlimit_sudoc'] = md_nakala_import['westlimit_sudoc'].map(conversion_dms_to_dd).astype(str)
md_nakala_import['eastlimit_sudoc'] = md_nakala_import['eastlimit_sudoc'].map(conversion_dms_to_dd).astype(str)
md_nakala_import['northlimit_sudoc'] = md_nakala_import['northlimit_sudoc'].map(conversion_dms_to_dd).astype(str)
md_nakala_import['southlimit_sudoc'] = md_nakala_import['southlimit_sudoc'].map(conversion_dms_to_dd).astype(str)
md_nakala_import['westlimit'].fillna(md_nakala_import['westlimit_sudoc'])
md_nakala_import['eastlimit'].fillna(md_nakala_import['eastlimit_sudoc'])
md_nakala_import['northlimit'].fillna(md_nakala_import['northlimit_sudoc'])
md_nakala_import['southlimit'].fillna(md_nakala_import['southlimit_sudoc'])
md_nakala_import['spatial'] = "northlimit=" + md_nakala_import['northlimit'].astype(str) + "; " + "southlimit=" + md_nakala_import['southlimit'].astype(str) + "; " + "westlimit=" + md_nakala_import['westlimit'].astype(str) + "; " + "eastlimit=" + md_nakala_import['eastlimit'].astype(str)

md_nakala_import.loc[md_nakala_import['date'].astype(int) <= 1920, 'licence'] = "etalab-2.0"
md_nakala_import.loc[md_nakala_import['date'].astype(int) > 1920, 'licence'] = "Reserved"

md_nakala_import.drop(columns=['Unnamed: 0','westlimit', 'eastlimit', 'northlimit', 'southlimit', 'westlimit_sudoc','eastlimit_sudoc', 'northlimit_sudoc', 'southlimit_sudoc','datefull', 'Lot', 'titre', 'nom de fichier attendu v2', 'Nalaka (JP2)', 'poids (MB)', 'georef', 'poids (MB).1', 'Notes'], inplace=True)

out_path = f'{OUTPUT_DIR}/metadata_{date.today().strftime("%Y%m%d")}.xlsx'

writer = pd.ExcelWriter(out_path , engine='openpyxl')
md_nakala_import.to_excel(writer, sheet_name='Sheet1')
writer.save()

md_nakala_import.to_csv(f'{OUTPUT_DIR}/metadata_{date.today().strftime("%Y%m%d")}.csv', index=None, header=True)

print('MERGE DONE. .XLSX/.CSV CREATED')
