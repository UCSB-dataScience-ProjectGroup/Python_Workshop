# Adult Census Income Data Set
## Case Study for Python Workshop

**Problem**: 
Your team has been hired by a local hiring agency to make sense of a recent census (admittedly 1994 isn't recent, but just play along). They're trying to find the relationship between race and income within the United States, among other indicators taken during the census. They would like digestible visuals to include on their website relating to race, more specifically the difference between **Caucasian** and **African American** populations in the United States relating to the different indicators. 

**Process**: 
The hiring agency is only concerned with these variables:

+ age
+ workclass
+ fnlwgt
+ education
+ educationNum
+ marital
+ relationship
+ race
+ sex
+ capitalGain
+ capitalLoss
+ nativeCountry
+ hoursPerWeek
+ income

They would like your team to make sense of these variables but your team quickly realize that in order to do so some transformations must be made to ensure that your *data analysis* is sound. Some of the variables are **discrete variables** so they *must* be converted to their correct numerical representation. The hiring agency decides that **logistic regression** was the most appropriate method that they would want your analysis to be in.

Your team agrees and will go about this process converting the 'income' variable to a simple binary representation for your analysis i.e 1 is '<=50K' and 0 is ' >50K'. As well as converting other categorical variables to their numerical representation for **logistic regression**.  

Recall before you start your analysis, you want create visuals with respect to two subsections of your data set so it would be helpful to create two additional data frames: One relating to the *Caucasian* population in the *United States* and the other relating to the *African American* population in the *United States*. After doing so, create a *logistic regression* model relating to the newly converted data frame. 

**Important to Note**:
Just because I know its shitty to hard code conversions I've provided some of the longer variable conversions in `dict` format:

	{' Private':0, ' State-gov':1, ' Federal-gov':2, ' Self-emp-not-inc':3, ' Self-emp-inc':4, ' Local-gov':5, ' Without-pay':6}
	{' Widowed':0, ' Divorced':1, ' Separated':2, ' Never-married':3, ' Married-civ-spouse':4, ' Married-AF-spouse':4, ' Married-spouse-absent':5} 
	{ ' Doctorate':15, ' Masters':14, ' Bachelors':13, ' Some-college':12, ' Prof-school':11, ' Assoc-acdm':10, ' Assoc-voc':9, ' HS-grad':8, ' 12th':7, ' 11th':6, ' 10th':5, ' 9th':4, ' 7th-8th':3, ' 5th-6th':2, ' 1st-4th':1 , ' Preschool':0}


**Requirements:**
+ GitHub repository
	+ README including:
		+ Abstract (problem you are trying to solve and how you are going to do so)
		+ Contributors
		+ Raw file and newly converted file
		+ Explanation of Data Wrangling Process
		+ Explanation of Data Analysis Process
		+ Brief Overview of **Logistic Regression**
	+ Scripts
		+ Data Wrangling Process script (**NOTE**: Only if your data set requires data wrangling)
		+ Data Analysis Script
	+ Images folder and images for exploratory analysis
		+ Link to said images on the README file
	+ requirements.txt
+ Data Wrangling
	+ Convert categorical data to appropriate numerical representation
	+ Convert 'income' variable to appropriate binary representations.
	+ Output new file with appropriate conversions
+ Data Analysis
	+ At least *2* visuals showcasing features that distinguish sex of abalone the best
		+ Can be interactive (i.e. **plotly**, **bokeh** etc.) 
		+ Must be properly labeled: title and legend explaing sex (not just **M**, **F** and **I**, needs to directly state their actual sex)
	+ Quick summary of **Logistic Regression**
	 	+ Create appropriate **training** and **test** set, for this example use 80-20 split
		+ Give an overview of the method. Can include:
			+ Explanation of Algorithm  
			+ Visual representation of Algorithm
+ Conclusions
	+ Explain results within context of what you learned, and advice for people planning on learning *data analysis* with this data set or **Python**, as a whole.

**Resources**
+ [Adult Data Set Source](https://archive.ics.uci.edu/ml/datasets/Adult)
+ [Logistic Regression Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
+ [Simplified Logistic Regression Explanation](https://codesachin.wordpress.com/2015/08/16/logistic-regression-for-dummies/)
+ [Kaggle Page for Data Set](https://www.kaggle.com/uciml/adult-census-income)
