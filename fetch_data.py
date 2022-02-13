import os
import yaml
import wget
import time

from argparse import ArgumentParser
from zipfile import ZipFile

from absl import app
from absl import flags

def get_cfg():
    fname = 'config.yaml'
    with open(fname, 'r') as f:
        return yaml.load(f, Loader=yaml.Loader)


  
# specifying the zip file name
def unzip_file(fname):
    assert os.path.splitext(fname)[-1] == '.zip'
    # opening the zip file in READ mode
    with ZipFile(fname, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()
    
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')


cfg = get_cfg()

def parse_args(cfg):
    parser = ArgumentParser()
    for arg in cfg['args']:
        arg_name = arg['name']
        arg_default = arg['default']
        arg_type = type(arg_default)
        parser.add_argument(
            f'--{arg_name}', 
            dest=arg_name,
            type=arg_type, 
            default=arg_default
        )
    args = parser.parse_args()
    return args

print(cfg)

FLAGS = flags.FLAGS

def parse_absl(cfg, flags):
    for arg in cfg['args']:
        arg_name = arg['name']
        arg_default = arg['default']
        arg_type = type(arg_default)
        arg_descr = arg['description']
        if arg_type == int:
            flags.DEFINE_integer(arg_name, arg_default, arg_descr)
        elif arg_type == float:
            flags.DEFINE_float(arg_name, arg_default, arg_descr)
        elif arg_type == bool:
            flags.DEFINE_bool(arg_name, arg_default, arg_descr)
        elif arg_type == str:
            flags.DEFINE_string(arg_name, arg_default, arg_descr)

parse_absl(cfg, flags)

def main(argv):
    for arg in cfg['args']:
        arg_name = arg['name']
        if hasattr(FLAGS, arg_name):
            arg_val = getattr(FLAGS, arg_name)
            print({arg_name: arg_val})



if not os.path.exists('data'): os.mkdir('data')

def get_genage():
    os.chdir('data')
    os.mkdir('genage')
    os.chdir('genage')
    fname_out = wget.download(cfg['data']['gen_age_homo'])
    print(fname_out)
    unzip_file(fname_out)
    time.sleep(1)
    fname_out = wget.download(cfg['data']['gen_age_model'])
    unzip_file(fname_out)
    os.chdir('..')

def get_drugage():
    os.chdir('data')
    os.mkdir('drugage')
    os.chdir('drugage')
    fname_out = wget.download(cfg['data']['drug_age'])
    print(fname_out)
    unzip_file(fname_out)
    os.chdir('..')

# get_genage()
# get_drugage()

if __name__ == '__main__':
    app.run(main)