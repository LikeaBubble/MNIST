# MNIST

# About dataset
  - MNIST is a collection of hand written digits (28x28 images) and their labels.
  - It known as the most basic task in computer vision field.
  - Images looks like this:  
![img_171](https://github.com/user-attachments/assets/5b5fc447-c4ed-4d9c-b183-69f17b90f53c)  ![img_122](https://github.com/user-attachments/assets/d5cc9e72-b58b-4b88-b418-9026e5ce3066)  ![img_108](https://github.com/user-attachments/assets/4c09f8c6-6ac0-402e-bade-b1829aaffe68)


# Task
  - To predicting the label of each image I have been used ANNs and CNNs.
  - We will compare the results of models.

# Results
- Because dataset is very small and simple, I think a shallow network with less than 10'000 trainable parameters will be enough.
- Results on unseen data are as here:
  1. ANN(~7500 trainable params):
       - Accuracy: %94
       - Loss: 0.20
       - F1 score: %94
         <img width="1224" height="451" alt="out3" src="https://github.com/user-attachments/assets/897de85b-9399-4d3e-8d2b-fa6d8c0b6d7a" />
       - Predicted examples:  
         <img width="252" height="252" alt="out2" src="https://github.com/user-attachments/assets/d97a09e1-cf48-497e-9c4a-4af93f64b769" />


  2. CNN(~12000 trainable params):
       - Accuracy: %98
       - Loss: 0.05
       - F1 score: %98
          <img width="1215" height="451" alt="output" src="https://github.com/user-attachments/assets/3ea7f9e0-61e7-4290-90f7-099ca1ad6ede" />
       - Predicted examples:  
          <img width="252" height="252" alt="out1" src="https://github.com/user-attachments/assets/9bcbfed9-f381-4334-8685-1dd97a5944e0" />

