# Week 3 — Statistical Analysis and Hypothesis Testing in Python

> **Data Science Internship | Statistical Inference | Python | UCI Iris Dataset**

## 📌 Project Overview

This project focuses on **statistical analysis and hypothesis testing using Python**. It applies statistical inference techniques to the cleaned **UCI Iris working dataset** carried forward from Weeks 1 and 2.

The primary objective is to formulate a well-defined statistical hypothesis, evaluate the underlying assumptions, apply appropriate inferential tests, quantify uncertainty, and interpret the statistical findings using reproducible Python workflows.

---

## 🎯 Research Question

**Do mean petal lengths differ significantly among the three Iris species?**

The analysis investigates whether the observed differences in petal length between **Setosa, Versicolor, and Virginica** provide sufficient statistical evidence to conclude that their population means are not all equal.

---

## 🧪 Hypotheses

### Null Hypothesis — H₀

> The population mean petal length is equal across Setosa, Versicolor, and Virginica.

### Alternative Hypothesis — H₁

> At least one Iris species has a different population mean petal length.

### Significance Level

**α = 0.05**

---

## 📊 Primary Statistical Analysis

The analysis uses **Welch's One-Way ANOVA** as the primary omnibus test because the group variances are not homogeneous.

Additional statistical procedures are included to strengthen the analysis and validate the findings:

* Classical One-Way ANOVA
* Levene's Test for Homogeneity of Variance
* Shapiro-Wilk Residual Normality Test
* Kruskal-Wallis Non-Parametric Test
* Pairwise Welch's t-Tests
* Holm Multiple-Comparison Correction
* 95% Confidence Intervals
* Effect-Size Analysis

This combination provides both **parametric and non-parametric evidence**, along with assumption checks and uncertainty estimates.

---

## 📈 Main Statistical Finding

The **Welch One-Way ANOVA** provides extremely strong statistical evidence against the null hypothesis for the analyzed dataset.

Pairwise Welch's t-tests further indicate statistically significant differences in mean petal length between all three species after applying **Holm's correction for multiple comparisons**.

The interpretation considers statistical significance together with **confidence intervals and effect sizes**, rather than treating a p-value alone as an indicator of practical importance.

---

## 📉 Visualizations

The project includes six supporting visualizations designed to complement the statistical analysis:

| # | Visualization                        | Purpose                                     |
| - | ------------------------------------ | ------------------------------------------- |
| 1 | Petal-Length Violin/Box Distribution | Compare species-level distributions         |
| 2 | Mean Petal Length with 95% CIs       | Visualize group means and uncertainty       |
| 3 | Q-Q Plot of ANOVA Residuals          | Examine residual normality                  |
| 4 | Residuals by Species                 | Inspect residual patterns across groups     |
| 5 | Pairwise Mean Differences            | Visualize differences between species means |
| 6 | Petal-Length Density Curves          | Compare distribution shapes and overlap     |

These visualizations provide graphical evidence for **distributional differences, uncertainty, group comparisons, and model assumptions**.

---

## 🛠️ Technologies and Tools

The project was developed using the following technologies:

* **Python**
* **Pandas** — Data manipulation and descriptive analysis
* **NumPy** — Numerical computation
* **SciPy** — Statistical hypothesis testing
* **Statsmodels** — Statistical modelling and inference
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **Jupyter Notebook** — Interactive analysis and reproducibility

---

## 📁 Project Structure

```text
week3-iris-statistical-analysis-hypothesis-testing/
│
├── data/
│   └── processed/
│       └── iris_cleaned_week3.csv
│
├── docs/
│   └── Week_3_Statistical_Analysis_Hypothesis_Testing_Report.docx
│
├── notebooks/
│   └── Week_3_Statistical_Analysis_Hypothesis_Testing_FINAL.ipynb
│
├── reports/
│   └── figures/
│       ├── 01_petal_length_distribution.png
│       ├── 02_mean_ci.png
│       ├── 03_qq_residuals.png
│       ├── 04_residuals_by_species.png
│       ├── 05_pairwise_mean_differences.png
│       └── 06_density.png
│
├── src/
│   └── week3_statistical_analysis.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Vikas-Yadav-6696/week3-iris-statistical-analysis-hypothesis-testing.git
```

### 2. Navigate to the Project Directory

