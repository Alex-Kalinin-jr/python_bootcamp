import sys
sys.path.append('proto_files')
from concurrent import futures
import grpc
import definition_pb2
import definition_pb2_grpc
import random
import dataset


def CreateOfficers()->list:
  list_of_officiers = []
  for _ in range (random.randint(0, 9)):
    list_of_officiers.append(definition_pb2.Officer(firstname=random.choice(dataset.name), 
                                                    lastname=random.choice(dataset.lastname), 
                                                    rank=random.choice(dataset.rank)))
  return list_of_officiers


def FormOutput(data):
  return definition_pb2.ShipData(
    alignment=random.choice(definition_pb2.Alignment.keys()),
    name = data[0],
    ship_class = data[1],
    size=random.randint(dataset.types_data[data[1]][0][0], 
                        dataset.types_data[data[1]][0][1]),
    armed=random.choice([True, False]) if dataset.types_data[data[1]][1] else False,
    officer=CreateOfficers(),
    status = random.choice(['Ours', 'Enemy']) if dataset.types_data[data[1]][2] and data[0] != 'Unknown' else 'Enemy'
  )


class RouteGuideServicer(definition_pb2_grpc.RouteGuideServicer):
  def GetFeature(self, request, context):
    if request.coords in dataset.space_map.keys():
      for i in dataset.space_map[request.coords]:
        yield FormOutput(i)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    definition_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

