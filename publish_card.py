"""Publish the project's model card to a private Hugging Face repository."""

import os
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import HfApi, ModelCard

load_dotenv(Path(__file__).with_name(".env"))

PROJECT_NAME = "exo-chap2"
username = os.getenv("USERNAME", "").strip()
token = os.getenv("HF_TOKEN", "").strip()

missing = [
    name for name, value in (("USERNAME", username), ("HF_TOKEN", token)) if not value
]
if missing:
    raise SystemExit(
        f"Missing required configuration: {', '.join(missing)}. Set it in .env or the environment."
    )


repo_id = f"{username}/{PROJECT_NAME}"
api = HfApi(token=token)
api.create_repo(repo_id=repo_id, repo_type="model", private=True, exist_ok=True)

card = ModelCard.load("model_card.md")
card.push_to_hub(repo_id, token=token)

print("Model Card published successfully.")
