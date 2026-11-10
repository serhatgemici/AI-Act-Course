---
license: mit
language:
  - en
datasets:
  - iris
metrics:
  - accuracy
  - f1
pipeline_tag: tabular-classification
tags:
  - sklearn
  - random-forest
  - iris
  - classification
---

# Model Card — Iris Flower Classifier

## Model Details

- **Model name**: Classificador de Flores Iris
- **Author**: Liora
- **Date**: 2026-06-22
- **Version**: 1.0
- **Model type**: RandomForestClassifier (scikit-learn), 100 estimadores, random_state=42
- **License**: MIT

---

## Intended Use

### Intended Use Cases

This model predicts the species of an Iris flower (setosa, versicolor, or virginica) based on four morphological measurements: length and width of the sepals and petals.

**Usage Context**: learning environment only. This model can be used for technical demonstrations, supervised classification exercises, or ML pipeline testing.

### Use Beyond the Scope

- **Not suitable for production use**: this model has not undergone robustness testing, cross-validation, or regulatory audit.
- **Not designed for high-stakes decisions**: any use in a medical, legal, or commercial context is out of scope.
- **Not generalizable**: the model was trained on a very small and very clean dataset, not representative of real-world data collected under varied conditions.

---

## Factors

Two main factors can influence the performance of this model:

1. **Distribution of input features**: the model was trained on measurements (length/width of sepals and petals) from a very homogeneous and well-separated dataset. If the input data in production has a different distribution (for example, atypical specimens or measurements from a different collection protocol), the performance could degrade significantly.

2. **Class Balance**: The Iris dataset is perfectly balanced (50 examples per class). A class imbalance in a real dataset could bias predictions in favor of the majority class, which has not been tested here.

---

## Metrics

### Selected Metrics

For a **multi-class classification** problem, accuracy alone can mask disparities between classes. The following metrics have therefore been retained:

- **Accuracy** : overall proportion of correct predictions.
- **Precision** (per class) : among the examples predicted as class X, how many are actually class X.
- **Recall** (per class) : among the examples actually of class X, how many were correctly identified.
- **F1-score** (per class) : harmonic mean of precision and recall, useful when both are important.
- **Macro average** : unweighted average of metrics by class — treats all classes equally regardless of their frequency.

### Results on the test set (30 examples, test_size=0.2, random_state=42)

| Class        | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| setosa       | 1.00      | 1.00   | 1.00     | 10      |
| versicolor   | 1.00      | 1.00   | 1.00     | 9       |
| virginica    | 1.00      | 1.00   | 1.00     | 11      |
| **accuracy** |           |        | **1.00** | **30**  |
| macro avg    | 1.00      | 1.00   | 1.00     | 30      |
| weighted avg | 1.00      | 1.00   | 1.00     | 30      |

> An accuracy of 1.0 on this dataset is expected and known in the literature: Iris is a nearly linearly separable dataset. These results are **not representative of the expected performance on real data**.

---

## Training Data

- **Dataset Name**: Iris flower dataset (Fisher, 1936)
- **Source**: `sklearn.datasets.load_iris()`
- **Total Size**: 150 examples
- **Training Size**: 120 examples (80%, after train/test split)
- **Features** (input variables):
  - `sepal length (cm)` — sepal length
  - `sepal width (cm)` — sepal width
  - `petal length (cm)` — petal length
  - `petal width (cm)` — petal width
- **Target**: flower species — 3 classes: `setosa`, `versicolor`, `virginica`
- **Preprocessing**: none (the dataset is clean, with no missing values and no normalization needed for random forests)
- **Known Limitations**: dataset collected in 1936 from a single geographical location (Gaspé Peninsula, Canada). Not representative of global botanical diversity.

---

## Evaluation Data

- **Source** : same dataset as training (Iris), test partition
- **Size** : 30 examples (20% of the total dataset)
- **Separation method** : `train_test_split(test_size=0.2, random_state=42)` — reproducible random split
- **Preprocessing** : no specific preprocessing applied
- **Note** : evaluation on a split of the same dataset does not guarantee generalization to new data. No external benchmark has been used.

---

## Quantitative Analyses

Disaggregated performances by class on the test set:

| Class      | Precision | Recall | F1-score | Support |
| ---------- | --------- | ------ | -------- | ------- |
| setosa     | 1.00      | 1.00   | 1.00     | 10      |
| versicolor | 1.00      | 1.00   | 1.00     | 9       |
| virginica  | 1.00      | 1.00   | 1.00     | 11      |

The performances are **homogeneous among the three classes**: no class is classified worse than the others on this test set. This is consistent with the nature of the Iris dataset, where the classes are well separated in the feature space.

> This homogeneity is specific to this dataset and should not be interpreted as a guarantee of general robustness. On real data featuring morphologically similar species, disparities between classes would be likely.

---

## Ethical Considerations

### Usage Risks

This model does not present a direct ethical risk, as it classifies flowers rather than people. However, using this model in a high-stakes context (for example, an automated botanical classification system used for business or scientific decisions) would be inappropriate without further rigorous validation. It was not designed or tested for such use.

### Potential Biases

The Iris dataset was collected in 1936 from a single geographical location. It does not represent the natural variability of iris species around the world. A model trained on this data might fail on specimens from other regions, different climatic conditions, or different blooming periods. Furthermore, the dataset is perfectly balanced (50 examples per class), which does not necessarily reflect the natural distribution of the species.

---

## Caveats and Recommendations

- **Very small dataset (150 observations)** → Do not generalize the results without validation on a larger and more diverse dataset. An accuracy of 1.0 on 30 examples is not statistically robust.

- **No cross-validation** → The presented performances are based on a single train/test split. Recommendation: perform k-fold cross-validation (k=5 or k=10) before any deployment to obtain a more reliable estimate of the performances.

- **Data not representative of the real world** → The Iris dataset is a standardized academic benchmark, not a reflection of actual botanical diversity. Recommendation: test the model on data collected under varied conditions (different regions, seasons, measurement protocols) before using it in an applied context.

- **Absence of post-deployment monitoring** → No monitoring mechanism is planned. Recommendation: implement tracking of input distributions (data drift) if the model is to be used on data collected over time.

---

## Reproducibility

- **Git commit (git_sha)** : bf3c8d9b3a58e7aee41393464d78a1ce20552adf
- **MLflow run_id** : N/A (not used in this chapter)
- **Dataset hash** : N/A (not used in this chapter)
