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
