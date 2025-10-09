"""
Understand what data science is and how it's applied
Navigate the complete data science life cycle
Work with Python's most popular data science packages
Create and manipulate datasets
Build visualizations to communicate your findings
Part 1: Understanding Data Science

What is Data Science?

Let's start with the basics. Data science is an interdisciplinary field where you'll discover patterns and describe relationships using data. You'll combine techniques from computer science and statistics, writing code to store, modify, and visualize large datasets.

As a data scientist, you'll also build, test, and interpret data models—representations of real-life systems that organize data elements and show how they relate to one another.

Example: Think of the FBI's Most Wanted list. This model contains data elements like eye color, hair color, and known accomplices for each suspect. 
You can use this data model to make predictions about new data.

Understanding Datasets
You'll work extensively with datasets—collections of information that consist of features and instances.

Key terminology you need to know:
Feature (or variable): A characteristic that can be measured or observed. Features are organized in columns.
Instance (or observational unit): Individual data points or observations. Instances are organized in rows.
Working with Big Data

Over the last 20 years, data science has exploded due to big data—datasets with:
Large volume (massive amounts of data)
High velocity (created and updated quickly)
Wide variety (different structures and formats)
Volume: Managing Large Datasets

You'll use specialized tools to handle very large amounts of data:
Apache Spark and Hadoop: Open-source platforms for storing and analyzing large datasets
Cloudera: Software for cloud-based data storage and management
Cloud-based storage: Amazon Web Services, Google Cloud, or Microsoft Azure spread datasets across different locations, loading only what you need when you need it
Velocity: Keeping Up with Changing Data

Learn these techniques to work with continuously updating datasets:
Write reproducible code: Your analyses can be updated and quickly re-run, unlike Excel-based analyses
Automate your analyses: Schedule your code to run at specific times (like once per week)
Use version control: Ensure that new software versions don't break your analysis
Variety: Handling Different Data Types

You'll encounter data in many forms: tables, spreadsheets, images, videos, sound, text, and more. This tutorial will teach you techniques from statistics, computer science, machine learning, and artificial intelligence to handle this variety.

The Data Science Life Cycle
Now let's walk through the five-step process you'll follow for every data science project. You may revisit these steps multiple times during a single project.

Step 1: Gathering Data
What you'll do: Identify available and relevant data, then gather new data if needed.
You'll encounter two types of data:
Structured data: Stored in a pre-defined format, typically with features in columns and instances in rows.
Example: Databases and tables

Unstructured data: Has no predefined format and is difficult to interpret without processing.
Example: Audio files, videos, images, and text

You may work with both types during a single project.

Step 2: Cleaning Data
What you'll do: Reformat datasets, create new features, and address missing values.
Most software requires datasets to be structured as tables with features in columns and instances in rows. You'll:
Combine data from multiple sources
Ensure proper formatting
Examine datasets for missing values or errors
Calculate new features based on available data

Step 3: Exploring Data
What you'll do: Create data visualizations and calculate summary statistics to explore potential relationships.
During exploratory data analysis, you'll use plots and graphs to:
Recognize patterns or trends
Identify unusual observations
Brainstorm appropriate models
Calculate summary statistics like mean and median

Step 4: Modeling Data
What you'll do: Use modeling skills and content knowledge to fit and evaluate models, measure relationships, and make predictions.
You'll select from different model types:
Supervised models (predict features with known values):
Classification models: Predict categorical features
Regression models: Predict numerical features
Unsupervised models: Look for hidden groups or patterns without predicting a known feature

Remember: No model is ideal for every situation, so you'll try several before making your selection.

Step 5: Interpreting Data
What you'll do: Describe and interpret conclusions through written reports and presentations.
Communication is essential! You'll learn to:
Interpret model results effectively
Communicate findings to both technical and non-technical audiences
Adapt models for changing circumstances or new data

Part 3: Introduction to Python for Data Science
Why Python?
Python is one of the most popular languages for data science. Here's why you'll be learning it:

Advantages:
Readability: Python reads like English with consistent syntax
Popularity: Widely used in industry with abundant learning resources
Innovation: New data science models and technologies are constantly added

Disadvantages to be aware of:
Consistency: Different libraries may have different syntax conventions
Memory: Uses more computer memory than some other languages
Speed: Some languages like Julia perform computations faster
Essential Python Packages You'll Use

You'll work with these packages:

Package	            Alias	    What You'll Use It For
numpy	            np	        Numerical computation and array operations
pandas	            pd	        Working with tabular and time-series data
scikit-learn	    sk	        Machine learning algorithms
matplotlib.pyplot	plt	        Creating data visualizations
seaborn	            sns	        Creating statistical visualizations with DataFrames
scipy.stats	        sp.stats	Statistical computing
statsmodels	        sm	        Estimating and analyzing statistical models

Pro tip: Different packages provide different functionality, so you'll use multiple packages in every project. For example, you might load data with pandas, run classification algorithms with scikit-learn, then visualize results with seaborn.

Part 4: Getting Started with Jupyter Notebooks
What is Jupyter?
Jupyter is your interactive development environment (IDE) for writing and testing data science code. You'll write code in Jupyter notebooks—interactive documents that organize code, text, and output all in one place.

Understanding Cells
Notebooks contain three types of cells:
Code cells: Where you write your Python code
Markdown cells: For text, explanations, and documentation
Raw cells: For output
Each cell can be run independently, making it easy to test and debug your code.

Using the Sample Notebooks

You can:
Modify them to test new parameter values
Try different modeling functions
Download them using "File" > "Download as" to save your progress
For installation instructions, visit the Jupyter installation guide.

Part 5: Working with NumPy
What is NumPy?
NumPy (pronounced "Num-pie") provides tools for mathematical computations in Python. You'll use it for:
Linear algebra operations
Fast Fourier transforms
Statistical calculations
Working with other packages like pandas and Matplotlib
Installation: Visit https://numpy.org/install/

Understanding NumPy Arrays
NumPy's core data structure is the ndarray (N-dimensional array)—similar to a list but with more mathematical support and faster performance.

Import NumPy like this:
"""
import numpy as np

