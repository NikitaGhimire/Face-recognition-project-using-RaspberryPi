from picamera import PiCamera
import time
import boto3

directory = '/home/nikita/Desktop/Face Recognition Door Lock/Faces'

P = PiCamera()
P.resolution = (800, 600)
P.start_preview()

collectionId = 'facerecognitiondoorlock'

# connecting to amazon rekognition service
rek_client = boto3.client(
    'rekognition',  # Name of the service
    aws_access_key_id='',  # add the aws access keyid
    # add the secret access key
    aws_secret_access_key='',
    region_name=''  # add region name
)

if __name__ == "__main__":
    time.sleep(2)

    milli = int(round(time.time()*1000))
    image = '{}/image_{}.jpg'.format(directory.milli)
    P.capture(image)
    print('Captured :' + image)
    with open(image, 'rb') as image:
        try:
            match_response = rek_client.search_faces_by_image(CollectionId=collectionId,
                                                              Image={
                                                                  'Bytes': image.read()},
                                                              MaxFaces=1,
                                                              FaceMatchThreshold=85)
            if match_response['FaceMatches']:
                print(
                    'Hello,', match_response['FaceMatches'][0]['Face']['ExternalImageId'])
                print('Similarity :',
                      match_response['FaceMatches'][0]['Similarity'])
                print('Confidence :',
                      match_response['FaceMatches'][0]['Face'], ['Confidence'])
            else:
                print('No face matched!!')
        except:
            print('No face detected!!')

        time.sleep(1)
