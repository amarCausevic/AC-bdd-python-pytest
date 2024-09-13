# bdd-python-pytest
This repository gives you a quick sample on how to user BDD implementation in pyTest

## Scenarios
In current implementation I have focused on creating a fail scenario on Joan Portal. 
Meaning that we as user are going to send invalid email suffix format and invalid string as user credentials and try to login.
User will receive error validation messages during this process which we would like to test.
After the test we are goint to close the driver which is currenlty running as CHROME.

## What have I used as support:
I have introduced into this project pyTest (pyTest BDD) with selenium automation framework to automate web-browser scenario.

##Principles
I have used BDD principles to create the scenario with pyTest-BDD framework. Which means that I have used:
  * feature file (containes scenario defined in BDD)
  * steps file (containes steps that will be executed from features file)
  * actions file (will contain all actions that will be used for specific page)
  * enums (currenlty selectors and validation message values are defined)
  * common (utils like Wait, Selectors, etc.)

###Project structure
![image](https://github.com/user-attachments/assets/4493ea07-730e-4178-a9bc-2c3c4a452322)


##How to run: 
I have provided PyTestRunner run/debug configuration which you can simply press Run in your pyCharm or other IDE that you prefer.

##Run Example:
https://github.com/user-attachments/assets/4b8eab86-9bd7-4fe1-be4c-b34e5e2a4dfd



##Current status
Only once scenario was added to this project, more will be on the way:
![image](https://github.com/user-attachments/assets/a89e6797-496d-4478-9964-a11603b624db)