"""
Array Dimensions
You'll work with arrays of different dimensions:
Zero-dimensional: A scalar object (e.g., 2)
One-dimensional: A container of scalars (e.g., [2, 4, 6, 8])
Two-dimensional: A container of containers with rows and columns (e.g., [[2, 4, 6, 8], [12, 14, 16, 18]])
N-dimensional: N levels of nested containers

Important concepts:
Shape: A tuple showing the lengths of each dimension (e.g., (2, 4))
Size: Total number of elements in the array (e.g., 8)

Creating Arrays
Create an array using the array() function:
"""

# Create a 1D array from a list
array1D = np.array([1, 2, 3, 4])

# Create a 2D array from nested lists
array2D = np.array([[1, 2], [3, 4]])

"""
Understanding Array Axes
Think of an axis as a direction along each array dimension:
1D arrays: 1 axis
2D arrays: 2 axes
Axis 0: Runs down the rows
Axis 1: Runs across the columns
Many NumPy functions take an axis argument to specify which direction to operate along.

Creating Placeholder Arrays
When you don't know the values yet, create placeholder arrays:
"""
# Create a (1, 3) array filled with zeros
zeros_array = np.zeros((1, 3))

# Create a (1, 3) array filled with ones
ones_array = np.ones((1, 3))

# Create a (2, 2) array filled with 6s
sixes_array = np.full((2, 2), 6)

"""
Essential Array Operations
Here are the key functions and methods you'll use:
Accessing Elements
"""
array2D = np.array([[1, 2], [3, 4]])

# Get element at row 1, column 0
elem = array2D[1, 0]  # Returns 3

"""
Deleting Rows or Columns
"""

# Delete the second row (index 1)
new_array = np.delete(array2D, 1, axis=0)  # Returns [1, 2]
"""
Sorting
"""
my_array = np.array([2, 4, 1, 3])

# Sort in place
my_array.sort()  # Now [1, 2, 3, 4]

"""
Reshaping
"""
# Flatten a 2D array to 1D
array_7 = np.array([[7, 7], [7, 7]])
array_flat = array_7.ravel()  # Returns [7, 7, 7, 7]

