import os

from flask import Flask, g, request
from yaml import load as load_yaml

'''
Establish configuration.
'''
config_file = os.environ.get('MULTIWORLD_SERVER_CONFIGFILE', os.path.dirname(os.path.realpath(__file__)) + '../../config.yaml')
if not os.path.isfile(config_file):
    print('Failed to find the configuration file; is it missing? Should be in the root folder of the installation.')
    exit(1)
with open(config_file, 'r') as loaded_config:
    config = load_yaml(loaded_config)

DATABASE = config['database']
DEBUG = config['debug']

'''
Start the application.
'''
application = Flask(__name__)
application.config.from_object(__name__)

'''
Aaaaand go!
'''
if __name__ == '__main__':
    application.run(host='0.0.0.0')
