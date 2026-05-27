# ============================================
# Exploratory Data Analysis (EDA) Project
# Student Performance Analysis
# ============================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Settings
plt.rcParams['figure.figsize'] = (10,6)
sns.set_style("whitegrid")

# ============================================
# Load Dataset
# ============================================

df = pd.read_excel(
    r"E:\Exploratory Data Analysis (EDA) Project\student_performance.xlsx"
)


# ============================================
# Basic Dataset Information
# ============================================

print("First 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ============================================
# Check Missing Values
# ============================================

print("\nMissing Values")
print(df.isnull().sum())

# ============================================
# Check Duplicate Rows
# ============================================

print("\nDuplicate Rows")
print(df.duplicated().sum())

# ============================================
# Correlation Analysis
# ============================================

numeric_df = df[['math_score', 'reading_score', 'writing_score']]

correlation = numeric_df.corr()

print("\nCorrelation Matrix")
print(correlation)

# ============================================
# Visualization 1: Correlation Heatmap
# ============================================

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()

# ============================================
# Visualization 2: Distribution of Math Scores
# ============================================

sns.histplot(df['math_score'], bins=10, kde=True)

plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")

plt.show()

# ============================================
# Visualization 3: Gender-wise Performance
# ============================================

gender_scores = df.groupby('gender')[
    ['math_score', 'reading_score', 'writing_score']
].mean()

print("\nAverage Scores by Gender")
print(gender_scores)

gender_scores.plot(kind='bar')

plt.title("Average Scores by Gender")
plt.ylabel("Average Score")
plt.xticks(rotation=0)

plt.show()

# ============================================
# Visualization 4: Lunch Type vs Math Score
# ============================================

sns.boxplot(
    x='lunch',
    y='math_score',
    data=df
)

plt.title("Lunch Type vs Math Score")

plt.show()

# ============================================
# Visualization 5: Parental Education Impact
# ============================================

sns.barplot(
    x='parental_education',
    y='math_score',
    data=df
)

plt.title("Parental Education vs Math Score")

plt.show()

# ============================================
# Visualization 6: Pair Plot
# ============================================

sns.pairplot(
    df,
    hue='gender'
)

plt.show()

# ============================================
# Key Insights
# ============================================

print("\n========== KEY INSIGHTS ==========")

print("""
1. Reading and writing scores are strongly correlated.

2. Female students perform better in reading and writing.

3. Students with standard lunch score higher.

4. Higher parental education positively affects performance.

5. Math scores vary more compared to reading and writing scores.
""")

# ============================================
# Conclusion
# ============================================

print("\nEDA Project Completed Successfully!")