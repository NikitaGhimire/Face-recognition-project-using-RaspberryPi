import boto3

#connecting with s3
s3_client = boto3.client(
    's3', #Name of the service
    aws_access_key_id='', #add the aws access keyid
    aws_secret_access_key='' #add the secret access key
)

collectionId='facerecognitiondoorlock' #collection name

#connecting to amazon rekognition service
rek_client = boto3.client(
    'rekognition', #Name of the service
    aws_access_key_id='', #add the aws access keyid
    aws_secret_access_key='', #add the secret access key
    region_name='' #add region name
)

bucket='face-recognition-doorlock-system' #add name of the bucket
all_objects = s3_client.list_objects(Bucket = bucket)

#delete existing collection if it exists

list_response=rek_client.list_collections(MaxResults=2)

if collectionId in list_response['CollectionIds']:
    rek_client.delete_collection(CollectionId = collectionId)

#create new collection 

rek_client.create_collection(CollectionId = collectionId)

#add all images in current bucket to the collection ,using folder name as the label

for content in all_objects['Contents']:
    collection_name,collection_image= content['Key'].split('/')
    if collection_image:
        label = collection_name
        print('Indexing:', label)
        image = content['Key']
        index_response = rek_client.index_faces(
                        CollectionId= collectionId,
                        Image={'S3Object': {'Bucket' :bucket, 'Name': image}},
                        ExternalImageId=label,
                        MaxFaces=1,
                        QualityFilter="AUTO",
                        DetectionAttributes=['ALL'])
        print('FaceId:', index_response['FaceRecords'][0]['Face']['FaceId'])

