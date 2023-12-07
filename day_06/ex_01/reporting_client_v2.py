import sys
import grpc
from google.protobuf.json_format import MessageToDict
import argparse
from pydantic import ValidationError

sys.path.append('../ex00/proto_files')
import validator
import definition_pb2
import definition_pb2_grpc


parser = argparse.ArgumentParser()
parser.add_argument('coords', nargs='+', type = str)


def output_response_human_friendly(response):
  for item in response:
    response_dict = MessageToDict(item, including_default_value_fields=True)
    try:
      person = validator.ShipData(**response_dict)
    except ValidationError as e:
      print(e)
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
