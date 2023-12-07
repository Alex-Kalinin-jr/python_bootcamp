from __future__ import print_function
import sys
sys.path.append('proto_files')
import grpc
import definition_pb2
import definition_pb2_grpc
from google.protobuf.json_format import MessageToDict
from pydantic import BaseModel
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('coords', nargs='+', type = str)


def output_response_human_friendly(response):
  for item in response:
     response_dict = MessageToDict(item)
     print(response_dict)


def run(input_coords):
  with grpc.insecure_channel("localhost:50051") as channel:
    stub = definition_pb2_grpc.RouteGuideStub(channel)
    response = stub.GetFeature(definition_pb2.coords(coords=input_coords))
    output_response_human_friendly(response)


if __name__ == "__main__":
  args = parser.parse_args()
  input_coords = ','.join(x for x in args.coords)
  run(input_coords)
