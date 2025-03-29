import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load dataset (Replace with your actual CSV file)
    file_path = "your_dataset.csv"  # Change to your dataset filename
    df = pd.read_csv(file_path)

    # Display the first few rows
    print("📌 First 5 rows of the dataset:")
    print(df.head())

    # Display dataset information (data types, missing values)
    print("\n📌 Dataset Info:")
    print(df.info())

    # Check for missing values
    print("\n📌 Missing Values in Each Column:")
    print(df.isnull().sum())

    # Handle missing values (Drop rows with missing values)
    df_cleaned = df.dropna()

    # Verify after cleaning
    print("\n📌 After Cleaning: Missing Values Count")
    print(df_cleaned.isnull().sum())

    # Save cleaned dataset
    df_cleaned.to_csv("cleaned_dataset.csv", index=False)
    print("\n✅ Cleaned dataset saved as 'cleaned_dataset.csv'")

except FileNotFoundError:
    print("❌ Error: File not found. Please check the file path.")
except Exception as e:
    print(f"❌ An error occurred: {e}")

# Task 2: Basic Data Analysis
print("\n📊 Basic Data Analysis")
print(df_cleaned.describe())  # Compute basic statistics

# Grouping example (Modify based on your dataset)
categorical_col = "Category"  # Change to an actual categorical column
numerical_col = "Sales"  # Change to an actual numerical column

if categorical_col in df_cleaned.columns and numerical_col in df_cleaned.columns:
    grouped_data = df_cleaned.groupby(categorical_col)[numerical_col].mean()
    print("\n📌 Average Sales per Category:")
    print(grouped_data)

# Task 3: Data Visualization
plt.figure(figsize=(12, 8))

# 1️⃣ Line Chart (Trends over time)
plt.subplot(2, 2, 1)
if "Date" in df_cleaned.columns:
    df_cleaned["Date"] = pd.to_datetime(df_cleaned["Date"])
    df_sorted = df_cleaned.sort_values("Date")
    plt.plot(df_sorted["Date"], df_sorted[numerical_col], marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel(numerical_col)
    plt.title("Trend Over Time")

# 2️⃣ Bar Chart (Comparison of numerical values across categories)
plt.subplot(2, 2, 2)
if categorical_col in df_cleaned.columns and numerical_col in df_cleaned.columns:
    sns.barplot(x=grouped_data.index, y=grouped_data.values)
    plt.xticks(rotation=45)
    plt.xlabel(categorical_col)
    plt.ylabel(numerical_col)
    plt.title("Average Sales per Category")

# 3️⃣ Histogram (Distribution of a numerical column)
plt.subplot(2, 2, 3)
sns.histplot(df_cleaned[numerical_col], bins=20, kde=True)
plt.xlabel(numerical_col)
plt.title(f"Distribution of {numerical_col}")

# 4️⃣ Scatter Plot (Relationship between two numerical columns)
plt.subplot(2, 2, 4)
numerical_col2 = "Profit"  # Change to another numerical column
if numerical_col in df_cleaned.columns and numerical_col2 in df_cleaned.columns:
    sns.scatterplot(x=df_cleaned[numerical_col], y=df_cleaned[numerical_col2])
    plt.xlabel(numerical_col)
    plt.ylabel(numerical_col2)
    plt.title(f"{numerical_col} vs {numerical_col2}")

plt.tight_layout()
plt.show()

