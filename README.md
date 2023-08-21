# Cheque It Fraud Detction System
This was made in part of a Research Collaboartion of Polaris Technologies with our Technical Advisors. 

This project implements a signature forgery detection and cheque verification system using a combination of image processing and deep learning techniques. The project's goal is to provide a reliable solution for detecting forged signatures and verifying bank cheques.

## Technical Summary

### Data Collection

- **Signatures:** Genuine and forged signatures data collected from Kaggle and CEDAR datasets.
- **Cheques:** High-resolution bank cheque images collected from Kaggle.

### Data Preparation

- **Signatures:** Data organized into real and forged folders. Image processing includes rotations, rescaling, and horizontal flips using Keras Image Generator.
- **Cheques:** Preprocessing involves BGR to grayscale conversion, thresholding, edge detection, dilation, erosion, and noise reduction using OpenCV.

### Model Training

- **Signatures:** Convolutional Neural Networks (CNNs) used with Keras and TensorFlow. The model includes 6 layers with convolution, batch normalization, max pooling, dropout, and fully connected layers.

### Image Segmentation

- **Signatures:** Images segmented to extract relevant parts (amount and signature) using OpenCV functions.

### Testing and Evaluation

- Model accuracy validated using a holdout set. Data augmentation and additional layers employed to improve accuracy.
- Cheque verification includes user-submitted image and account number, with the system detecting forgery or errors.

### Conclusion

- Successful implementation demonstrated for signature forgery detection and cheque verification.
- High accuracy achieved on Kaggle and CEDAR datasets.
- Proposed system contributes to Industry Innovation and Infrastructure SDG by automating document verification.
- System improves efficiency in detecting and investigating forgeries, simplifying authentication for bank staff.

## Purpose

The project's purpose is to provide a reliable and practical solution for authentication and security in financial processes. By combining data collection, image processing, and deep learning, the system effectively detects signature forgery and verifies bank cheques.


