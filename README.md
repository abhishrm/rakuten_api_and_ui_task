# Rakuten_task_submission : Rakuten API i.e. Movies/video_qualities/audio_qualities/genres and UI (Youtube)test Automation.

# How to run complete project using Docker(In this case Docker will build an image with all pre-requisites like installing requirements.txt automatically which is required to run test automation and then will automatically trigger test using behave command):
-Pre requisite is that your machine should have Docker installed.

-Clone the repository using command -> git clone https://github.com/abhishrm/rakuten_task_submission

-Navigate to project path on command line -> /Rakuten_Assignment/

-This folder directory i.e. github_project contains bash script with name -> "build_and_run.sh"

-You need to run this bash script by passing only one mandatory command line parameter. The parameter should be the name with which you want to build the image.

-If you do not pass this parameter, then this bash script will exit and will provide you instructions about passing a mandatory command line argument.

-Run this bash script by writing and then enter-> ./build_and_run.sh

-This bash script while running will create the image and will run the container .

-Also it will install all the dependencies required to run the test i.e. all python libraries from the requirements.txt file.

-There is no such manual intervention required. You only need to trigger bash script "build_and_run.sh"

- The test which will run are defined in command set in Image file used by docker i.e. CMD ["behave", "src/features/Rakuten_api_automation_test.feature"]
-This will by default run all the API test placed in Rakuten_api_automation_test.feature feature file. If you want to run the UI test ,please change the feature file name to ui_youtube_test_automation_part.feature in Dockerfile (This file is placed in Rakuten_Assignment folder).


# How to run the test locally by creating a virtual environment cloning the repository

-Install virtualenv by passing command "pip install virtualenv".

-Now create a virtualenv using the following command: virtualenv <here_pass_name_of_the_virtual_environment>
 After running this command, a directory named <here_pass_name_of_the_virtual_environment> will be created. This is the directory which contains all the necessary executables to use the packages that a Python project would need. This is where Python packages will be installed.

-Specify Python interpreter of your choice using command -> virtualenv -p /usr/bin/python3 virtualenv_name

-Now after creating virtual environment, you need to activate it.
 To do this run command -> "source virtualenv_name/bin/activate"
 Once the virtual environment is activated, the name of your virtual environment will appear on left side of terminal. This will let you know that the virtual environment is currently active

-Now clone the code from git clone https://github.com/abhishrm/rakuten_task_submission
-Now you can install dependencies by navigating to Rakuten_Assignment directory.
 This directory contains all dependencies in "requirements.txt"
 Install all dependencies by running command : pip install -r ./requirements.txt

-Navigate to the project path folder on the command line -> /Rakuten_Assignment/src/src.
-Under step folder run the command like -> behave src\features\api_automation_test.feature -t <tagname> --no-capture

On windows command prompt it looks like,

    C:\Users\Abhishek\Downloads\Rakuten_Assignment\src>behave src\features\Rakuten_api_automation_test.feature -t @TC-1

     where: 'Rakuten_Assignment' is a directory where we check out automation code from repo

-If you want to run all the test from Rakuten_api_automation_test.feature then under src folder run the command like -> behave src\features\api_automation_test.feature -t <tagname> --no-capture

On windows command prompt it looks like,

    C:\Users\Abhishek\Downloads\Rakuten_Assignment\src>behave src\features\Rakuten_api_automation_test.feature

     where: 'Rakuten_Assignment' is a directory where we check out automation code from repo


-Once you are done with the work, you can deactivate the virtual environment by the following command:deactivate
