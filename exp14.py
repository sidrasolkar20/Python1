import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def demonstrate_series():
    """
    Demonstrates creating and manipulating pandas Series objects
    """
    print("=" * 50)
    print("PANDAS SERIES DEMONSTRATION")
    print("=" * 50)
    
    # Creating a Series from a list
    data_list = [10, 20, 30, 40, 50]
    series1 = pd.Series(data_list)
    print("Series from list:")
    print(series1)
    print()
    
    # Creating a Series with custom indices
    series2 = pd.Series(data_list, index=['a', 'b', 'c', 'd', 'e'])
    print("Series with custom indices:")
    print(series2)
    print()
    
    # Creating a Series from a dictionary
    data_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
    series3 = pd.Series(data_dict)
    print("Series from dictionary:")
    print(series3)
    print()
    
    # Series operations
    print("Series arithmetic operations:")
    print("series2 + series3:")
    print(series2 + series3)
    print()
    
    # Series methods and attributes
    print("Series attributes and methods:")
    print(f"Shape: {series3.shape}")
    print(f"Size: {series3.size}")
    print(f"Index: {series3.index}")
    print(f"Data type: {series3.dtype}")
    print(f"Mean value: {series3.mean()}")
    print(f"Max value: {series3.max()}")
    print(f"Min value: {series3.min()}")
    print()
    
    # Series filtering
    print("Series filtering:")
    print("Values greater than 300:")
    print(series3[series3 > 300])
    print()


def demonstrate_dataframes():
    """
    Demonstrates creating and manipulating pandas DataFrame objects
    """
    print("=" * 50)
    print("PANDAS DATAFRAME DEMONSTRATION")
    print("=" * 50)
    
    # Creating a DataFrame from a dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 22],
        'City': ['New York', 'Chicago', 'Boston', 'Detroit', 'Miami'],
        'Salary': [50000, 60000, 70000, 80000, 65000]
    }
    
    df = pd.DataFrame(data)
    print("DataFrame from dictionary:")
    print(df)
    print()
    
    # Accessing columns
    print("Accessing a single column (returns a Series):")
    print(df['Name'])
    print()
    
    print("Accessing multiple columns:")
    print(df[['Name', 'Salary']])
    print()
    
    # Adding a new column
    df['Experience'] = [2, 5, 8, 12, 3]
    print("DataFrame after adding a new column:")
    print(df)
    print()
    
    # Basic statistics
    print("DataFrame statistics:")
    print(df.describe())
    print()
    
    # Filtering rows
    print("Filtering rows (employees with salary > 60000):")
    print(df[df['Salary'] > 60000])
    print()
    
    # Sorting
    print("Sorting by Age (ascending):")
    print(df.sort_values(by='Age'))
    print()
    
    print("Sorting by Salary (descending):")
    print(df.sort_values(by='Salary', ascending=False))
    print()
    
    # GroupBy operations
    # Create a larger DataFrame with some repeated values
    cities = ['New York', 'Chicago', 'Boston', 'New York', 'Chicago',
              'Boston', 'Miami', 'Miami', 'New York', 'Chicago']
    departments = ['HR', 'IT', 'Marketing', 'IT', 'HR', 
                  'Marketing', 'IT', 'HR', 'Marketing', 'IT']
    salaries = [55000, 65000, 60000, 70000, 65000,
               75000, 62000, 59000, 72000, 80000]
    
    df_grouped = pd.DataFrame({
        'City': cities,
        'Department': departments,
        'Salary': salaries
    })
    
    print("New DataFrame for grouping operations:")
    print(df_grouped)
    print()
    
    # Group by one column
    print("Group by City and calculate mean salary:")
    print(df_grouped.groupby('City')['Salary'].mean())
    print()
    
    # Group by multiple columns
    print("Group by City and Department:")
    print(df_grouped.groupby(['City', 'Department'])['Salary'].mean())
    print()
    
    # More groupby operations
    print("Various aggregations after grouping:")
    print(df_grouped.groupby('City')['Salary'].agg(['count', 'mean', 'min', 'max']))
    print()


def demonstrate_advanced_features():
    """
    Demonstrates advanced pandas features and operations
    """
    print("=" * 50)
    print("ADVANCED PANDAS FEATURES")
    print("=" * 50)
    
    # Sample DataFrame with dates
    date_range = pd.date_range('2023-01-01', periods=10, freq='D')
    df_dates = pd.DataFrame({
        'Date': date_range,
        'Value': np.random.randn(10).cumsum(),
        'Category': np.random.choice(['A', 'B', 'C'], 10)
    })
    
    print("DataFrame with dates:")
    print(df_dates)
    print()
    
    # Setting Date as index
    df_dates.set_index('Date', inplace=True)
    print("After setting Date as index:")
    print(df_dates)
    print()
    
    # Resampling time-series data
    print("Resampling to 3-day frequency (mean):")
    print(df_dates['Value'].resample('3D').mean())
    print()
    
    # Pivot tables
    # Reset index to get Date back as a column
    df_dates.reset_index(inplace=True)
    
    # Create a pivot table
    pivot = pd.pivot_table(df_dates, values='Value', 
                           index='Date', columns='Category',
                           aggfunc='sum')
    
    print("Pivot table by Date and Category:")
    print(pivot)
    print()
    
    # Missing data
    # Create a DataFrame with some missing values
    df_missing = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, 5],
        'C': [1, 2, 3, np.nan, 5]
    })
    
    print("DataFrame with missing values:")
    print(df_missing)
    print()
    
    print("Check for missing values:")
    print(df_missing.isnull())
    print()
    
    print("Count of missing values per column:")
    print(df_missing.isnull().sum())
    print()
    
    print("Filling missing values with 0:")
    print(df_missing.fillna(0))
    print()
    
    print("Filling missing values with the mean of each column:")
    print(df_missing.fillna(df_missing.mean()))
    print()
    
    print("Dropping rows with any missing values:")
    print(df_missing.dropna())
    print()


if __name__ == "__main__":
    # Demonstrate Series
    demonstrate_series()
    
    # Demonstrate DataFrames
    demonstrate_dataframes()
    
    # Demonstrate advanced features
    demonstrate_advanced_features()
