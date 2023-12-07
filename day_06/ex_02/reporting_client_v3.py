from google.protobuf.json_format import MessageToDict, MessageToJson
from pydantic import ValidationError
from copy import deepcopy

import argparse
import sys

sys.path.append('../ex01')
sys.path.append('../ex00/proto_files')
import sql_entities
import validator
import grpc
import definition_pb2
import definition_pb2_grpc


parser = argparse.ArgumentParser()
parser.add_argument('coords', nargs='*', type=str)
parser.add_argument('--scan', action='store_true', default=False, help='Enable scanning')
parser.add_argument('--list_traitors', action='store_true', default=False, help='')


#***********************************************************************
#***********************************************************************

def find_traitors(crew):
   crew = deepcopy(crew)
   for first in crew:
      for second in crew:
         if first[0] == second[0] \
          and first[1] == second[1] \
          and first[2] == second[2] \
          and first[3] != second[3] \
          and first[3] == 'Unknown' or second[3] == 'Unknown':
            print(first)
            print(second)
            crew.remove(first)
            crew.remove(second)


def output_response_human_friendly(response):
  for item in response:
    response_dict = MessageToDict(item, including_default_value_fields=True)
    try:
      person = validator.ShipData(**response_dict)
    except ValidationError as e:
      print(e)
    print(response_dict)


def run(input_coords, session_data):
  with grpc.insecure_channel("localhost:50051") as channel:
    stub = definition_pb2_grpc.RouteGuideStub(channel)
    response = stub.GetFeature(definition_pb2.coords(coords=input_coords))
    for item in response:
      sql_entities.add_data(item, session_data)


if __name__ == "__main__":
    args = parser.parse_args()
    session_data = 'postgresql://postgres:password@localhost:5431/postgres'

    if args.scan:
        if args.coords:
          input_coords = ','.join(x for x in args.coords)
          run(input_coords, session_data)
        else:
            print("No coordinates provided")
    if args.list_traitors:
      rows = sql_entities.recieve_data(session_data)
      find_traitors(rows)
