# upload-image-api
Api for uploading images for specific users and getting links in regards to the bought plan.
Although app has not been finished, it has been made public to let people see the progress.
I am going to focus on the remaining functionality, test, validations and edge cases.
I hope that this will bear fruits. I have had lots of fun doing this project and have learned a lot of Django stuff.

### App is running on the localhost port 8009, http://localhost:8009/
## Prerequisities
### I assume you have installed Docker and it is running. See the [Docker website](http://www.docker.io/gettingstarted/#h_installation) for installation instrucitons.
## Build
1. Clone this repo
    ``` git clone https://github.com/mradzikowski/upload-image-api.git ```
2. Build the docker image
    ``` docker-compose build ```
3. Fire up the container in detached mode
    ``` docker-compose up -d ```
4. If you make any change, update the container using command
    ``` docker-compose up -d --build ```
5. To see docker-compose logs use:
    ``` docker-compose logs ```
   
## Testing
``` docker-compose exec images pytest ```

### Flake8
``` docker-compose exec images flake8```
### Black
``` docker-compose exec images black```
### Isort
``` docker-compose exec images isort```

### Requests to be made and build better serializers
### TO DO 
#### I hope that during this weekend i will have finished the rest of the work and prepare consistent application that could be extended to bigger project.
