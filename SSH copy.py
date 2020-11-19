
from aliases import *
import config
import os

""" Convert strings to dicts """

input_aliases_list = [alias for alias in input_aliases.split("\n") if alias != '']
output_aliases_list = [alias for alias in output_aliases.split("\n") if alias != '']

input_aliases_dict = dict(x.strip().split("=") for x in input_aliases_list)
output_aliases_dict = dict(x.strip().split("=") for x in output_aliases_list)


def aliases():
	if input_file.isdigit():
		input_file_result = list(input_aliases_dict.values())[int(input_file)-1]
	elif input_file in input_aliases_dict.keys():
		input_file_result = input_aliases_dict[input_file]
	else:
		input_file_result = input_file

	if output_file.isdigit():
		ouput_file_result = list(output_aliases_dict.values())[int(output_file)-1]
	elif output_file in output_aliases_dict.keys():
		ouput_file_result = output_aliases_dict[output_file]
	else:
		ouput_file_result = output_file

	return input_file_result, ouput_file_result

try:
	print("\nEnter 'aliases' to edit aliases\nExisting input aliases:\n")
	for counter,v in enumerate(input_aliases_dict.items(),1):
		print(f"{counter}. {': '.join(v)}")
	print()
	input_file = input('Enter file path or alises (or alias number) to send to server: ')
	if input_file == "aliases":
		os.system(f"nano {config.your_aliases_file_path}")
	else:
		print("\nExisting loaction aliases:\n")
		for counter,v in enumerate(output_aliases_dict.items(),1):
			print(f"{counter}. {': '.join(v)}")
		print()
		output_file = input('Where on a server i should place your file (path / alias / alias number?): ')
		input_file, output_file = aliases()
		os.system(f"scp {input_file} {config.your_ssh_home_path}/{output_file}")
		os.system("exit")
except KeyboardInterrupt:
	print("\n\nCancelled :)")
