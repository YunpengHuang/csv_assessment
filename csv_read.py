import logging
import csv
import os

import yaml

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('csv_to_yaml.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# input from commandline
input_csv_filename = "csv_text.csv"  # input("input filename or the directory to the filename : ")
output_yaml_filename = "csv_result.yaml"  # input("output filename or the directory of the output : ")
try:
    if os.path.getsize(input_csv_filename) > 0 and input_csv_filename.lower().endswith(
            ".csv") and output_yaml_filename.lower().endswith(".yaml"):
        # DictReader will always convert to string
        # (another option would to use pandas which tries to automatically detect datatype of each column)
        input_csv = csv.DictReader(open(input_csv_filename))

        # convert division and point to integer
        new_input_csv = []
        for entries in input_csv:
            entries["division"] = int(entries["division"])
            entries["points"] = int(entries["points"])
            new_input_csv.append(entries)

        # sort based on division (acs) and points (desc) (top 3 in the entries)
        data = sorted(new_input_csv, key=lambda x: (x["division"], -x["points"]))[:3]

        print(data)


        def convert_to_yaml_format(dictionary):
            """put data into a YAML recognisable format"""
            temp_dict_list = []
            data_test = {}
            for items in dictionary:
                temp_dict = {
                    "detail": "In division " + str(items["division"]) + " from " + items["date"] + " performing " +
                              items[
                                  "summary"], "name": items["firstname"] + " " + items["lastname"]}
                temp_dict_list.append(temp_dict)

            data_test['record'] = temp_dict_list
            return data_test


        # output as YAML format
        top_three_records = convert_to_yaml_format(data)
        with open(output_yaml_filename, "w") as output_file:
            yaml.dump(top_three_records, output_file, default_flow_style=False)

        logger.debug('input: {}, output: {}'.format(input_csv_filename, output_yaml_filename))
    else:
        logger.warning('input: {}, output: {}'.format(input_csv_filename, output_yaml_filename))
        print("file is empty or filename is not named correctly")
except OSError as e:
    logger.warning('input: {}, output: {}'.format(input_csv_filename, output_yaml_filename))
    print("file does not exist")
