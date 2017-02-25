# Wine Quality Data Set 
## Case Study for Python Workshop

**Problem**:

A Portuguese Winery is concerned with wine selections based on rating of red wine (*Vinho Verde* wine to be precise), so you are given the task of predicting the best wine quality given 11 physicochemical characteristics. 

**Process**: 

For this group you will have to connect to an *in-memory* database using the set of instructions I have provided. There will be more leniency for this group with respect to what analysis will be done, so you have to propose the problem you are trying to address as opposed to me giving you a pre-made problem. (although I do know of a process that can lead to 99% accuracy, but I will let you find that on your own)

There is inclusion of missing data, you will have to identify the amount, and convert to `np.nan` then remove these values before starting your data analysis. (**Hint**: Missing values are **not** positive numbers)

**Preliminary**:
For this case study your group must connect to a *in-memory database*, and use that connection to retrieve your data set, if there are more than one group who feel as though they are within this level of analysis then each team will be assigned a certain type of wine. 

More advanced group will be assigned the white wine subcategory. The other group will do the red wine subcategory. 

**Requirements:**
+ GitHub repository
	+ README including:
		+ Abstract (problem you are trying to solve and how you are going to do so)
		+ Contributors
		+ Raw file and newly converted file
		+ Explanation of Data Wrangling Process
		+ Explanation of Data Analysis Process
		+ Brief Overview of **Random Forest**
	+ Scripts
		+ Data Wrangling Process script (Extracting the data from the database, based on the specific parameters given to your team)
		+ Data Analysis Script 
	+ Images folder and images for exploratory analysis
		+ Link to said images on the README file
	+ requirements.txt
+ Data Wrangling
	+ Concise comments and documentation for the data wrangling aspect of your project
	+ Inclusion of pre-processed data file 
	+ Inclusion of new file with appropriate conversions
+ Data Analysis
	+ Brief justification for your process 
	+ Quick summary of **Random Forest**
	 	+ Create appropriate **training** and **test** set, for this example use 80-20 split
		+ Give an overview of the method. Can include:
			+ Explanation of Algorithm  
			+ Visual representation of Algorithm
			+ Finding the best iteration of **Random Forest** algorithm
	+ Conclusions
		+ Explain results within context of 

**Resources**
+ [Wine Quality Data Set](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)
