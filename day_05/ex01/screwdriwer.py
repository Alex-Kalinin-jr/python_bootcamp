import argparse
import requests


URL_GET = 'http://localhost:8888/list/'
URL = 'http://localhost:8888/'


def PostFiles(files: list)->None:
  for file in files:
    try:
      response = requests.post(URL, files={'file': open(file, 'rb')})
      if response:
        print(f'File {file} uploaded successfully')
    except:
      pass


def GetData() -> list:
  response = requests.get(URL_GET).json()
  return response

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('upload', nargs='*', default=False, help='upload a file')
  parser.add_argument('list', nargs='?',default=False, help='list all uploaded files')
  args = parser.parse_args()

  if args.upload:
    files = args.upload
    PostFiles(files)

  if args.list:
    data = GetData()
    if data['files']:
      print('Files:')
      counter = 1
      for file in data['files']:
        print(f'{counter}. - {file}')
        counter += 1
    else:
      print('Response failed')


if __name__ == '__main__':
  main()