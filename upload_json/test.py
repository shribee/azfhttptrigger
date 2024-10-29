import os
import json
import datetime

from azure.storage.blob import ContainerClient


def _get_prices():
    folder_name = os.path.join(os.getcwd(), "data")
    local_file_name = os.path.join(folder_name, "price_points.json")
    
    with open(local_file_name, mode="w") as fp:
        prices = [{"name": "john", "age": "21"}]
        json.dump(fp=fp, obj=prices, indent=2)
        

def _move_file():
    url = os.getenv("URL")
    token = os.getenv("TOKEN")
    container_name = os.getenv("CONTAINER_NAME")
    container_client = ContainerClient(
        account_url=url,
        container_name=container_name,
        credential=token
    )
    folder_name = os.path.join(os.getcwd(), "data")
    local_file_name = os.path.join(folder_name, "price_points.json")
    fmt = "%Y/%m/%d/%H-%M-%S"
    destination_sub_folder_hierarchy = datetime.datetime.strftime(datetime.datetime.now(), fmt)
    destination_filename = f"orbital_pricing/{destination_sub_folder_hierarchy}"
    with open(file=local_file_name, mode="rb") as data:
        _ = container_client.upload_blob(
            name=destination_filename,
            blob_type="BlockBlob",
            data=data,
            overwrite=True
            )


if __name__ == '__main__':
    # folder_name = os.path.join(os.getcwd(), "data") 
    # print("Hello")
    # print(folder_name)
    _get_prices()
    _move_file()



