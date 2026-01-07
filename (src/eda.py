import matplotlib.pyplot as plt
import seaborn as sns

def plot_attrition_by_department(df):
    sns.countplot(x='Department', hue='Attrition', data=df)
    plt.title("Attrition by Department")
    plt.show()

def plot_income_vs_attrition(df):
    sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
    plt.title("Monthly Income vs Attrition")
    plt.show()
