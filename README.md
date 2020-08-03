"# rk307_team_sphynx" 
SIH- RK307- SPHYNX
Project Title: Prevention of Emotional Entrapment of girls on Social Media Platforms.

Our Project consists of 2 major functionalities:
1. Age Detection for filtering out teenagers(using DNN(21)) and
2. Predicting for grooming or non grooming charecteristics in the conversations between teenagers and adult male(using svm classifier).  

The following files have been used for the project:

1.fchatroom.py: This module has the chatroom code and performs all the Backend operations including the DB commands.

2.login.html: The html page for login into chatroom.

3.session.html: Front end code for chatroom.

4.age1.py: The module for age detection using DNN(21).

5.dnn1.py: DNN training.

6.svm.py: Has the svm classifier code for detecting if the conversation is grooming or not.

7.svmtest.py: For testing the svm classifier.

8.metrics.py: Accuracy detection.

9.mail.py: Used for sending alert messages to the respective authorities.

10.bigdic.dic: The dictionary of all english words, including slang words and the coressponding stages.
