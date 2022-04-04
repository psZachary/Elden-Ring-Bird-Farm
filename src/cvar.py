import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\config.ini")

load_time = config['DEFAULT']['load_time']
toggle_farm_key = config['DEFAULT']['toggle_farm_key']
exit_program_key = config['DEFAULT']['exit_program_key']
farm_running = False
