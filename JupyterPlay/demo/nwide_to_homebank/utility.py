import configparser
import os
from pathlib import Path


class MissingEnvironmentVariableError(Exception):
    """Custom exception for missing environment variables."""
    pass


def create_config():
    config = configparser.ConfigParser()
    config['General'] = {'debug': True, 'log_level': 'info'}
    config['Database'] = {'db_name': 'example_db',
                          'db_host': 'localhost', 'db_port': '5432'}
    config['TransactionConfig'] = {
        'cc_txn_source_path': r'nonsense', 'x': '22', 'y': '44'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def read_config(config_file):
    config = configparser.ConfigParser()
    print("######### File Path:", Path(__file__).absolute())
    # Directory of current working directory, not __file__
    print("######### Directory Path:", Path().absolute())

    config.read('./config.inix')
    cc_txn_source_path = config.get('TransactionConfig', 'cc_txn_source_path')

    config_values = {
        'cc_txn_source_path': cc_txn_source_path
    }
    return config_values


def load_env_config():
    ''' 
    Load environment variables. There is no default, as I never want to 
    accidentally pick a wrong value.
    Windows: rundll32.exe sysdm.cpl,EditEnvironmentVariables
    and to check: [Get-ChildItem Env:] (note end :)
    '''
    config = {
        'cc_txn_source_path': os.getenv('cc_txn_source_path')
    }
    return config


def set_env_var(key, value):
    '''
    Set an environment variable. This is only called for 
    testing purposes, but WILL CORRUPT THE ENVIRONMENT
    # Example usage
    set_env_var('SETTING1', 'test_value')
    '''
    os.environ[key] = value



def read_env_var(config, key):
    """Read an environment variable and throw an exception if it does not exist."""
    if key not in config or config[key] is None:
        raise MissingEnvironmentVariableError(
            f"Environment variable '{key}' is not set.")
    return config[key]


# main
c = load_env_config()
cc_txn_source_path = read_env_var(c, 'cc_txn_source_path')
# Get-ChildItem Env:
print(cc_txn_source_path)
