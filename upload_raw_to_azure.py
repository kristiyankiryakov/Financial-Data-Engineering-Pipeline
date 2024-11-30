from access_vault import service_client
from datetime import datetime

current_date = datetime.now().strftime('%Y%m%d')
local_file = 'raw_stocks.csv'
destination = f'stocks/raw_stocks_{current_date}.csv'


def upload_file(container_name:str, local_file_path:str, destination_path:str):
     file_system_client = service_client.get_file_system_client(file_system=container_name)
     file_client = file_system_client.get_file_client(destination_path)

     with open(local_file_path, 'rb') as file:
          file_client.upload_data(file, overwrite=True)


upload_file('rawdata', local_file, destination)
print(f'Successfully uploaded {local_file} to {destination}')