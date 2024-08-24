import configparser

def create_config():
    config = configparser.ConfigParser()
    config['General'] = {'debug': True, 'log_level': 'info'}
    config['Database'] = {'db_name': 'example_db',
                          'db_host': 'localhost', 'db_port': '5432'}
    config['TransactionConfig'] = {
        'cc_txn_source_path': r'nonsense', 'x': '22', 'y': '44'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def read_config():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    cc_txn_source_path = config.get('TransactionConfig', 'cc_txn_source_path')

    config_values = {
        'cc_txn_source_path': cc_txn_source_path
    }
    return config_values