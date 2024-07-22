import cv2
import time


cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)
cap.set(10, 70)

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

def traffic_light():
    classNames = []
    classFile = 'coco.data'
    with open(classFile, 'rt') as f:

        classNames = f.read().rstrip('\n').split('\n')

    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    font = cv2.FONT_HERSHEY_COMPLEX


    def red_signal_image_mail_sender():
        strFrom = 'eeswarofficial@gmail.com'
        strTo = 'eshwarem26@gmail.com'

        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'ALERT VIOLATION DETECT ON TRAFFIC '
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)
        mail_message_Text = MIMEText('VEHICLE VIOLATION DETECT FINE 500')
        msgAlternative.attach(mail_message_Text)
        sending_image = open('VEHICLE.jpg', 'rb')
        msgImage = MIMEImage(sending_image.read())
        sending_image.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('eshwarem26@gmail.com', 'cvdhhnzfmbtoeacx')
        print("mail id and password correct")
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        print("mail send")
        smtp.quit()

    def mobile_image_mail_sender():
        strFrom = 'eshwarem26@gmail.com'
        strTo = 'eshwarem26@gmail.com'

        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'ALERT VIOLATION DETECT ON TRAFFIC '
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)
        mail_message_Text = MIMEText('VEHICLE VIOLATION DETECT FINE 500')
        msgAlternative.attach(mail_message_Text)
        sending_image = open('mobile.jpg', 'rb')
        msgImage = MIMEImage(sending_image.read())
        sending_image.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('eshwarem26@gmail.com', 'cvdhhnzfmbtoeacx')
        print("mail id and password correct")
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        print("mail send")
        smtp.quit()

    def red_function():
        add_red = 15
        for count in range(0, 15):

            add_red = add_red - 1
            success, img = cap.read()
            classIds, confs, bbox = net.detect(img, confThreshold=0.45)

            print(add_red)

            if len(classIds) != 0:

                for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):

                    object_name = (classNames[classId - 1])
                    object_id = [classId - 1]

                    if object_id == [2]:
                        print("signal violated  vehicle detected  ")
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imwrite("VEHICLE.jpg", img)
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        red_signal_image_mail_sender()

                    if object_id == [3]:
                        print(" signal violated vehicle detected  ")
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imwrite("VEHICLE.jpg", img)
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        red_signal_image_mail_sender()

                    if object_id == [4]:
                        print(" signal violated vehicle detected  ")
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imwrite("VEHICLE.jpg", img)
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        red_signal_image_mail_sender()

                    if object_id == [76]:
                        print(" mobile usage detected  ")
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imwrite("mobile.jpg", img)
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        mobile_image_mail_sender()

            cv2.putText(img, "RED-SIGNAL", (170, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            # cv2.putText(img, 'cse-department', (00, 430), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
            # cv2.putText(img, 'Divya , Archana', (00, 470), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(img, "Timer=", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(img, str(add_red), (350, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.circle(img, (100, 70), 20, (0, 0, 255), 80)

            time.sleep(1)
            cv2.imshow("display", img)
            cv2.waitKey(1)

    # yellow_function()


    def yellow_function():

        add_yellow = 15

        for count in range(0, 15):

            success, img = cap.read()
            add_yellow = add_yellow -1
            print("yellow_signal=")
            print(add_yellow)
            classIds, confs, bbox = net.detect(img, confThreshold=0.45)

            if len(classIds) != 0:

                for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):

                    object_name = (classNames[classId - 1])
                    object_id = [classId - 1]

                    if object_id == [76]:
                        print(" mobile usage detected  ")
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (0, 255, 0), 2)
                        cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imwrite("mobile.jpg", img)
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        mobile_image_mail_sender()

            cv2.putText(img, "Timer=", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.putText(img, str(add_yellow), (350, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.circle(img, (100, 70), 20, (0, 255, 255), 80)
            cv2.putText(img, "YELLOW-SIGNAL", (170, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            # cv2.putText(img, 'cse-department', (00, 430), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
            # cv2.putText(img, 'Divya , Archana', (00, 470), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

            time.sleep(1)
            cv2.imshow("display",img)
            cv2.waitKey(1)

        print("yelowwww--------yellow-----end")
        red_function()




    while (1):

        add_green = 15

        for count1 in range(0, 15):

            success, img = cap.read()
            add_green = add_green - 1
            print(add_green)
            classIds, confs, bbox = net.detect(img, confThreshold=0.45)

            if len(classIds) != 0:

                for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):

                    object_name = (classNames[classId - 1])
                    object_id = [classId - 1]

                    if object_id == [76]:
                        print(" mobile usage detected  ")
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (0, 255, 0), 2)
                        cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imwrite("mobile.jpg", img)
                        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                        mobile_image_mail_sender()
            cv2.putText(img, "Timer=", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, str(add_green), (350, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.circle(img, (100, 70), 20, (0, 255, 0), 80)
            cv2.putText(img, "GREEN-SIGNAL", (170, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            # cv2.putText(img, 'cse-department', (00, 430), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
            # cv2.putText(img, 'Divya , Archana', (00, 470), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

            time.sleep(1)
            cv2.imshow("display", img)
            cv2.waitKey(1)

        print("green-----Green---------- end")

        yellow_function()

def no_parking():

    def no_parking_mail_sender():

        strFrom = 'eshwarem26@gmail.com'
        strTo = 'eshwarem26@gmail.com'

        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'NO-PARKING VEHICLE DETECTED '
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)
        mail_message_Text = MIMEText('VEHICLE NO-PARKING DETECT FINE 100')
        msgAlternative.attach(mail_message_Text)
        sending_image = open('NO_PARK_VEHICLE.jpg', 'rb')
        msgImage = MIMEImage(sending_image.read())
        sending_image.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('eshwarem26@gmail.com', 'cvdhhnzfmbtoeacx')
        print("mail id and password correct")
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        print("mail send")
        smtp.quit()

    cap.set(3, 1280)
    cap.set(4, 720)
    cap.set(10, 70)

    classNames = []
    classFile = 'coco.data'
    with open(classFile, 'rt') as f:

        classNames = f.read().rstrip('\n').split('\n')

    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    font = cv2.FONT_HERSHEY_COMPLEX



    while(1):

        success, img = cap.read()
        classIds, confs, bbox = net.detect(img, confThreshold=0.45)



        if len(classIds) != 0:

            for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):

                object_name = (classNames[classId - 1])
                object_id = [classId - 1]

                if object_id == [2]:
                    print("NO-PARKING vehicle detected  ")
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imwrite("NO_PARK_VEHICLE.jpg", img)
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    no_parking_mail_sender()

                if object_id == [3]:
                    print(" NO-PARKING  vehicle detected  ")
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imwrite("NO_PARK_VEHICLE.jpg", img)
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    no_parking_mail_sender()

                if object_id == [4]:
                    print(" NO-PARKING  vehicle detected  ")
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imwrite("NO_PARK_VEHICLE.jpg", img)
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    no_parking_mail_sender()

        cv2.putText(img, "NO-PARKING VEHICLE", (170, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.line(img, (50, 60), (150, 100), (0,0,255), 5)

        cv2.circle(img, (100, 70), 50, (0, 0, 255), 20)

        time.sleep(1)
        cv2.imshow("display", img)
        cv2.waitKey(1)

user=input("Enter mode of detection: ")
if user=='traffic':
    traffic_light()
elif user=='no_parking':
    no_parking()
else:
    print("Enter correct mode")
