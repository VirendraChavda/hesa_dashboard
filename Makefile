install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

dashboard:
	streamlit run .app/graph.py

hf-login: 
	pip install -U "huggingface_hub[cli]"
	git pull origin main
	git switch main
	huggingface-cli login --token $(HF) --add-to-git-credential

push-hub: 
	huggingface-cli upload VirendraChavda/Hesa_Dashboard ./app --repo-type=space --commit-message="Sync App files"
	huggingface-cli upload VirendraChavda/Hesa_Dashboard ./Data/updated.csv --repo-type=space --commit-message="Sync Model"

deploy: hf-login push-hub

all: install dashboard deploy
