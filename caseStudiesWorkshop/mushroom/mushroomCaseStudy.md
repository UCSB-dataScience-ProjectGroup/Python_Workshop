# Mushroom Data Set
## Case Study for Python Workshop

**Problem**: 

A scientific researcher spent quite a bit of time collecting data for mushrooms. They were concerned about the accuracy of predictions based on *Naive Bayes* classification to see whether or not a mushroom was edible based on different physical characteristics. So your team was called to do a analysis on this data set provided by the researcher. The scientific researcher wants your team to include the *ROC Curve* and the *AUC* value within your *analysis* since this will be useful for their understanding. 

**Process**: 

Your team quickly realized that this data set is all *discrete variables*, so conversion to what are called *dummy variables* are necessary. Utilizing the `get_dummies()` function (More on this later) in pandas will be useful in your analysis. 

After doing so, your team decided since there was a conversion of variables types, you would use *Naive Bayes* to try to see which variables showed the most significance in the model created.

The prediction aspect is as follows: a requirement for this data set was that the reseacher wanted a 65-35 split with respect to the *training* and *test set*. Again provide the following pieces of information in your analysis:
+ Training and test sets' *false positive* totals
+ Explanation of the process of converting *discrete variables* to *dummy variables* 
+ ROC curve for your *test set*
+ Any prediction measurements that would be helpful in understanding model predictions and outcomes

**IMPORTANT TO NOTE**: 

For this data set since all dependent variables are *discrete* you will need to employ the `pandas.get_dummies()` function. Fair warning this will produce a fairly large dataframe. An important feature in the `pd.get_dummies()` is the use of `prefix = []`, which will be helpful in distinguishing columns when the conversion is made.  

As well as choosing the appropriate *Naive Bayes* method from the `sklearn` module. 

**Requirements:**
+ GitHub repository
	+ README including:
		+ Abstract (problem you are trying to solve and how you are going to do so)
		+ Contributors
		+ Raw file and newly converted file
		+ Explanation of Data Wrangling Process
		+ Explanation of Data Analysis Process
		+ Brief Overview of **Naive Bayes**
	+ Scripts
		+ Data Analysis Script 
	+ Images folder and images for exploratory analysis
		+ Link to said images on the README file
	+ requirements.txt
+ Data Wrangling
	+ Convert all variables to appropriate numerical **dummy variable** 
	+ Output new file with appropriate conversions
+ Data Analysis
	+ Documentation regarding the conversion of the *discrete variables*
	+ file containing data both pre and post processing
	+ Quick summary of **Naive Bayes**
	 	+ Create appropriate **training** and **test** set, for this example use 70-30 split
		+ Give an overview of the method. Can include:
			+ Explanation of Algorithm  
			+ Visual representation of Algorithm
+ Conclusions
	+ Include *ROC Curve* and *AUC* Calculated 
	+ Explain results within context of your analysis, what you learned, and advice for people planning on learning *data analysis* with this data set, **Python**, as a whole. 
	+ As well as explaining the results within context of the data set, was this algorithm useful in the amount of predicted edible that were actually poisonous

**Resources**
+ [Mushroom Data Set Source](https://archive.ics.uci.edu/ml/datasets/Mushroom)
+ [Simplified Explanation of Naive Bayes](http://blog.aylien.com/naive-bayes-for-dummies-a-simple-explanation/)
+ [Sklean Documentation](http://scikit-learn.org/stable/modules/naive_bayes.html)
+ [Pandas get_dummies() Documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html)
+ [Kaggle Page for Data Set](https://www.kaggle.com/uciml/mushroom-classification)
