import csv

import yaml
import operator

# DictReader will always convert to string
input_csv = csv.DictReader(open("csv_text.csv"))

# sort based on division and points (top 3 in the entries)
result = sorted(input_csv, key=lambda x: (x["division"], x["points"]))[:3]



# format that it needs to be in for it output in yaml
data = {
    'records': [
        {'detail': "In division 1 from 2018-01-02 performing Offensive Duties", 'name': "zelma Ivatt"},
        {'detail': "In division 1 from 2018-01-02 performing Offensive Duties", 'name': "zelma Ivatt"},
        {'detail': "In division 1 from 2018-01-02 performing Offensive Duties", 'name': "zelma Ivatt"},
    ],
}

with open("test.yaml", "w") as output_file:
    yaml.dump(data, output_file, default_flow_style=False)

    # with open("csv_result.yaml", "w") as output_file:
    #     for rows in range(3):
    #         yaml.dump(result[rows], output_file, default_flow_style=True)

    # firstname: string
    # lastname: string
    # date: String
    # division: Integer
    # points: Integer
    # summary: String

    # sort by division then by points
    # use dictionary python format
    # what needs to be validated only the sorting order
