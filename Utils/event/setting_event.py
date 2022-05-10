from setting.setting import mqtt_setting, network_setting, serial_setting


def setting_button_event(self):
    self.setting_mqtt.triggered.connect(
        lambda: mqtt_setting.mqtt_setting(self))
    self.setting_network.triggered.connect(
        lambda: network_setting.network_setting(self))
    self.setting_serial.triggered.connect(
        lambda: serial_setting.serial_setting(self))
