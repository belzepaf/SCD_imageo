# -*- coding: utf-8 -*-
# PYTHON 3
#----------------------------------------------------------------------------
# Created By  : Mélanie Aubry - aubry.melanie33@gmail.com
# Created Date: March 29, 2022
# ---------------------------------------------------------------------------

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from definitions import OUTPUT_DIR, INPUT_DIR
from datetime import date

DOMAIN = 'https://www.sudoc.fr'
SUDOC_ID_COLUMN = 'PPN'

def extract_text_from_tags(xml_record, tags):
    if(tags := xml_record.select(tags)):
        text = []
        for tag in tags:
            text.append(tag.get_text(strip=True))
        return '#'.join(text)
    return None

def extract_first_text_from_tags(xml_record, tags):
    if(tags := xml_record.select(tags)):
        for tag in tags:
            return tag.get_text(strip=True)
    return None

def create_sudoc_excel_from_csv():
    csv_file = pd.read_csv(f'{INPUT_DIR}/global_save.csv')
    csv_file = csv_file[csv_file['PPN'].notna()]
    csv_file['PPN'] = csv_file['PPN'].astype('str').str.removesuffix('.0')
    csv_file['URL'] = DOMAIN + '/' + csv_file['PPN'].astype(str) + '.xml'

    urls_list = csv_file.URL.tolist()

    sudoc_maps = []
    for url in urls_list:
        response = requests.get(url)
        xml_response = bs(response.text, 'lxml')
        if(xml_record := xml_response.select_one('record')):
            sudoc_maps.append({
                'PPN': extract_text_from_tags(xml_record, 'controlfield[tag="001"]'),
                'title': extract_text_from_tags(xml_record, 'datafield[tag="200"] [code="a"], datafield[tag="200"] [code="c"], datafield[tag="200"] [code="d"], datafield[tag="200"] [code="e"], datafield[tag="200"] [code="f"]'),
                'creatorln': extract_text_from_tags(xml_record, 'datafield[tag="700"] [code="a"]'),
                'creatorfn': extract_text_from_tags(xml_record, 'datafield[tag="700"] [code="b"]'),
                'creatorentity': extract_text_from_tags(xml_record, 'datafield[tag="710"] [code="a"], datafield[tag="710"] [code="b"]'),
                'datefull': extract_text_from_tags(xml_record, 'datafield[tag="100"] [code="a"]'),
                'format': extract_text_from_tags(xml_record, 'datafield[tag="215"] [code="d"]'),
                'subject': extract_text_from_tags(xml_record, 'datafield[tag="607"] [code="a"]'),
                'language': extract_first_text_from_tags(xml_record, 'datafield[tag="101"] [code="a"],datafield[tag="101"] [code="c"]'),
                'westlimit_sudoc': extract_text_from_tags(xml_record, 'datafield[tag="123"] [code="d"]'),
                'eastlimit_sudoc': extract_text_from_tags(xml_record, 'datafield[tag="123"] [code="e"]'),
                'northlimit_sudoc': extract_text_from_tags(xml_record, 'datafield[tag="123"] [code="f"]'),
                'southlimit_sudoc': extract_text_from_tags(xml_record, 'datafield[tag="123"] [code="g"]'),
                'extent': extract_text_from_tags(xml_record, 'datafield[tag="123"] [code="b"]'),
                'publisher': extract_text_from_tags(xml_record, 'datafield[tag="210"] [code="c"]'),
                'description': extract_text_from_tags(xml_record, 'datafield[tag="300"]')
            })
    dataFrame = pd.DataFrame(sudoc_maps)

    writer = pd.ExcelWriter(f'{OUTPUT_DIR}/parse_sudoc_{date.today().strftime("%Y%m%d")}.xlsx' , engine='openpyxl')
    dataFrame.to_excel(writer, sheet_name='Sheet1')
    writer.save()

create_sudoc_excel_from_csv()

print("FROM PPN(SUDOC) IN EXCEL, XML PARSED")