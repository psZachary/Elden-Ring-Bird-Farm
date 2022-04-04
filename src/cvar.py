#parse config ini
import configparser

config = configparser.ConfigParser()
config.read('..\config.ini')

load_time = config['DEFAULT']['load_time']
toggle_farm_key = config['DEFAULT']['toggle_farm_key']
exit_program_key = config['DEFAULT']['exit_program_key']

farm_running = False