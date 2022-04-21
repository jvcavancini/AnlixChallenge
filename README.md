# AnlixChallenge
This work is based on the challenge in https://github.com/anlix-io/desafio-anlix

This project was created in django with an integration to MongoDB. It was my first django experience.

I intend to continue this work and create a frontend in Angular and a container with it

To run, you should run the commands:
AnlixChallenge/env/Scripts/Activate.ps1
pip install -r requirements.txt
python manage.py runserver 8000

This rest api works as follows:
You can see all the patients and their info in the url localhost:8000/api/patients
You can see an specific patient consulting by cpf in the url localhost:8000/api/'patientcpf', where in 'patientcpf' you use the patient cpf
You can see all patients that have cardiac or pulmonary data in a specific date in the url localhost:8000/api/date/'specificdate', where in 'specificdate' you use the date you want to consult
You can see all patients that have cardiac or pulmonary data in a range of dates in the url localhost:8000/api/rangedate/'firstdate'/'lastdate', where 'firstdate' is the start of the range and 
'lastdate' is the end of the range
You can check the patients that have a cardiac or pulmonary index between 2 values in the url localhost:8000/api/valuerange/'firstvalue'/'lastvalue', where 'firstvalue' is the start of the range and 'lastvalue' is the end of the range
You can check the information of a patient according to a substring of his name in localhost:8000/api/namesearch/'substring', where 'substring' is a substring of the patient name