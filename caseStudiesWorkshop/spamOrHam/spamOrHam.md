# Spam or Ham Data Set
## Case Study for Python Workshop

**Problem**:
To put it bluntly getting spam in your email is crappy. Fortunately many email providers have been able to classify spam (or ham) appropriately, but some of you witnessed when my email regarding the **Python** workshop was marked as spam, its not perfect.

This is a good segue to this case study, your team is given the task of classifying email, but the company that has given you this task stresses the importance of having minimal *false positives* as possible (good mail marked as spam). So your group decides to use *decision trees*. And to drive home the significance of *false positives* within your model. The company wants your team to provide an *ROC Curve* and *AUC* value in your analysis. 

As well as stating the amount of *false positives* for both your *training* and *test set*. To help the people you are working for understand how we go about interpretting and receiving these numbers in our analysis.

**Process**: 
Pretty straight forward, the only requirement for this data set was that the client wanted a 75-25 split with respect to the *training* and *test set*. Again provide the following pieces of information in your analysis:
+ Visual Representation of the decision tree created
+ Training and test sets' *false positive* totals
+ Detailing the Variable Importances using *Gini Importance* (Read the documentation if you are unsure of this step) 
+ ROC curve for your *test set*
+ Any prediction measurements that would be helpful in understanding model predictions and outcomes

**Requirements:**
+ GitHub repository
	+ README including:
		+ Abstract (problem you are trying to solve and how you are going to do so)
		+ Contributors
		+ Explanation of Data Wrangling Process
		+ Explanation of Data Analysis Process
		+ Brief Overview of **Decision Trees**
	+ Scripts
		+ Data Wrangling Process script (**NOTE**: Only if your data set requires data wrangling)
		+ Data Analysis Script
	+ Images folder and images for exploratory analysis
		+ Link to said images on the README file
	+ requirements.txt
+ Data Wrangling
	
+ Data Analysis
	+ Visual Representation of the decision tree created
	+ Training and test sets' *false positive* totals
	+ Detailing the Variable Importances using *Gini Importance* (Read the documentation if you are unsure of this step) 
	+ ROC curve for your *test set*
	+ Any prediction measurements that would be helpful in understanding model predictions and outcomes
+ Conclusions
	+ Explain results within context of what you learned, and advice for people planning on learning *data analysis* with this data set or **Python**, as a whole.

**Resources**
+ [Spambase Data Set Source](https://archive.ics.uci.edu/ml/datasets/Spambase)
+ [sklearn Decision Trees Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
+ [Paper explaining Decision Trees](https://www-users.cs.umn.edu/~kumar/dmbook/ch4.pdf)