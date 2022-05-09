# -*- coding: utf-8 -*-
# PYTHON 3
#----------------------------------------------------------------------------
# Created By  : Mélanie Aubry - aubry.melanie33@gmail.com
# Created Date: April 02, 2022
# ---------------------------------------------------------------------------

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = f'{ROOT_DIR}/input'
OUTPUT_DIR = f'{ROOT_DIR}/output'

BASE_URL = "https://test.nakala.fr"
API_URL = "https://apitest.nakala.fr"
API_KEY_NKL = "01234567-89ab-cdef-0123-456789abcdef"

NAKALA_API_HEADERS = {
    "X-API-KEY": API_KEY_NKL,
    "accept": "application/json",
    "Content-Type": "application/json"
} 

COLUMN_NAME_BY_META_PROPERTY_NAKALA = {
    'http://nakala.fr/terms#title': 'title',
    'http://nakala.fr/terms#creator': 'creator',
#   'http://nakala.fr/terms#license': 
    'http://nakala.fr/terms#type':  'type',
    'http://nakala.fr/terms#created': 'date',
    'http://purl.org/dc/terms/source': 'ppn',
    'http://purl.org/dc/terms/format': 'f',
    'http://purl.org/dc/terms/subject': 'subject',
    'http://purl.org/dc/terms/language': 'language',
    'http://purl.org/dc/terms/spatial': 'spatial',
    'http://purl.org/dc/terms/extent': 'extent',
    'http://purl.org/dc/terms/publisher': 'publisher',
    'http://purl.org/dc/terms/description': 'description',
    'http://purl.org/dc/terms/identifier': 'cote'
}

TYPE_BY_META_PROPERTY_NAKALA = {
    'http://nakala.fr/terms#title': 'http://www.w3.org/2001/XMLSchema#string',
    'http://nakala.fr/terms#created': 'http://www.w3.org/2001/XMLSchema#string'
}

META_PROPERTY_NAKALA_BY_COLUMN_NAME = {v: k for k, v in COLUMN_NAME_BY_META_PROPERTY_NAKALA.items()}