# Reshape a 1D array to 2D
array1D = np.array([1, 2, 3, 4])
array_reshaped = array1D.reshape((2, 2))  # Returns [[1, 2], [3, 4]]
"""
Transposing
"""
# Transpose an array
array_transposed = array_reshaped.transpose()  # Returns [[1, 3], [2, 4]]

"""
Mathematical Operations
Perform element-wise operations between arrays:

# Example: [5, 5, 5] + [1, 2, 3] = [6, 7, 8]

Common operations:
Operation	                        Description
array1 + array2	                    Element-wise addition
array1 - array2	                    Element-wise subtraction
array1 * array2	                    Element-wise multiplication
array1 / array2	                    Element-wise division
np.sqrt(array1)	                    Square root of elements
np.log(array1)	                    Logarithm of elements
np.sin(array1)	                    Sine of elements
np.max(array1)	                    Maximum element
np.median(array1)	                Median of elements
np.std(array1)	                    Standard deviation
np.var(array1)	                    Variance
np.dot(array1, array2)	            Dot product
np.matmul(array1, array2)	        Matrix multiplication
np.cross(array1, array2)	        Cross product

What is pandas?
pandas is your go-to Python package for storing and manipulating 2-dimensional datasets. Built on top of NumPy, pandas uses DataFrames to represent datasets in a table format.
Installation: Visit https://pandas.pydata.org/docs/getting_started/install.html
Import pandas like this:
"""

import pandas as pd

"""
Understanding DataFrames
A DataFrame organizes data into rows and columns:
Columns: Contain the features of your dataset (labeled with names)
Rows: Contain the instances (labeled with an index, usually integers)

Example: In a countries dataset:
Columns: "Name", "Continent", "Population"
Rows: 0, 1, 2, 3, 4 (representing five countries)

Key features:
All values in a column must have the same type
Different columns can have different types
Row labels (index) are usually auto-generated integers
Column labels are usually manually specified strings


DataFrame vs. NumPy Array

Similarities:
Both are indexed, ordered, and mutable containers
Both represent data in multiple dimensions
Both have a shape attribute

Differences:
DataFrames are always 2D; arrays can have any number of dimensions
DataFrame columns can have different types; arrays must have one type
DataFrame labels can be strings; array indices are integers only
Why use DataFrames? Since datasets typically have named features with different types, DataFrames are usually better than NumPy arrays for data science work.

Subsetting Data
Learn to select specific rows and columns from your DataFrame.
Selecting Columns
"""

# Select a single column (two ways)
country["Population"]
country.Population

# Select multiple columns
country[["Name", "Population"]]

"""
Selecting Elements and Ranges
Use iloc[] (integer location) and loc[] (label location):
"""
# Single element: row 0, column 1
country.iloc[0, 1]

# Multiple rows: rows 2 through 5
country[2:6]

# Range of elements: rows before 5, columns 1 and 2
country.iloc[:5, 1:3]

# Range using labels: rows 0 through 6, specific columns
country.loc[:6, ["Continent", "Population"]]
"""
Important: iloc[] excludes the end index, but loc[] includes it!

Subsetting with Comparison Operators
Filter rows based on conditions:
"""

# Show only countries with population > 100000
country[country["Population"] > 100000]

"""
Comparison operators: <, >, <=, >=, ==, !=

Logical operators for pandas:
Operator	Description	Example
&	AND     (both must be True)	(condition1) & (condition2)
|	OR      (at least one must be True)	(condition1) | (condition2)
~	NOT     (opposite truth value)	~(condition)

Essential DataFrame Methods
Here are the key methods you'll use to manipulate DataFrames:
Dropping Rows or Columns
"""

# Drop by label and axis
df.drop(labels="column_name", axis=1, inplace=False)

# Drop by index
df.drop(index=0, inplace=False)

# Drop by column name directly
df.drop(columns="column_name", inplace=False)

"""
Removing Duplicates
"""

# Remove duplicate rows based on specific column(s)
df.drop_duplicates(subset=["Name"], inplace=False)

# Use all columns if subset=None
df.drop_duplicates(inplace=False)

"""
Inserting Columns
"""

# Insert a new column at position 1
df.insert(1, "newcol", [99, 89])

"""
Replacing Values

"""
# Replace specified values with new values
df.replace(to_replace=old_value, value=new_value, inplace=False)

