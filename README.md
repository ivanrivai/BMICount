# HappyFresh Simple Apps
This is a simple apps to count the BMI (Body Mass Index) of a person. I developed using local environment, so there's some requirements that will not be met, but I hope the core concept is met.

# Resource  
https://hub.docker.com/r/irivai/flask     <em>image repository</em>  
https://github.com/ivanrivai/happyFresh_assignment     <em>code repository</em>  
<br />

## Pre-requisites:
1. Windows 10-64bit
2. Python version 3.9.x
3. Flask version 2.0.1 and other dependencies from requirements.txt
4. Postman (to test API hit)
5. Visual Studio Code (or any editing tools)
6. Docker Desktop
7. Github accounts
8. Docker hub accounts
9. Git

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
    ![Github Step 1](/image_resources/secret_github.PNG)  
>>      From the repo Settings, click secret    
> Step 2  
    ![Github Step 2](/image_resources/secret_github_2.PNG)  
>>      Click new repository secret  
> Step 3  
    ![Github Step 3](/image_resources/secret_github_3.PNG)  
>>      Add a key DOCKER_HUB_USERNAME, and add the value  
> Step 4  
    ![Github Step 4](/image_resources/dockerhub_settings.PNG)  
>>      Go to dockerhub repo, create new access token as above
> Step 5  
    ![Github Step 5](/image_resources/secret_github_4.PNG)  
>>      Add another key DOCKER_HUB_ACCESS_TOKEN, and add the value from the docker hub access token, then we have 2 keys like this  
<br />

# Prerequisites for the service
1. Create and clone repository by using git  
![Github Step 1](/image_resources/git-1.PNG)  
2. Create initial commit  
![Github Step 2](/image_resources/git-2.PNG) 
3. Github workflow before push  
![Github Step 3](/image_resources/github-action0.PNG) 
4. Git push  
![Github Step 4](/image_resources/git-push.PNG) 
5. After git push, workflow is automatically created and triggered via 'push' action  
![Github Step 5](/image_resources/github-action1.PNG) 
6. Job snippet
![Github Step 6](/image_resources/github-action2.PNG) 

<br />

# Run the Service
I am personally using docker-compose for the container orchestration. To be noted, by using docker-compose, the network is automatically created, so that the containers are packaged into 1 single isolated network, and can talk to each other.  
1. Go to the project directory, and run command **docker-compose up -d**. -d is used for detached mode, meaning we can use the same terminal.  
![Docker step 1](/image_resources/docker1.PNG)  
<em> you can see that 4 containers are created, the flask (apps), and additional ELK stack for centralized logging. The process should be pulling all containers, but because i have pulled the ELK images before, the docker use the cached image.</em>  
<br />

2. If you want to see the running containers, run command **docker ps**.
![Docker step 2](/image_resources/docker2.PNG) 
<br />

3. Now, all is up and running (it might take a while for the kibana to fully operates), let's access **http://localhost:5601**. The kibana should be showing, click the three-lines menu then navigate to <em>Discover</em>.    
![Docker step 3](/image_resources/kibana.PNG)  
<br />

4. In here, we need to create the index pattern. Remember logstash.conf? in this part <em> index => "logs-%{+YYYY-MM-dd}" </em>. When you type logs-*, the kibana understands and match the search. Then proceed to the next step.
![Docker step 4](/image_resources/kibana2.PNG)  
<br />

5. In the next section, we need to apply time filter for the logs. choose **@timestamp** and then create index pattern.  
![Docker step 5](/image_resources/kibana3.PNG) 
<br />

6. Navigate back to Discover (it may take 1-2minutes for the logs to propagate), and we can the logs is already streaming.
![Docker step 6](/image_resources/kibana4.PNG) 
<br />

7. We can filter the logs based on the available fields. I want to explain about **tag**. We need to navigate back to <em>docker-compose.yml</em>.  
In docker-compose.yml, i added tag options in flask and kibana services, namely <em>flask_app</em> and <em>flask_kibana</em>. For kibana, i just set to log everything.  
In flask apps, i only logs when the apps is having error message. Let's look at this example.  
![Docker step 7](/image_resources/kibana5.PNG)  
This is before hitting the apps with intend to error.  
<br />

8. Now, let us try hitting some random endpoints, or hit the validation. I am using postman for hitting GET request.  
the url for the apps here is: **http://localhost:5000**.  
I tried hitting http://localhost:5000/?height=180&weight=-60 and see what happens.  
![Docker step 8](/image_resources/postman.PNG)  
> The apps returns an error. Now let's refresh the logs in kibana.  
![Docker step 9](/image_resources/kibana6.PNG)  
> The logs was streamed with tag <em>flask_app</em> as defined.  
<br />

# Unit Tests
Here is some tests I ran for the validation.  
1. negative weight  
![Docker step 10](/image_resources/postman.PNG)  
2. negative height  
![Docker step 11](/image_resources/postman2.PNG)  
3. non-numeric height/weight  
![Docker step 12](/image_resources/postman3.PNG)  
4. actual validation  
![Docker step 12](/image_resources/postman4.PNG)  
<br />

# Conclusion
<p> From the requirements, there is some that I can not fulfill, like DNS hosting and centralized logging with public access. But I tried to give something like docker orchestration, dockerfile, and local logging using ELK stack. I hope that this tutorial can meet the requirements.</p>  
<br />

To terminate the containers, run command **docker-compose down -v**. -v is used to take down and remove all containers, networks, and volumes included.  

**Thank you !!**
