import time
import requests
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET

from tqdm import tqdm
from utils import get_cfg, reset_index

cfg = get_cfg()

def get_entrez_url(cas_number):
    """Use entrez API to get pubchem ids from a cas number."""
    api_root = "http://www.ncbi.nlm.nih.gov/entrez/eutils"
    query = f"esearch.fcgi?db=pccompound&retmax=10000&term={cas_number}"
    return f"{api_root}/{query}"

def load_drugage(cfg):
    fpath = cfg['data']['drugage_path']
    df = pd.read_csv(fpath)
    df = df.drop(columns=['Unnamed: 10', 'Unnamed: 11'])
    return reset_index(df)

def get_cas_numbers(drugage):
    return {
        k: None if type(v) is float and np.isnan(v) else v 
            for k,v in drugage['cas_number'].to_dict().items()
    }

def ask_entrez(uid, cas_number):
    url = get_entrez_url(cas_number)
    time.sleep(0.5)
    res = requests.get(url)
    return parse_entrez(res, uid, cas_number)

def parse_entrez(response, uid, cas_number):
    pubchem_cids = []
    if response.status_code != 200:
        print(f'Bad request for cas_number {cas_number} with uid {uid} ')
        return pubchem_cids
    
    # Okay now we know we got a response, let's parse it.
    xml = response.text
    tree = ET.fromstring(xml)
    for item in tree.findall('IdList'):
        for node in item:
            pubchem_cids.append(node.text)
    return pubchem_cids

def get_all_cids(drugage):
    #TODO: This is premature. We still have to clean the cas_numbers column.
    cas_numbers = get_cas_numbers(drugage)
    res = {}
    for key, val in tqdm(cas_numbers.items()):
        if val is None: continue
        cids = ask_entrez(key, val)
        res[val] = cids
    return res

def get_sdf(cid):
    base_url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{cid}/record/SDF'
    query = f'record_type=3d&response_type=save&response_basename=Conformer3D_CID_{cid}'
    res = requests.get(f'{base_url}/?{query}')
    sdf_text = res.text.replace('\\n', '\n')
    return sdf_text