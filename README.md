# Week 3 — Statistical Analysis and Hypothesis Testing in Python

## Project Overview
This project applies statistical inference to the cleaned UCI Iris working dataset carried forward from Weeks 1 and 2.

### Research Question
Do mean petal lengths differ among the three Iris species?

### Hypotheses
- **H0:** The population mean petal length is equal across Setosa, Versicolor, and Virginica.
- **H1:** At least one species has a different population mean petal length.

### Primary Analysis
Because the group variances are not homogeneous, the project reports **Welch's one-way ANOVA** as the primary robust omnibus test. A classical one-way ANOVA, Kruskal-Wallis test, assumption checks, confidence intervals, and pairwise Welch t-tests with Holm correction are included as supporting analyses.

### Main Result
Welch ANOVA provides extremely strong evidence against H0 for this dataset. Pairwise comparisons also show statistically significant differences in mean petal length between all three species after Holm correction.

## Visualizations
1. Petal-length violin/box distribution
2. Mean petal length with 95% confidence intervals
3. Q-Q plot of ANOVA residuals
4. Residuals by species
5. Pairwise mean differences
6. Petal-length density curves

## Project Structure
```text
week3-iris-statistical-analysis/
├── data/processed/iris_cleaned_week3.csv
├── docs/Week_3_Statistical_Analysis_Hypothesis_Testing_Report.docx
├── notebooks/Week_3_Statistical_Analysis_Hypothesis_Testing_FINAL.ipynb
├── reports/figures/
├── src/week3_statistical_analysis.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Run
```bash
pip install -r requirements.txt
jupyter notebook
```

Open the notebook and run all cells.

## Dataset
UCI Iris Dataset, Dataset ID 53. The Week 3 analysis uses the cleaned 149-row working dataset produced during Week 1/Week 2. No new artificial missing values or duplicates are introduced in Week 3.

## Interpretation
Statistical significance is interpreted using alpha = 0.05. P-values are reported with confidence intervals and effect-size context rather than being treated as a measure of practical importance by themselves.
