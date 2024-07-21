install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py 

dashboard:
	streamlit run .app/graph.py

update-branch:
	git config --global user.name $(USER_NAME)
	git config --global user.email $(USER_EMAIL)
	git commit -am "Update with new results"
	git push --force origin HEAD:update

hf-login: 
	pip install -U "huggingface_hub[cli]"
	git pull origin update
	git switch update
	huggingface-cli login --token $(HF) --add-to-git-credential

push-hub: 
	huggingface-cli upload VirendraChavda/Hesa_Dashboard ./app --repo-type=space --commit-message="Sync App files"
	huggingface-cli upload VirendraChavda/Hesa_Dashboard ./Data/updated.csv --repo-type=space --commit-message="Sync Model"

deploy: hf-login push-hub

all: install format dashboard deploy
