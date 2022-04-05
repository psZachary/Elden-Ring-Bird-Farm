import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\config.ini")

load_time = config['SETTINGS']['load_time']
toggle_farm_key = config['SETTINGS']['toggle_farm_key']
exit_program_key = config['SETTINGS']['exit_program_key']
rest_at_grace_interval = config['SETTINGS']['rest_at_grace_interval']
rest_at_grace_counter = 0
farm_running = False