```bash
cd week3-iris-statistical-analysis-hypothesis-testing
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

### 5. Open the Analysis Notebook

Navigate to:

```text
notebooks/Week_3_Statistical_Analysis_Hypothesis_Testing_FINAL.ipynb
```

Run the notebook cells sequentially to reproduce the statistical analysis, calculations, and visualizations.

---

## 🗂️ Dataset

The project uses the **UCI Iris Dataset — Dataset ID 53**.

The Week 3 analysis is based on the **149-row cleaned working dataset** produced during Weeks 1 and 2.

No new artificial missing values or duplicate records are introduced during Week 3. The focus of this stage is statistical inference and hypothesis testing using the cleaned dataset.

### Dataset Characteristics

* **Dataset:** UCI Iris
* **Dataset ID:** 53
* **Working observations:** 149
* **Species:** Setosa, Versicolor, Virginica
* **Primary variable analyzed:** Petal Length
* **Data source:** UCI Machine Learning Repository

---

## 🔬 Statistical Workflow

The project follows a structured inferential workflow:

```text
Cleaned Iris Dataset
        │
        ▼
Descriptive Statistics
        │
        ▼
Assumption Checks
        │
        ├── Levene's Test
        └── Shapiro-Wilk Test
        │
        ▼
Welch One-Way ANOVA
        │
        ▼
Pairwise Welch's t-Tests
        │
        ▼
Holm Multiple-Comparison Correction
        │
        ▼
95% Confidence Intervals
        │
        ▼
Effect-Size Analysis
        │
        ▼
Statistical Interpretation
```

A **classical ANOVA** and **Kruskal-Wallis test** are also included as supporting analyses to assess whether the overall conclusion is consistent across different statistical approaches.

---

## 📐 Statistical Interpretation

All hypothesis tests are evaluated using:

> **Significance Level: α = 0.05**

The analysis considers multiple dimensions of statistical evidence:

* **P-values**
* **95% confidence intervals**
* **Effect sizes**
* **Distributional assumptions**
* **Variance assumptions**
* **Multiple-comparison correction**
* **Agreement between parametric and non-parametric methods**

A statistically significant result is not interpreted as automatically representing practical importance. The findings are considered alongside **effect sizes, confidence intervals, assumptions, and dataset characteristics**.

---

## 🔎 Key Analytical Components

### Descriptive Analysis

Species-level descriptive statistics are used to summarize the central tendency and variability of petal length before conducting inferential tests.

### Assumption Testing

Statistical assumptions are examined before selecting the primary inferential approach.

* **Levene's test** evaluates homogeneity of variance.
* **Shapiro-Wilk testing and Q-Q plots** assess residual normality.

### Omnibus Testing

**Welch's One-Way ANOVA** is used as the primary robust test for detecting differences among the three species means.

Classical ANOVA and Kruskal-Wallis testing provide additional supporting evidence.

### Post-Hoc Analysis

When examining differences between individual species, **pairwise Welch's t-tests** are performed with **Holm correction** to control for multiple comparisons.

### Effect Sizes and Uncertainty

The analysis supplements hypothesis-test results with:

* 95% confidence intervals
* Eta-squared
* Omega-squared
* Pairwise mean differences

This provides a more complete interpretation than relying on p-values alone.

---

## 📋 Reproducibility

The repository contains the complete analytical workflow required to reproduce the project:

* Cleaned dataset
* Python source code
* Jupyter Notebook
* Statistical visualizations
* Word report
* Requirements file
* README documentation
* MIT License
* Git configuration

The analysis can therefore be reviewed, executed, and reproduced using the files provided in the repository.

---

## 📄 Project Documentation

The complete statistical analysis and interpretation are documented in:

```text
docs/
└── Week_3_Statistical_Analysis_Hypothesis_Testing_Report.docx
```

The report contains:

* Introduction
* Research question
* Hypotheses
* Dataset and methodology
* Descriptive statistics
* Assumption testing
* Statistical tests
* Visualizations
* Results
* Confidence intervals
* Effect sizes
* Interpretation
* Limitations
* Conclusion
* Reproducibility information
* References

---

## 🎓 Internship Context

This project was completed as part of **Week 3 of the Data Science Internship**, with a focus on:

> **Statistical Analysis and Hypothesis Testing in Python**

The project demonstrates practical experience with statistical inference, hypothesis formulation, assumption checking, statistical testing, visualization, interpretation, and reproducible data-analysis workflows.

---

## 👨‍💻 Author

**Vikas Yadav**
**MCA-DSAI | Data Science Intern**

---

## 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for complete license information.
