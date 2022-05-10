from email.policy import default
from Utils.msg_pop_up import msgPopUp
from setting.mqtt.connect_mqtt import Create_connections
import time

broker_information = {
    'host': 'localhost',
    'port': 1883,
    'user': '',
    'password': '',
    'retain': False
}

default_host = {
    'host': 'driver.cloudmqtt.com',
    'port': 18675,
    'user': 'burlgbdf',
    'password':'0--UiYtSUWAZ',
    'retain': True
}

def set_info(self, host, port, user, password, retain):
    """Set the info to the textboxs"""
    if self.default_button.isChecked():
        broker_information['host'] = default_host['host']
        broker_information['port'] = default_host['port']
        broker_information['user'] = default_host['user']
        broker_information['password'] = default_host['password']
        broker_information['retain'] = default_host['retain']
       
        self.percent.setVisible(True)
        for percent in range(1, 10):
            self.percent.setValue(percent/10*100)
            time.sleep(1)
        self.percent.setVisible(False)   
        msgPopUp('Default broker is set.', 'info') 
        Create_connections(
            broker=broker_information['host'],
            port=broker_information['port'],
            username_=broker_information['user'],
            password_=broker_information['password'])
    else:
        
        broker_information['host'] = host
        broker_information['port'] = port
        broker_information['user'] = user
        broker_information['password'] = password
        broker_information['retain'] = retain
        
        self.percent.setVisible(True)
        for percent in range(1, 10):
            self.percent.setValue(percent/10*100)
            time.sleep(1)
        self.percent.setVisible(False)
        msgPopUp('MQTT broker information set', 'success')
        Create_connections(
            broker=broker_information['host'],
            port=broker_information['port'],
            username_=broker_information['user'],
            password_=broker_information['password'])
    self.txt_host.setText('')
    self.txt_port.setText('')
    self.txt_username.setText('')
    self.txt_password.setText('')
    self.retain_checkbox.setChecked(False)


def get_info(self):
    """Get the info from the textboxs"""
    self.txt_host.setText(broker_information['host'])
    self.txt_port.setText(str(broker_information['port']))
    self.txt_username.setText(broker_information['user'])
    self.txt_password.setText(broker_information['password'])
    self.retain_checkbox.setChecked(broker_information['retain'])
    msgPopUp('MQTT broker information get', 'success')


