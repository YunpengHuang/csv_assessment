import csv

import yaml
import operator

# DictReader will always convert to string
input_csv = csv.DictReader(open("csv_text.csv"))

# sort based on division and points (top 3 in the entries)
data = sorted(input_csv, key=lambda x: (x["division"], x["points"]))[:3]


def convert_to_yaml_format(dictionary):
    temp_dict_list = []
    data_test = {}
    for items in dictionary:
        temp_dict = {"detail": "In division " + items["division"] + " from " + items["date"] + " performing " + items[
            "summary"], "name": items["firstname"] + " " + items["lastname"]}
        temp_dict_list.append(temp_dict)

    data_test['record'] = temp_dict_list
    return data_test


top_three_records = convert_to_yaml_format(data)
with open("test.yaml", "w") as output_file:
    yaml.dump(top_three_records, output_file, default_flow_style=False)
