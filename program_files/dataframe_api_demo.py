import matplotlib.pyplot as plt
import pandas_datareader as pdr
print("""This short tutorial demonstrates how to use the Yahoo Finance API 
to download "real time" data for any stock. To do this:
1. pip install pandas-datareader
2. import the datareader 
3. execute a one-liner to get the data of your choice:
   dataframe = pdr.get_data_yahoo('ZNGA', start='2021-03-01', end='2020-03-01')
   *Note both start and end are optional
 Let's try it""")
input('Enter to continue')
print("Fetching data...")

dataframe = pdr.get_data_yahoo('ZNGA', start='2020-04-01')

print("Success!")
input('Enter to continue')
print()
print("""The data downloaded comes in a convenient matrix-like structure
called a DataFrame - one of the two main structures in the pandas library. 
The other structure is called a Series, and is analogous to a single
column in a in a table of data with a separate index. Actually a DataFrame 
is two or more Series stacked together.   
A data frame can also be compared to a spreadsheet with rows and columns. 
Let take a look at the first few rows of our downloaded data with this code:
dataframe.head()""")
print()
input('Enter to continue')
print()
print(dataframe.head())
print()
print("""As you can see the Head function by default calls the first five rows of a
DataFrame (or a Series). You can also see the data is roughly organized into columns
rows, and that the name of each column appears as the first row. The Left column
containing the dates is the DataFrame's index.""")
input('Enter to continue')
print()

print("""You can easily subset by either column(s) or row(s), but for this 
exercise we want to subset by a single column and then graph that column. Let's start 
by getting just the first few rows of the Close column:
dataframe['Close'].head()""")
input('Enter to continue')

print(dataframe['Close'].head())
print()
input('Enter to continue')
print("""You can also easily output descriptive statistics for the entire dataframe
or for a single column with the .describe method. Let's try it for the Close column:
dataframe['Close'].describe().""")
input('Enter to continue')
print()
print(dataframe['Close'].describe())

input('Enter to continue')
print()
print("""You can store the subset of a DataFrame as it own variable. For example
close = dataframe['Close'], which you can then use to do many interesting things
like plotting graphs:
plt.plot(close)
plt.grid(True, alpha = 0.3)
plt.show()""")
input('Enter to continue')
close = dataframe['Close']
plt.plot(close)
plt.grid(True, alpha = 0.3)
plt.show()




