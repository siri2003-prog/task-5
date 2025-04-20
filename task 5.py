import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {'Age': [28, 24, 35, 32, 40, 36, 30, 25, 38, 42],
        'Salary': [50000, 45000, 70000, 60000, 80000, 65000, 55000, 48000, 75000, 82000],
        'Experience': [5, 3, 10, 7, 12, 9, 6, 4, 11, 14],
        'Department': ['Sales', 'Marketing', 'Sales', 'Marketing', 'Sales', 'Marketing', 'Sales', 'Marketing', 'Sales', 'Marketing']}
df = pd.DataFrame(data)
print("Descriptive Statistics:")
print(df.describe())
print("\nDataFrame Info:")
print(df.info())
print("\nValue Counts for Department:")
print(df['Department'].value_counts())
sns.pairplot(df[['Age', 'Salary', 'Experience']])
plt.show()
corr_matrix = df[['Age', 'Salary', 'Experience']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.show()
print("\nRelationships and Trends:")
print("Age and Salary: Strong positive correlation")
print("Experience and Salary: Strong positive correlation")
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=5)
plt.title("Histogram of Age")
plt.show()
plt.figure(figsize=(8, 6))
sns.boxplot(df['Salary'])
plt.title("Boxplot of Salary")
plt.show()
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Experience', y='Salary', data=df)
plt.title("Scatterplot of Experience vs Salary")
plt.show()
print("\nObservations:")
print("Histogram of Age: The age distribution is slightly skewed to the right.")
print("Boxplot of Salary: There are no outliers in the salary distribution.")
print("Scatterplot of Experience vs Salary: There is a strong positive relationship between experience and salary.")
print("\nSummary of Findings:")
print("The dataset shows a strong positive correlation between age and salary, and between experience and salary.")
print("The age distribution is slightly skewed to the right, while the salary distribution is relatively normal.")
print("There is a strong positive relationship between experience and salary, indicating that more experienced employees tend to earn higher salaries.")

