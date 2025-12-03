# Amazon Reviews Analysis

## ⚙️ Installation

### 🔧 Set Up the Python Environment

#### 1. Clone the repository

```bash
git clone https://github.com/DenkoProg/amazon-reviews-analysis.git
cd amazon-reviews-analysis
```

#### 2. Install `uv` — A fast Python package manager

📖 [Installation guide](https://docs.astral.sh/uv/getting-started/installation/)

#### 3. Create and activate a virtual environment

```bash
uv venv
source .venv/bin/activate
```

Alternatively, you can use the predefined Makefile command:

```bash
make install
```

This will set up the virtual environment, install dependencies, and configure pre-commit hooks automatically.

#### 4. Install dependencies (choose ONE path)

##### 4.1 Reproduce exact versions (use uv.lock)

```bash
# Usage environment (pinned, reproducible)
uv sync --locked

# Development environment (pinned + dev extras)
uv sync --locked --extra dev
```

- Uses the checked-in uv.lock exactly; no re-resolution.
- Ideal for CI and deterministic installs.

##### 4.2 Resolve fresh compatible versions (from pyproject.toml)

```bash
# Usage environment (resolve now and write/update uv.lock)
uv sync

# Development environment (resolve + dev extras)
uv sync --extra dev
```

- Resolves to the latest compatible versions and writes/updates uv.lock.
- Ideal when you want newer dependency versions locally.

##### 4.3 pip-style installs (do NOT enforce the lockfile)

```bash
# Usage only
uv pip install .

# Development (editable) install
uv pip install -e .[dev]
```

> These behave like regular pip installs and ignore uv.lock.

### 🐳 Docker Usage

You can build and run the project using Docker:

#### 1. Build the Docker image

```bash
make docker-build
```

#### 2. Run the Docker container

```bash
make docker-run
```

This will execute `main.py` inside the container using all dependencies and Java for PySpark.

## 📊 Project Structure

### Pipelines

#### 0-preprocess

The preprocessing pipeline contains Jupyter notebooks for data exploration, cleaning, and business analysis across multiple product categories:

- **EDA & Cleaning Notebooks** (`*_eda_and_cleaning.ipynb`): Exploratory Data Analysis (EDA) and data cleaning for each category (e.g., Musical Instruments, All Beauty, Amazon Fashion, etc.)
- **Queries Notebooks** (`*_queries.ipynb`): Answer business questions and perform domain-specific analysis for each category

Each category has its own pair of notebooks to facilitate modular and category-specific analysis workflows.

#### 1-train

The training pipeline contains notebooks for fitting both classification and regression models on the processed Amazon reviews data.

**Classification training (`pipelines/1-train`):**

- `classification_training_lr.ipynb` – trains a **Logistic Regression** sentiment classifier (negative / neutral / positive) using TF–IDF text features.
- `classification_training_rf.ipynb` / `classification_training_random_forest.ipynb` – train **Random Forest** classifiers for comparison with LR.
- `classification_training_svm.ipynb` and `classification_training_svm-my.ipynb` – train **SVM-based** classifiers (LinearSVC + One-vs-Rest).

**Regression training (`pipelines/1-train`):**

- `linear_regression.ipynb` – trains a baseline **Linear Regression** model.
- `random_forest_regression.ipynb` – trains a **Random Forest Regressor**.
- `gbt_regression.ipynb` – trains a **Gradient-Boosted Trees Regressor**.
- `DT_regression.ipynb` – trains a **Decision Tree Regressor**.

#### 2-eval

The evaluation pipeline provides notebooks to assess and compare trained models.

**Classification evaluation (`pipelines/2-eval`):**

- `classification_eval.ipynb` – loads the trained classification models and evaluates them on a held-out test set using:

  - Accuracy
  - F1 score
  - Weighted precision
  - Weighted recall
  - Confusion matrices and per-class metrics
- Includes visualizations (e.g., bar plots) for side-by-side comparison of **Logistic Regression**, **Random Forest**, and **SVM** classifiers.

**Regression evaluation (`pipelines/2-eval`):**

- `regression_eval_linear.ipynb`
- `regression_eval_rf.ipynb`
- `regression_eval_gbt.ipynb`
- `regression_eval_DT.ipynb`

Each notebook:

- Loads the corresponding regression model.
- Evaluates performance using metrics such as RMSE, MAE, and R².
- Provides plots and tables that help compare predictive quality across models.

These notebooks are intended for **model selection**, benchmarking, and reporting.

#### 3-infer

The inference pipeline shows how to use trained models for predictions on new or unseen data.

**Classification inference (`pipelines/3-infer`):**

- `classification_inference_lr.ipynb` – demonstrates how to:

  - Load the saved Logistic Regression classifier.
  - Run predictions on custom review texts.
  - Interpret the predicted sentiment labels.
- (You can add similar notebooks for RF / SVM if needed, following the same pattern.)

**Regression inference (`pipelines/3-infer`):**

- `regression_inference_linear.ipynb`
- `regression_inference_rf.ipynb`
- `regression_inference_gbt.ipynb`
- `regression_inference_DT.ipynb`

These notebooks:

- Load the corresponding regression models.
- Show how to build a Spark DataFrame with new input samples.
- Generate predictions (e.g., for review rating or target variable) and interpret the outputs.

The `3-infer` stage is focused on **practical usage** of the models – integrating them into workflows, demos, or downstream applications.
