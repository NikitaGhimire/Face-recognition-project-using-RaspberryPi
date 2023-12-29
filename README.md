# Face-recognition-project-using-RaspberryPi

A face recognition door lock model using Raspberry Pi has been created that is correctly able to identify the authority of the visitors, if they are recognised visitors or not and is accurately able to give access or restrict access based on the authority. In particular, the designed model is can accurately achieve the following:

- Motion detection: The entire operation of the smart door lock operates only if the PIR sensor detects movement within its’ detection zone. Hence, it is of utmost importance that sensor is operating normally and the sensitivity and delay before firing is adjusted as required. Likewise, the sensor is not able to detect stationary or still objects because of its detection mechanism and it should also be noted that the only way to retrigger the sensor is if the object in radar moves again or there is another movement.

- Face detection and image capture: When the camera is activated upon motion detection, the Pi camera can auto focus on the face of the visitor and the image captured is of right precision for the Amazon S3 and Amazon Rekognition service to identify the visitor.
  
- Face analysis and recognition: Consecutively, once the image is captured, Amazon S3 and ‘Amazon Rekognition’ is able to load any authorised face in the database and accurately produce output. The whole idea of the proposed system depends on the fact that the Amazon S3 and Amazon Rekognition can distinguish authorised users from other. Therefore, it is a functional requirement that the module is accurate, up to date and functioning properly.
  
- Database Management: It is a functional requirement that the database is up to date and the owner can manually review and manage the database of the authorised visitors as needed anytime.
- Door lock and unlock system: Completion of a single operation of the proposed system is determined only if the door is unlocked or remains closed. Hence, the communication between the system and the component must be correct and ideal.
  
- Notification system: Notification system adds an extra layer of security to the proposed system by keeping a record of the authorised visitors and possible intruders. It is a functional requirement that the homeowner is always in check of who is accessing the property and when, to maintain home security and assess, report and act upon any potential threats timely.
