install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py 

process:
	python Convert_Data.py

dashboard:
	python .app/HESA_Dashboard.py
		
update-main:
	git config --global user.name $(USER_NAME)
	git config --global user.email $(USER_EMAIL)
	git commit -am "Update with new results"
	git push --force origin HEAD:main

hf-login: 
	pip install -U "huggingface_hub[cli]"
	git pull origin main
	git switch main
	huggingface-cli login --token $(HF) --add-to-git-credential

push-hub: 
	huggingface-cli upload VirendraChavda/Drug_Classifier ./app --repo-type=space --commit-message="Sync App files"
	huggingface-cli upload VirendraChavda/Drug_Classifier ./Data/updated.csv --repo-type=space --commit-message="Sync Model"

deploy: hf-login push-hub

all: install format process dashboard deploy
