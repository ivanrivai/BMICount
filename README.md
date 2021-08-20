# HappyFresh Simple Apps
This is a simple apps to count the BMI (Body Mass Index) of a person. I developed using local environment, so there's some requirements that will not be met, but I hope the core concept is met.

## Pre-requisites:
1. Windows 10-64bit
2. Python version 3.9.x
3. Flask version 2.0.1 and other dependencies from requirements.txt
4. Postman (to test API hit)
5. Visual Studio Code (or any editing tools)
6. Docker Desktop
7. Github accounts
8. Docker hub accounts

<em>This application was developed using specifications above, it might have different syntax if you are using linux/macOS based, but the concept should be the same.</em>
<em>For python installation, please visit https://python.org , recommended to use the latest stable build.</em>
<em> Download Docker: https://docs.docker.com/get-docker/</em>

# Workflow Diagram
![Workflow Diagram](/image_resources/workflow.png)

> Here is the process of the development:
>> 1. Develop apps using Python + Flask
>> 2. Push the code to Github
>> 3. Use Github Action to automate build (CI/CD), and push the image to Docker Hub
>> 4. Pull the image from Docker Hub, and run it locally using Docker Desktop

## Directory Structure
1. .github/workflows/ : this is used in Github Action to do the CI/CD, the naming must be exact
2. image_resources/ : this is image resource from screenshoots
3. docker-compose.yml : orchestration for creating the apps' container and other supporting containers 
4. Dockerfile : the config for building the apps
5. logstash.conf : the logstash config file
6. main.py : the source code of the apps
7. requirements.txt : modules that need to be installed to support the apps, extracted from <em>pip3 freeze > requirements.txt</em>

## Additional
1. Add secrets to Github, credentials for pushing image to dockerhub
> Step 1  
    ![Github Step 1](/image_resources/secret_github.png)  
>>      From the repo Settings, click secret    
> Step 2  
    ![Github Step 1](/image_resources/secret_github_2.png)  
>>      Click new repository secret  
> Step 3  
    ![Github Step 1](/image_resources/secret_github_3.png)  
>>      Add a key DOCKER_HUB_USERNAME, and add the value  
> Step 4  
    ![Github Step 1](/image_resources/dockerhub_settings.png)  
>>      Go to dockerhub repo, create new access token as above
> Step 5  
    ![Github Step 1](/image_resources/secret_github_4.png)  
>>      Add another key DOCKER_HUB_ACCESS_TOKEN, and add the value from the docker hub access token, then we have 2 keys like this  


