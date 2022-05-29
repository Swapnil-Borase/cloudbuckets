from google.cloud import storage

if __name__ == '__main__':

    bucketname="swa-bucketpython1"
    storage_client=storage.Client()
    bucket=storage_client.bucket(bucketname)
    bucket.storage_class="STANDARD"
    new_bucket=storage_client.create_bucket(bucketname,location="US-EAST1")

    print("Succesfully created")