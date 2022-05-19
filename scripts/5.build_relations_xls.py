# -*- coding: utf-8 -*-
# PYTHON 3
#----------------------------------------------------------------------------
# Created By  : Mélanie Aubry - aubry.melanie33@gmail.com
# Created Date: May 10, 2022
# ---------------------------------------------------------------------------

from heapq import merge
from definitions import INPUT_DIR, OUTPUT_DIR
from datetime import date
import pandas as pd


global_xls = pd.read_excel(f'{INPUT_DIR}/global_save.xlsx')
philippe_xls = pd.read_excel(f'{INPUT_DIR}/Fichier de Synthèse de Philippe_202204.xlsx')
matching_ppn = global_xls.cote.isin(philippe_xls.cote)
merge_global = pd.merge(global_xls, philippe_xls, on='cote', how="left")

handle_relation = merge_global[["PPN_y", "Carte en plusieurs feuilles", "Série carte topo", "Même ensemble", "handle_full_georef", "handle geotiff", "handle geotiff pdf", "handle geotiff points", "handle geotiff jp2"]].copy()
handle_relation.dropna(subset = "PPN_y", inplace=True)

handle_relation['relation'] = handle_relation['Carte en plusieurs feuilles'].fillna('') + handle_relation['Série carte topo'].fillna('') + handle_relation['Même ensemble'].fillna('')

handle_relation = handle_relation.drop(columns=['Carte en plusieurs feuilles', 'Série carte topo', 'Même ensemble'], axis=1)

print(handle_relation)
handle_relation.to_excel(f'{OUTPUT_DIR}/relations__{date.today().strftime("%Y%m%d")}.xlsx')
#Don't mind the alert, not an error
print('FICHIER "RELATIONS" CRÉÉ !')