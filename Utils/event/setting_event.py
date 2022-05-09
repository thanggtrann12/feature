from setting.setting import mqtt_setting, network_setting


def setting_button_event(self):
    self.setting_mqtt.triggered.connect(lambda: mqtt_setting.mqtt_setting())
    self.setting_network.triggered.connect(lambda: network_setting.network_setting(self))