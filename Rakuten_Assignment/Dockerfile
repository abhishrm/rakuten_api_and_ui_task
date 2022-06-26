#Deriving the python image
FROM python:3.8-slim


#Labels as key value pair
LABEL Maintainer="abhishek sharma"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# I have chosen /usr/app/testing
WORKDIR /usr/app/testing

#to COPY the remote working directory in container
COPY src ./

# copy requirements
COPY requirements.txt ./

# installing requirements - python modules
RUN pip install -r ./requirements.txt || { echo 'required module installation failed. Exitinng!!' ; exit 1; }

# install git
RUN apt-get -y update
RUN apt-get -y install git


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD ["behave", "src/features/Rakuten_api_automation_test.feature"]