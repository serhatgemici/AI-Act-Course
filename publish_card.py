from huggingface_hub import HfApi, ModelCard
import os

"""""
Hugging Face Model Card Publisher

This script automates the creation and publishing of a Hugging Face Model Card for the specified project.

It expects the environment variables HF_TOKEN and USERNAME to be set.

Usage:
    python publish_card.py

Ensure that the environment variables HF_TOKEN and USERNAME are set before running the script.
""" ""

PROJECT_NAME = "exo-chap2"

REPO_ID = os.getenv("USERNAME") + "/" + PROJECT_NAME

token = os.getenv("HF_TOKEN")

if token is None:
    raise ValueError("Missing HF_TOKEN")

api = HfApi(token=token)

# Creation of the private repo
api.create_repo(repo_id=REPO_ID, repo_type="model", private=True, exist_ok=True)

# Loading the Model Card
card = ModelCard.load("model_card.md")

# Push to the Hub
card.push_to_hub(REPO_ID, token=token)

print("Model Card published successfully.")
