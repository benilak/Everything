import PyPDF2
import textract
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
import nltk
# this is here as a fix to some errors and missing files involving the package 'nltk'
# probably machine-specific
nltk.download('punkt')
nltk.download('stopwords')

import csv

# most of this code was taken from the web somewhere - a tutorial on how to convert a pdf file into a csv file

'''Read PDF File'''
# write a for-loop to open many files -- leave a comment if you'd #like to learn how
bible = '/Users/brycekaline/Desktop/Bible_King_James_Version.pdf'
#open allows you to read the file
pdfFileObj = open(bible,'rb')
# The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfReader.numPages
count = 0
text = ""
# The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
# This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
# If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
else:
   text = textract.process(bible, method='tesseract', language='eng')
# Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
# Now, we will clean our text variable, and return it as a list of keywords.

'''Convert text into keywords'''
# The word_tokenize() function will break our text phrases into #individual words
tokens = word_tokenize(text)
# we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',']
# We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
stop_words = stopwords.words('english')
# We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in punctuations]

'''with open('/Users/brycekaline/Desktop/Bible.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(keywords)'''

with open('/Users/brycekaline/Desktop/Bible.csv', 'w') as f:
    writer = csv.writer(f)
    for word in keywords:
        writer.writerow([word])

# print(keywords[0:1000])


