import os
from sys import argv
import database
import utilities
import micr
import imageExtractor
import handWritingRecognition
import signatureVerification


# Current Working Directory
currentWorkingDir = os.path.dirname(os.getcwd())
currentWorkingDir = os.path.join(currentWorkingDir, "cheque-verification")
print("hellllloooooooo")

# Connecting to Database
db = database.Database(currentWorkingDir)

# Receiver Account Number
receiverAccountNumber = int(argv[2])
print(receiverAccountNumber)


# Image Path
imageDir = currentWorkingDir + "/cheque_images"
imagePath = os.path.join(imageDir, argv[1])

# MICR Object
micrCode = micr.MICR(imagePath)

# Extracted Micr from Cheque
micrString = micrCode.extractMICR()

# Micr Id (middle part of Micr)
micrId = micrString.split(" ")
micrId = micrId[1] + micrId[2]
print(micrId)


# Get Details of the Payer from Database
payerDetails = db.micrToAccountDetails(micrId)

# Get name of receiver from account number
receiverName = db.accNumberToName(receiverAccountNumber)[0]
print(receiverName)


# ImageExtractor Object
imageExtractor = imageExtractor.ImageExtractor(currentWorkingDir, imagePath)

# Get name, amount and signature extracted from cheque
nameImage = imageExtractor.nameImage()
print("hello")
amountImage = imageExtractor.amountImage()
print("helloo")
signatureImage = imageExtractor.signatureImage()
print("hellooo")
# HandWritingRecognition Object
handWritingRecog = handWritingRecognition.HandWritingRecognition(nameImage, amountImage)
print("helloooo")
# Name of the receiver in Cheque
nameInCheque = handWritingRecog.nameOCR()
print(nameInCheque)

# If names don't match exit the code
if not utilities.nameCheck(nameInCheque, receiverName):
    print("here")
    exit(3)


# Path of signature database
chequeInDatabase = currentWorkingDir + "/database_images/" + payerDetails[2] + ".jpg"

# Signature Verification Object
signatureVerification = signatureVerification.SignatureVerification(
    currentWorkingDir, chequeInDatabase, signatureImage
)

# if signature is fake
if signatureVerification.verifySignature() == 1:
    print("fakeeeeeeeeeeeeeeeeeeeeee")
    os.remove(currentWorkingDir + "/garbage.jpg")
    exit(2)

# Removing the temporary file garbage.jpg
os.remove(currentWorkingDir + "/garbage.jpg")

print("line 86")


# Amount written on cheque
amountInCheque = handWritingRecog.amountOCR()
amountInCheque = utilities.amountStandarize(amountInCheque)

# if Money not sufficient in account, exit the code
if payerDetails[1] < amountInCheque:
    exit(55)

print("line 97")
# Update the balance in Payer's as well as Receiver's Account
db.updateAmount(payerDetails[3], receiverAccountNumber, amountInCheque)

print("line 101")
print("Cheque verification passed")



exit(0)