"""
Sorting
"""

# Sort by a specific column
df.sort_values(by="Population", ascending=True, inplace=False)

# Sort in descending order
df.sort_values(by="Population", ascending=False, inplace=False)
"""
Pro tip: Use inplace=True to modify the DataFrame directly, or inplace=False to create a new DataFrame with the changes.

Creating Visualizations with Matplotlib

What is Matplotlib?
Matplotlib is Python's most common data visualization package. You'll use it to create static, dynamic, and interactive plots that help you gain insights and communicate findings.

Why Matplotlib?
Versatility: Works in scripts, shells, iPython, and Jupyter Notebooks
Familiarity: Uses MATLAB-style functions
Portability: Runs on MacOS, Linux, and Windows
Customizability: Adjust every detail of your plots
Installation: Visit https://matplotlib.org/stable/users/installing/index.html

Getting Started with pyplot
Import the pyplot library with this standard alias:
"""
import matplotlib.pyplot as plt

"""
Creating Your First Plots
Line Plots
Connect consecutive points with lines:
"""

plt.plot(x, y)
#Note: x and y must be arrays of the same size.

"""
Scatter Plots
Show individual data points:
"""

plt.scatter(x, y)

"""
Essential Figure Functions
"""
# Create a new figure with specific size
plt.figure(figsize=[4, 5])

# Display the figure
plt.show()

# Save the figure to a file
plt.savefig("line_plot.png")

"""
Adding Labels and Titles
Make your plots informative with labels:
"""

# Add a title
plt.title("Alcohol-related fatalities on highways")

# Add axis labels
plt.xlabel("Year")
plt.ylabel("Number of fatalities")

"""
Adding Mathematical Expressions
You can include LaTeX-formatted mathematical expressions:
"""
# Add a title with mathematical notation
plt.title(r"Standard normal distribution $$f(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^2}$$")
#Use the letter r before the string and enclose expressions in dollar signs.
"""
Adding Text and Annotations
"""

# Add text at specific coordinates
plt.text(x, y, "Your text here")

# Add an annotation linking text to a point
plt.annotate("Your annotation", xy=(point_x, point_y), xytext=(text_x, text_y))

# Add a legend
plt.legend(loc="best")  # Options: "upper left", "lower right", "center", etc.

"""
Styling Your Plots
Customize colors, line styles, and markers:
"""

# Using shorthand characters
plt.plot(x, y, "ro")  # Red circles

# Using parameters
plt.plot(x, y, color="g", marker="X", linestyle="-.")  # Same as "gX-."

"""
Common style characters:
Colors: 'r' (red), 'g' (green), 'b' (blue), 'c' (cyan), 'm' (magenta), 'y' (yellow), 'k' (black), 'w' (white)
Line styles: '-' (solid), '--' (dashed), '-.' (dash-dot), ':' (dotted)
Markers: 'o' (circle), 's' (square), '^' (triangle), 'X' (X marker), '+' (plus), '*' (star)

Adding Grid Lines
Make it easier to read values from your plot:
"""

# Add grid lines to both axes
plt.grid()

# Add grid lines to x-axis only
plt.grid(axis="x")

# Customize grid line appearance
plt.grid(color="blue", linestyle="--", linewidth=5)

"""
Creating Multiple Subplots
Display multiple plots in one figure:
"""

# Create 2 rows, 1 column layout, place plot in row 1
plt.subplot(2, 1, 1)
plt.plot(x1, y1)

# Place second plot in row 2
plt.subplot(2, 1, 2)
plt.plot(x2, y2)

# Add a title for the entire figure
plt.suptitle("My Multiple Plots")

plt.show()
# Remember: The index parameter starts at 1, not 0!



# Practice with real datasets: Apply these techniques to actual data from sources like Kaggle, UCI Machine Learning Repository, or government open data portals
# Explore advanced topics: Dive deeper into machine learning algorithms, deep learning, and advanced statistical methods
# Build projects: Create end-to-end data science projects to solidify your skills
# Join the community: Participate in data science forums, competitions, and open-source projects
# Remember, data science is a hands-on field. The more you practice with real data, the more confident and skilled you'll become. Good luck on your data science journey!
