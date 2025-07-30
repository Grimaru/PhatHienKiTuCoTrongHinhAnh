### My own project for the Graduation Thesis.
###
### By: Grimaru (I did it alone even though I had a chance to have one more member for this project)
###
### Instructor: Assoc. Prof. PhD. Nguyen Thanh Binh (email: binhnt1@huflit.edu.vn)
###
### Email: rinnenguyenlife4u@gmail.com (sub: 22dh112315@st.huflit.edu.vn)
###
### The topic is to detect characters in images using appropriate methods.
###
###
#### Normally, when I go to refer to some demos of Vietnamese coders, they will use specialized detection models such as Yolo and focus on recognizing text in images using OCR libraries (easyOCR, keras-OCR or PaddleOCR)
####
#### For me, I feel that OCR libraries all have a detection model along with a recognition model. And because of that 2-in-1, I only use the OCR library (Optical Character Recognition library) to do this project (but because my topic is about Text Detection, I will focus more on it)
####
#### I use 3 libraries: PaddleOCR, easyOCR and Keras-OCR. All of them give excellent text detection results (lowest around 80-85% or lower, highest around 99%)
####
#### For each library, I also do data mining which is sequential pattern mining (this is just an example of Text Detection application so I don't really care about it).
####
#### Here, I only focus on detecting and extracting text from images into .csv files (output will be bill_sequences (library's name).csv) and besides PaddleOCR (main), I edited EasyOCR and KerasOCR myself outside to save time (because I only care about extracting text from images more than actually preprocessing data for data mining)
####
#### I have set requirements for PaddleOCR and Keras-OCR. I run PaddleOCR locally on Python 3.11 and Keras-OCR locally on Python 3.9. As for easyOCR and the sequential pattern mining application, I run them on Google Colab to save resources locally.
####
#### I made two files: 
##### .ipynb: three models in different environments with using for 1 letters (two versions: full + voice, detection only); 1 whole bill (two versions: full + voice, detection only) and data mining for 10 bills 
##### .py: only use the main model - PaddleOCR. The process order includes:
###### 1. Put the image in and use PaddleOCR then output the detected image
###### 2. Generate English Texts
###### 3. English Voice
###### 4. Translate into Vietnamese
###### 5. Vietnamese Texts
###### 6. Vietnamese Voice
