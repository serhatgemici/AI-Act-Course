# Chapter 2 - Model Cards and Documentation

## Overview

This exercise introduces the concept of **Model Cards**, a standardized way to document machine learning models.

The objective is to understand how model documentation improves:

- Transparency
- Reproducibility
- Traceability
- AI governance and compliance (AI Act)

You will train a simple machine learning model on the Iris dataset and progressively complete a Model Card describing the model, its performance, limitations, and intended use.

---

## Learning Objectives

By completing this exercise, you will learn how to:

- Train a machine learning model
- Document a model using a Model Card
- Describe datasets, metrics, and limitations
- Publish documentation on Hugging Face Hub
- Apply documentation practices aligned with responsible AI principles

---

## Project Structure

```text
chapitre-2/
├── train.py
├── model_card.md
├── publish_card.py
├── pyproject.toml
└── .env.example
```

| File | Description |
|--------|-------------|
| `train.py` | Training script (provided, do not modify) |
| `model_card.md` | Model Card template to complete |
| `publish_card.py` | Publishes the Model Card to Hugging Face |
| `pyproject.toml` | Project dependencies |
| `.env.example` | Hugging Face token template |

---

## Prerequisites

- Git
- UV package manager
- Hugging Face account

Install UV if needed:

```bash
pip install uv
```

---

## Installation

Clone the repository:

```bash
git clone  https://github.com/<votre-username>/AI-Act-Course.git
cd AI-Act-Course
```

Go to right branch (chapitre-2):

```bash
git checkout chapitre-2
```

Install dependencies:

```bash
uv sync
```

---

## Run the Training

Launch the training script:

```bash
uv run train.py
```

This script:

- Loads the Iris dataset
- Trains a RandomForestClassifier
- Evaluates the model
- Displays classification metrics
- Saves the trained model

Keep the generated metrics, as they will be required to complete the Model Card.

---

## Complete the Model Card

Open:

```text
model_card.md
```

Complete each section as you progress through the chapter:

- Model Details
- Intended Use
- Factors
- Metrics
- Training Data
- Evaluation Data
- Quantitative Analyses
- Ethical Considerations
- Caveats and Recommendations
- Reproducibility

---

## Hugging Face Publication

Create a `.env` file:

```bash
cp .env.example .env
```

Add your Hugging Face token and username:

```env
HF_TOKEN="hf_xxxxxxxxxxxxxxxxx"
USERNAME="your-hugging-face-username"
```

The script loads `.env` automatically. Environment variables already set in
your shell take precedence over values in the file. Keep your token private;
`.env` is ignored by Git.

Run:

```bash
uv run publish_card.py
```

This will:

- Create a Hugging Face repository (if needed)
- Upload the Model Card
- Associate the documentation with the model repository

---

## Expected Deliverables

### GitHub Repository

Must contain:

- Source code
- Completed `model_card.md`
- README.md

### Hugging Face Repository

Must contain:

- Published Model Card
- Private repository named `exo-chap2`

---

## Key Concepts Covered

- Model Cards
- Responsible AI
- AI Act documentation requirements
- Hugging Face Hub
- Reproducibility
- Machine Learning Governance

---
