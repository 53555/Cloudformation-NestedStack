#!/bin/python3
import boto3
import sys
import platform


class Session:
    def __init__(self, profile_name, region_name, client_name):
        self.profile_name = profile_name
        self.region_name = region_name
        self.client_name = client_name

    def session(self):
        try:
            os_flavour = platform.platform()
            os_flavour = os_flavour.split("-")
            if "Ubuntu" in os_flavour:
                self.ses = boto3.session.Session(
                    profile_name=self.profile_name, region_name=self.region_name)
            else:
                self.ses = boto3.session.Session()
            
          #  print("session")
        except Exception as e:
            print(e)            
           # print("exception")
        return None

    def client(self):
        clnt = self.ses.client(self.client_name)
        return clnt


profile_name = sys.argv[1]
region_name = sys.argv[2]
client_name = "s3"


def listbucket():
    s3_obj.session()
    lb = s3_obj.client().list_buckets()
    lb = lb['Buckets']
    buck = []
    for i in lb:
       buck.append(i['Name'])
    return buck


def createBucket():
    s3_obj.session()
    s3_obj.client().create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': s3_obj.region_name
        }
    )
    print("Bucket name " + bucket_name + " created")
    return None


def main():
    lb = listbucket()
    if bucket_name in lb:
        print("Bucket name " + bucket_name + " already exist")
        pass
    else:
        createBucket()
    return None


if __name__ == '__main__':
    bucket_name = sys.argv[3]
    s3_obj = Session(profile_name, region_name, client_name)
   # s3_obj.session()
   # resp = s3_obj.client().get_caller_identity()
   # print(resp)
    main()
