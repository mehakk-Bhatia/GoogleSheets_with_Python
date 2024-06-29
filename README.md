# GoogleSheets_with_Python

for setting up this project, first we need to create a new project on google cloud console. click on the link: https://console.cloud.google.com/
If you have already created projects on the Google Cloud console, you will see something like this. To create a new project, you have to click on the name of the current project you are in at the top.

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/ceb11764-c84a-4d5a-b7df-03755e7fb30b)

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/7a97158b-c566-4369-beed-97241eeb7f95)

after creating new project, you need to add API's to the project which include google drive API and Google sheets API for adding API's follow the images
![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/8b058f0e-c159-4027-9d0d-6e292c557127)

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/1feb1d81-fa31-4672-8cdd-97891ebaf3cc)

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/627ae76b-10b1-4236-9ad4-7a04c1e7cdfe)

now search Google sheets API and enable it. Similarly enable google drive API
Now click on credentials and then create credentials and choose service account.

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/962b76f5-f5bb-4e01-be57-36639aeaa47a)

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/21a93ed2-803d-4466-a587-c8a0a69d2be5)

fill the service account details

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/0fceae38-d926-4688-839f-5a91dfa51aa9)

choose editor as a role by clicking on basic

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/cf0b1a86-a3d7-416d-8231-b0b1a050cb1c)

now after setting up service account. Click on service account and then Go to Keys tab and create a key and select JSON.

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/ae7ff32d-56a7-45aa-9b13-59e3b9d54b53)

![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/39ceb53d-ed23-46b3-a3d8-2f53410caf7d)

A JSON file with credentials will be downloaded.

Now for running the code, fork the repository and clone the project into terminal

run command:
pip install -r requirements.txt
and update the credentials file with the downloaded credentials.

for using google sheets in the code, go to sheets.google.com
 create a sample spreadsheet with sheet1 and sheet2
 and click on the share button of google sheet. Add the client email id downloaded in credentials.json

 reference input and output:
 ![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/7f19688a-ea88-46e3-9d41-92292e7784d1)

 ![image](https://github.com/mehakk-Bhatia/GoogleSheets_with_Python/assets/91878394/1156c345-d158-4449-bb22-471b7745d179)
 



