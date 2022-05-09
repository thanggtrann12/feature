broker_information = {
    'host': 'localhost',
    'port': 1883,
    'user': '',
    'password': '',
    'retain': False
}


def set_info(host, port, user, password, retain):
    """Set the info to the textboxs"""
    broker_information['host'] = host
    broker_information['port'] = port
    broker_information['user'] = user
    broker_information['password'] = password
    broker_information['retain'] = retain


def get_info():
    """Get the info from the textboxs"""
    return broker_information
