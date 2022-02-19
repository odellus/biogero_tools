import yaml
import pandas as pd
from uuid import uuid4

def get_cfg():
    fname = 'config.yaml'
    with open(fname, 'r') as f:
        return yaml.load(f, Loader=yaml.Loader)

def reset_index(df):
    df['uid'] = [uuid4().hex for _ in range(len(df))]
    return df.set_index('uid')
