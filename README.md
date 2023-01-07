# MLOps-Credit-Card-Fraud-Detection
# Deploy Machine learning API using Flask and Docker

In this tutorial, we create a containerized machine learning application. This is an internal credit card fraud detection system designed by the bank for checking the fraud. All of the system have been designed end to end. Further integration of CI/CD pipeline through Gitlab/Kubernetes is also possible.

# Create your model
We create a classifier on credit card fraud detection dataset and stored the fitted model in a file.
train file- train.ipynb

model file- python app.py

# Deploy your docker image

docker build -t prathamesh/myapp:beta .


docker tag prathamesh/myapp:beta prathameshk711/credit_card

# Then just run your image
docker run -p 5000:3840 --rm demo

And if you go to http://127.0.0.1:5000 you will see your application running!

(If not use nmap localhost -p 5000 to see if the port is open and http http://127.0.0.1:5000 to see what's responding)

# Front end
### Enter your data here:- 
<img width="1223" alt="image" src="https://user-images.githubusercontent.com/89546195/211170690-67161632-3267-417c-8b6e-bbf3c4464f62.png">




