# Amazon Reviews Analysis - Project Tasks

## Dataset Information

- **Source**: Amazon Reviews 2023 (https://amazon-reviews-2023.github.io/)
- **Team Size**: 6 people
- **Approach**: Each team member analyzes a specific product category, then models are trained on the complete dataset

---

## Phase 1: Data Extraction (Етап видобування)

### Objectives

1. Create appropriate schemas for the Amazon Reviews dataset
2. Load data from local storage using the created schemas
3. Create DataFrames for each category
4. Verify data is loaded correctly
5. Create modules and functions for data loading operations

### Tasks

#### 1.1 Schema Design

- [ ] Analyze Amazon Reviews 2023 dataset structure
- [ ] Design PySpark schema for reviews data (rating, text, helpful votes, verified purchase, etc.)
- [ ] Design PySpark schema for metadata (product info, categories, price, etc.)
- [ ] Document schema in code with proper types (StringType, IntegerType, DoubleType, TimestampType, etc.)
- [ ] Create reusable schema definitions in `src/amazon_reviews_analysis/schemas.py`

**Deliverables**:

- `src/amazon_reviews_analysis/schemas.py` with defined schemas
- Documentation of schema structure

#### 1.2 Data Loading Implementation

- [ ] Create module `src/amazon_reviews_analysis/data_loader.py`
- [ ] Implement function `load_reviews_data(spark, category, data_path)` to load reviews
- [ ] Implement function `load_metadata(spark, category, data_path)` to load product metadata
- [ ] Add error handling for missing files or corrupted data
- [ ] Add logging for tracking data loading progress

**Deliverables**:

- `src/amazon_reviews_analysis/data_loader.py` with loading functions
- Unit tests for data loading functions

#### 1.3 Individual Category Data Loading (Each Team Member)

- [ ] **Member 1-6**: Load reviews data for assigned category
- [ ] **Member 1-6**: Load metadata for assigned category
- [ ] **Member 1-6**: Verify data loading with `.show()`, `.printSchema()`, `.count()`
- [ ] **Member 1-6**: Document any data quality issues found
- [ ] **Member 1-6**: Create notebook in `pipelines/0-preprocess/category_X_exploration.ipynb`

**Deliverables**:

- Individual exploration notebooks for each category
- Data quality report for each category

#### 1.4 Integration & Testing

- [ ] Create unified data loading pipeline in `pipelines/0-preprocess/load_all_categories.py`
- [ ] Test loading all 6 categories simultaneously
- [ ] Verify DataFrame schemas are consistent across categories
- [ ] Document memory/performance considerations

**Deliverables**:

- Working data loading pipeline for all categories
- Performance benchmarks

---

## Phase 2: Data Transformation (Етап трансформації)

### Objectives

1. Obtain general information about the dataset
2. Get statistics on numerical columns
3. Formulate 6 business questions per team member (36 total)
4. Implement queries using filters, joins, group by, and window functions

### Tasks

#### 2.1 Dataset Overview & Statistics

- [ ] Get schema information for all categories (`.printSchema()`)
- [ ] Count total rows and columns per category
- [ ] Get statistics for numerical columns (`.describe()`, `.summary()`)
- [ ] Analyze data distribution (ratings, review lengths, dates, prices)
- [ ] Create visualization of key statistics
- [ ] Document findings in `docs/data_analysis_report.md`

**Deliverables**:

- `pipelines/1-transform/dataset_overview.py` - Script for generating statistics
- `docs/data_analysis_report.md` - Comprehensive data analysis report
- Visualizations of key metrics

#### 2.2 Business Questions Formulation

Each team member must create **6 business questions** following these requirements:

- At least **3 questions** using **filters**
- At least **2 questions** using **joins**
- At least **2 questions** using **group by**
- At least **2 questions** using **window functions**

**Note**: Questions should be unique across team members!

##### Example Business Questions:

**Filters (3+ questions):**

1. What are the top-rated products (4.5+ stars) with at least 100 reviews?
2. Which verified purchase reviews have helpfulness ratio > 0.8?
3. What products were reviewed in the last 6 months with negative sentiment?

**Joins (2+ questions):**

1. What is the average rating per product category with price ranges?
2. Which reviewers have written the most reviews across multiple categories?

**Group By (2+ questions):**

1. What is the average rating per month for each category?
2. What is the distribution of review lengths by star rating?

**Window Functions (2+ questions):**

1. What is the running average of ratings over time for each product?
2. Rank products within each category by total number of reviews?

#### 2.3 Business Questions Implementation (Each Team Member)

- [ ] **Member 1**: Define 6 business questions for Category 1
- [ ] **Member 1**: Implement queries in `pipelines/0-preprocess/category1_queries.py`
- [ ] **Member 2**: Define 6 business questions for Category 2
- [ ] **Member 2**: Implement queries in `pipelines/0-preprocess/category2_queries.py`
- [ ] **Member 3**: Define 6 business questions for Category 3
- [ ] **Member 3**: Implement queries in `pipelines/0-preprocess/category3_queries.py`
- [ ] **Member 4**: Define 6 business questions for Category 4
- [ ] **Member 4**: Implement queries in `pipelines/0-preprocess/category4_queries.py`
- [ ] **Member 5**: Define 6 business questions for Category 5
- [ ] **Member 5**: Implement queries in `pipelines/0-preprocess/category5_queries.py`
- [ ] **Member 6**: Define 6 business questions for Category 6
- [ ] **Member 6**: Implement queries in `pipelines/0-preprocess/category6_queries.py`

**Deliverables**:

- 6 query modules (one per member)
- Documentation of all 36 business questions in `docs/business_questions.md`

#### 2.4 Query Validation & Testing

- [ ] Create test cases for each query
- [ ] Verify query results are correct and meaningful
- [ ] Optimize queries for performance
- [ ] Document query execution times

**Deliverables**:

- Test suite for all queries
- Performance optimization report

---

## Phase 3: Data Analysis - ML Models (Етап аналізу даних)

### Objectives

1. Build regression and classification models using PySpark MLlib
2. Perform data preprocessing for ML
3. Select and train at least 3 different models for regression and classification
4. Evaluate model quality
5. Compare results across algorithms

### Tasks

#### 3.1 Data Preprocessing for ML

- [ ] Handle missing values (imputation or removal)
- [ ] Feature engineering:
  - Extract features from review text (TF-IDF, word counts, sentiment)
  - Create temporal features (review date, time since product launch)
  - Encode categorical variables
  - Create review helpfulness ratio
- [ ] Create feature vectors using VectorAssembler
- [ ] Split data into train/test sets (80/20 or 70/30)
- [ ] Implement preprocessing pipeline in `pipelines/2-eval/preprocessing.py`

**Deliverables**:

- `pipelines/2-eval/preprocessing.py` - Preprocessing pipeline
- Preprocessed datasets ready for training

#### 3.2 Regression Task Definition

**Possible Regression Tasks:**

- Predict product rating based on review text and metadata
- Predict review helpfulness score
- Predict product price based on reviews and ratings

**Selected Task**: [To be decided by team]

- [ ] Define regression target variable
- [ ] Select relevant features
- [ ] Document task rationale in `docs/ml_tasks.md`

#### 3.3 Regression Models Implementation

Train at least **3 regression models**:

- [ ] **Model 1**: Linear Regression

  - Implement in `pipelines/2-eval/regression_linear.py`
  - Train on combined dataset
  - Evaluate RMSE and R²

- [ ] **Model 2**: Random Forest Regressor

  - Implement in `pipelines/2-eval/regression_rf.py`
  - Tune hyperparameters (numTrees, maxDepth)
  - Evaluate RMSE and R²

- [ ] **Model 3**: Gradient Boosted Trees Regressor
  - Implement in `pipelines/2-eval/regression_gbt.py`
  - Tune hyperparameters
  - Evaluate RMSE and R²

**Optional Additional Models:**

- Decision Tree Regressor
- Generalized Linear Regression

**Deliverables**:

- 3+ trained regression models
- Model artifacts saved to `models/regression/`

#### 3.4 Classification Task Definition

**Possible Classification Tasks:**

- Classify reviews as positive/negative (binary: rating > 3.5)
- Classify review helpfulness (helpful vs not helpful)
- Multi-class: Predict exact star rating (1-5 stars)
- Classify verified vs unverified purchases

**Selected Task**: [To be decided by team]

- [ ] Define classification target variable
- [ ] Handle class imbalance if needed
- [ ] Select relevant features
- [ ] Document task rationale in `docs/ml_tasks.md`

#### 3.5 Classification Models Implementation

Train at least **3 classification models**:

- [ ] **Model 1**: Logistic Regression

  - Implement in `pipelines/2-eval/classification_lr.py`
  - Train on combined dataset
  - Evaluate Accuracy, Precision, Recall, F1-score

- [ ] **Model 2**: Random Forest Classifier

  - Implement in `pipelines/2-eval/classification_rf.py`
  - Tune hyperparameters (numTrees, maxDepth)
  - Evaluate Accuracy, Precision, Recall, F1-score

- [ ] **Model 3**: Gradient Boosted Trees Classifier
  - Implement in `pipelines/2-eval/classification_gbt.py`
  - Tune hyperparameters
  - Evaluate Accuracy, Precision, Recall, F1-score

**Optional Additional Models:**

- Naive Bayes
- Decision Tree Classifier
- Support Vector Machine (if available)

**Deliverables**:

- 3+ trained classification models
- Model artifacts saved to `models/classification/`

#### 3.6 Model Evaluation & Analysis

- [ ] Calculate evaluation metrics for all models:
  - **Regression**: RMSE, R², MAE, MSE
  - **Classification**: Accuracy, Precision, Recall, F1-score, ROC-AUC
- [ ] Create confusion matrices for classification models
- [ ] Analyze feature importance
- [ ] Compare model performance across algorithms
- [ ] Visualize results (charts, graphs)
- [ ] Document findings in `docs/model_evaluation_report.md`

**Deliverables**:

- `pipelines/2-eval/evaluate_models.py` - Evaluation script
- `docs/model_evaluation_report.md` - Comprehensive evaluation report
- Visualization of model comparisons

#### 3.7 Hyperparameter Tuning

- [ ] Use CrossValidator or TrainValidationSplit
- [ ] Define parameter grids for each model
- [ ] Tune hyperparameters for best performing models
- [ ] Document optimal parameters

**Deliverables**:

- Tuned models with improved performance
- Documentation of hyperparameter tuning process

---

## Phase 4: Results Export (Етап запису результатів)

### Objectives

1. Export business question results to CSV files
2. Export model predictions and evaluation metrics
3. Organize output directory structure
4. Ensure results directory is in .gitignore

### Tasks

#### 4.1 Business Questions Results Export

- [ ] Create output directory structure: `results/business_questions/`
- [ ] Export each query result to separate CSV file
- [ ] Naming convention: `member{X}_question{Y}_result.csv`
- [ ] Add metadata files describing each result
- [ ] Create summary report with all business insights

**Deliverables**:

- `pipelines/3-infer/export_queries.py` - Script to export query results
- CSV files with query results (not in git)
- `results/business_questions/README.md` - Description of results

#### 4.2 Model Results Export

- [ ] Export model predictions: `results/predictions/`
- [ ] Export evaluation metrics: `results/metrics/`
- [ ] Export feature importance: `results/feature_importance/`
- [ ] Save model artifacts: `models/` (add to .gitignore if large)
- [ ] Create model comparison report

**Deliverables**:

- `pipelines/3-infer/export_models.py` - Script to export model results
- Model predictions and metrics (not in git)
- `results/models/README.md` - Description of model outputs

#### 4.3 Update .gitignore

- [ ] Add `data/` to .gitignore (raw dataset)
- [ ] Add `results/` to .gitignore (query and model outputs)
- [ ] Add `models/*.model` to .gitignore (if models are large)
- [ ] Keep model evaluation reports in git

**Deliverables**:

- Updated `.gitignore` file

#### 4.4 Final Documentation

- [ ] Create comprehensive README.md with:
  - Project overview
  - Dataset description
  - Team member contributions
  - How to run the project
  - Results summary
- [ ] Document all phases in `docs/project_report.md`
- [ ] Create presentation slides (optional)

**Deliverables**:

- Complete project documentation
- README.md with instructions
- Final project report

---

## Team Collaboration Guidelines

### Git Workflow

1. Each team member works on their own feature branch
2. Branch naming: `feature/{member-name}/{task-description}`
3. Create pull requests to `dev` branch
4. Require at least 1 code review before merging
5. Merge to `main` only after phase completion

### Code Standards

- Follow PEP 8 style guide for Python
- Add docstrings to all functions (Google style)
- Include type hints where applicable
- Write unit tests for critical functions
- Use meaningful variable and function names

### Communication

- Daily standup (async updates in chat)
- Weekly team meetings to sync progress
- Document decisions in `docs/decisions.md`
- Share blockers immediately

---

## Bonus Opportunities (+25%)

To earn the team collaboration bonus:

- ✅ Team of 6 members (requirement met)
- [ ] Each member contributes to every phase (tracked in git commits)
- [ ] Create `docs/team_roles.md` documenting each member's role per phase
- [ ] Each member creates 6 unique business questions (36 total)
- [ ] Regular pull requests and code reviews

---

## Success Criteria

### Phase 1: Data Extraction ✓

- [ ] All 6 categories successfully loaded
- [ ] Schemas properly defined and documented
- [ ] Data loading functions tested and working
- [ ] No data corruption or missing files

### Phase 2: Data Transformation ✓

- [ ] Dataset statistics documented
- [ ] 36 business questions defined (6 per member)
- [ ] All queries implemented and tested
- [ ] Query requirements met (filters, joins, group by, window functions)

### Phase 3: ML Models ✓

- [ ] 3+ regression models trained and evaluated
- [ ] 3+ classification models trained and evaluated
- [ ] RMSE and R² calculated for regression
- [ ] Accuracy, Precision, Recall, F1 calculated for classification
- [ ] Model comparison completed

### Phase 4: Results Export ✓

- [ ] All query results exported to CSV
- [ ] Model results and metrics exported
- [ ] .gitignore properly configured
- [ ] Complete documentation delivered

---

## Resources

### Amazon Reviews 2023 Dataset

- Main site: https://amazon-reviews-2023.github.io/
- Categories to consider: Electronics, Books, Clothing, Home & Kitchen, Sports, Beauty, etc.
- File formats: JSON/JSON.gz
- Download instructions: Follow dataset website guidelines

### PySpark Documentation

- PySpark SQL: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/index.html
- PySpark MLlib: https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html
- PySpark DataFrame API: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html

### Example Code Structure

```
amazon-reviews-analysis/
├── src/amazon_reviews_analysis/
│   ├── __init__.py
│   ├── schemas.py
│   ├── data_loader.py
│   ├── queries.py
│   └── models.py
├── pipelines/
│   ├── 0-preprocess/
│   │   ├── load_all_categories.py
│   │   └── category_*_exploration.ipynb
│   ├── 1-transform/
│   │   ├── dataset_overview.py
│   │   └── member*_queries.py
│   ├── 2-eval/
│   │   ├── preprocessing.py
│   │   ├── regression_*.py
│   │   └── classification_*.py
│   └── 3-infer/
│       ├── export_queries.py
│       └── export_models.py
├── docs/
│   ├── tasks.md
│   ├── business_questions.md
│   ├── data_analysis_report.md
│   ├── ml_tasks.md
│   ├── model_evaluation_report.md
│   └── team_roles.md
└── tests/
    └── test_*.py
```

---

## Notes

- **Data Location**: Store raw dataset outside the project directory (e.g., `~/datasets/amazon-reviews-2023/`)
- **Processing**: Use PySpark for all data operations (no pandas on large datasets)
- **Resources**: Monitor memory usage; use sampling for development/testing
- **Collaboration**: Use feature branches and pull requests for all changes
- **Documentation**: Keep all documentation up to date as work progresses

Good luck with your Big Data Analysis project! 🚀
