import os
import sys
from pprint import pprint

current_path = os.path.dirname(__file__)
if sys.path:
    sys.path.append(current_path)

from solver.reader import FileInputReader
from solver.parser import JsonParseInput
from solver.grouping_information import GroupingInformation


def main():
    current_path = os.path.dirname(__file__)
    json_path = os.path.join(current_path, 'input.json')
    file_input_reader = FileInputReader(json_path)
    json_parse_input = JsonParseInput(file_input_reader)
    grouping_information = GroupingInformation(json_parse_input)
    teams = grouping_information.get_grouping()
    pprint(teams)

if __name__ == '__main__':
    main()
