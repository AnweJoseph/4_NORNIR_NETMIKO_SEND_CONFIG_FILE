from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_save_config
from nornir_utils.plugins.functions import print_result
import time


nr = InitNornir(config_file="config.yaml")

def execute_send_config():
	print("#######...SENDING...CONFIGURATION...COMMANDS...###########")
	time.sleep(5)
	results = nr.run(task=netmiko_send_config, config_file="commands")
	print_result(results)
	time.sleep(3)

def execute_save_config():
	print("#############...SAVING...CONFIGURATION...###############")
	time.sleep(5)
	results = nr.run(task=netmiko_save_config)
	print_result(results)
	time.sleep(3)

execute_send_config()
execute_save_config()
