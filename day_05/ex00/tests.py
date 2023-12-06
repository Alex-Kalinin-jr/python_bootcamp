import subprocess

def Test(input: str, desired: str) -> None:
  output = subprocess.check_output(input, shell=True, universal_newlines=True)
  print(output)
  try:
    assert output == desired
    print("passed")
  except:
    print("failed")


def Main():
  Test('curl "http://localhost:8888/?species=Unit%20P"', "'Unit P': not found")
  Test('curl "http://localhost:8888/?species=Unit%20G"', "'credentials': lvl 4")
  Test('curl -X POST http://localhost:8888', "POST: Method Not Allowed")


if __name__ == '__main__':
  Main()