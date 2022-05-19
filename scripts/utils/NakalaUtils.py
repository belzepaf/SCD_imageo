import requests
import json
from definitions import API_URL, NAKALA_API_HEADERS

def get_data(nakala_id):
    print(f'FINDING NAKALA DATA WITH ID "{nakala_id}"...')
    endpoint = API_URL + '/datas/' + nakala_id
    response = requests.get(endpoint, headers=NAKALA_API_HEADERS)
    if response.status_code != 200:
        raise Exception(f'Data not found, details : {response.text}')
    return json.loads(response.text)

def put_data(nakala_data):
    print('OVERRIDING NAKALA METADATA BY SENDING "PUT" REQUEST...')
    endpoint = API_URL + '/datas/' + nakala_data["identifier"]
    response = requests.put(endpoint, json.dumps(nakala_data), headers=NAKALA_API_HEADERS)
    print(f'..."PUT" REQUEST FINISHED WITH STATUS {response.status_code}')
    print(f'RESPONSE : {response.text}')
    return response.text

def post_metadata(nakala_id, metadata_to_post):
    print(f'SENDING META {metadata_to_post["propertyUri"]} BY "POST" REQUEST...')
    endpoint = API_URL + '/datas/' + nakala_id + '/metadatas'
    response = requests.post(endpoint, json.dumps(metadata_to_post), headers=NAKALA_API_HEADERS)
    print(f'..."POST" REQUEST FINISHED WITH STATUS {response.status_code}')
    print(f'RESPONSE : {response.text}')
    return json.loads(response.text)

def post_relations(nakala_id, relations):
    print(f'ADDING {len(relations)} NEW RELATIONS ON "{nakala_id}"')
    endpoint = API_URL+"/datas/"+ nakala_id + "/relations"
    response = requests.post(endpoint, json.dumps(relations), headers=NAKALA_API_HEADERS)
    print(f'...RELATIONS ADDED ON "{nakala_id}"')
    print(f'RESPONSE : {response.text}')
    return json.loads(response.text)