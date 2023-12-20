from picamera import PiCamera
import time
import boto3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Initialize PiCamera
P = PiCamera()
P.resolution = (800, 600)
P.start_preview()

directory = '/home/pi/Desktop/FaceRecognition-main/Face'

# Configure AWS credentials and region
aws_access_key_id = 'enter awas access key id'
aws_secret_access_key = 'aws secret access key'
region_name = 'region name of your bucket'

# Configure email notification details
sender_email = 'enter sender email address'
sender_password = 'password of the senders email address'
recipient_email = 'recipient email address'
subject = 'Door Unlock Notification'
body = 'Someone is at the door trying to gain access'

# Initialize the Amazon Rekognition client
rek_client = boto3.client(
    'rekognition',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

def send_email_notification(sender_email, sender_password, recipient_email, subject, body, image_path):
    # Create a multipart message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the image
    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read())
        image.add_header('Content-Disposition', 'attachment', filename='image.jpg')
        message.attach(image)

    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        # Create a secure connection to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print('Email notification sent successfully!')
    except smtplib.SMTPException as e:
        print('Failed to send email notification. Error:', str(e))

if __name__ == "__main__":
    time.sleep(2)

    milli = int(round(time.time()*1000))
    image_path = '{}/image_{}.jpg'.format(directory, milli)
    P.capture(image_path)
    print('Captured:', image_path)

    try:
        match_response = rek_client.search_faces_by_image(CollectionId='facerecognitiondoorlock',
                                                          Image={'Bytes': open(image_path, 'rb').read()},
                                                          MaxFaces=1,
                                                          FaceMatchThreshold=85)
        if match_response['FaceMatches']:
            print('Hello,', match_response['FaceMatches'][0]['Face']['ExternalImageId'])
            print('Similarity:', match_response['FaceMatches'][0]['Similarity'])
            print('Confidence:', match_response['FaceMatches'][0]['Face']['Confidence'])
            send_email_notification(sender_email, sender_password, recipient_email, subject, body, image_path)
        else:
            print('No face matched!!')
            send_email_notification(sender_email, sender_password, recipient_email, subject, body, image_path)

            
            
    except:
        print('No face detected!!')
        

    time.sleep(1)
