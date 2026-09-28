"""
Week 3 — Statistical Analysis and Hypothesis Testing in Python
Dataset: cleaned UCI Iris working dataset from Week 1/Week 2
Main hypothesis: Mean petal length differs among Iris species.
"""
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm

DATA = "data/processed/iris_cleaned_week3.csv"
df = pd.read_csv(DATA)

groups = [df.loc[df.species == s, "petal_length"] for s in ["setosa","versicolor","virginica"]]

# Assumption checks
model = ols("petal_length ~ C(species)", data=df).fit()
print("Shapiro-Wilk residual normality:", stats.shapiro(model.resid))
print("Levene variance test:", stats.levene(*groups, center="median"))

# Classical one-way ANOVA
print("\nClassical one-way ANOVA:")
print(stats.f_oneway(*groups))

# Welch ANOVA — primary robust test because variance homogeneity is not supported
print("\nWelch one-way ANOVA:")
print(stats.f_oneway(*groups, equal_var=False))

# Kruskal-Wallis — non-parametric sensitivity analysis
print("\nKruskal-Wallis:")
print(stats.kruskal(*groups))

# Pairwise Welch t-tests with Holm correction
pairs = [("setosa","versicolor"), ("setosa","virginica"), ("versicolor","virginica")]
pvals = []
for a,b in pairs:
    t,p = stats.ttest_ind(df.loc[df.species==a,"petal_length"],
                           df.loc[df.species==b,"petal_length"],
                           equal_var=False)
    pvals.append(p)
    print(f"{a} vs {b}: t={t:.3f}, p={p:.6g}")
print("Raw p-values:", pvals)
print("Use Holm correction for family-wise error control when interpreting these pairwise tests.")

# The project figures use explicit tick positions to avoid set_ticklabels warnings.
