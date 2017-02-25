# Abalone Data Set
## Case Study for Python Workshop

**Problem**: 

A marine biologist from **Marine Research Laboratories** decided to reach out to your team because they need helping making sense of the data they collected. The underlying issue is that they are trying to predict the age of the **abalone** based on the physical attributes they collected during their study. 

**Process**:

Some preliminary requirements that they asked from your team is to show them exploratory analysis with respect to the sex of the **abalone**, a nominal value of {**M**: Male, **F**: Female, and **I**: Infant}. They were curious as to which physical attributes (i.e. dependent variables) showed the most distinction between the sexes. They asked that you do at least two visuals that will help them digest some of the information that your team found during your analysis.     

Your team quickly realized that the process best suited for this dataset is **linear regression** since the independent variable is *continous* ('rings'), but after some persuasion your team convinced the marine biologist that a more efficient process would be to do classification. So your team decided to create 3 appropriate bins for the 'rings': (Inspired by: citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.14.2321&rep=rep1&type=pdf)

| Rings |  Age  | 
|-------|-------|
| 0-8   | Young |
| 9-14  | Adult | 
| 15-29 |  Old  | 

After doing so, your team decided that **Kth Nearest Neighbor** would be the best approach for this analysis. Your team also decided that instead of doing the traditional *training* and *test* split you feel as though *cross validation* would be a more appropriate method. As well as showcasing the results of **3 different k values** for your algorithm.  

**IMPORTANT TO NOTE**: 

For this data set, the use of the **original** data set is encouraged for the **exploratory analysis**, since when going about **exploratory analysis** we are usually concerned with the original forms of measurement, whereas the *data analysis* part we are concerned with the *normalized* data set (since this helps with accuracy when applying our **machine learning algorithms**). Also after concluded your results 

**Requirements:**
+ GitHub repository
	+ README including:
		+ Abstract (problem you are trying to solve and how you are going to do so)
		+ Contributors
		+ Raw file and newly converted file
		+ Explanation of Data Wrangling Process
		+ Explanation of Data Analysis Process
		+ Brief Overview of **Kth Nearest Neighbor**
	+ Scripts
		+ Data Wrangling Process script
		+ Data Analysis Script
	+ Images folder and images for exploratory analysis
		+ Link to said images on the README file
	+ requirements.txt
+ Data Wrangling
	+ Convert **Male**, **Female** and **Infant** to appropriate numerical **dummy variable**
	+ Normalize Predictor Variables
	+ Convert 'rings' variable from *continous* to *categorical* (Must also be **dummy variable**, see table mentioned above)
	+ Output new file with appropriate conversions
+ Data Analysis
	+ At least *2* visuals showcasing features that distinguish sex of abalone the best
		+ Can be interactive (i.e. **plotly**, **bokeh** etc.) 
		+ Must be properly labeled: title and legend explaing sex (not just **M**, **F** and **I**, needs to directly state their actual sex)
	+ Quick summary of **Kth Nearest Neighbor**
	 	+ Create appropriate **training** and **test** set, for this example use 80-20 split
		+ Give an overview of the method. Can include:
			+ Explanation of Algorithm  
			+ Visual representation of Algorithm
			+ Finding the best **K** for your analysis
+ Conclusions
	+ Explain results within context of what you learned, and advice for people planning on learning *data analysis* with this data set or **Python**, as a whole.


**Resources**
+ [Abalone Data Set Source](https://archive.ics.uci.edu/ml/datasets/Abalone)
+ [Introduction to k-nearest neighbors : Simplified](https://www.analyticsvidhya.com/blog/2014/10/introduction-k-neighbours-algorithm-clustering/)
+ [KNeighborsClassifier Python Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier)
+ [Inertia7 K-NN Project on Iris Data set](http://www.inertia7.com/projects/iris-classification-r)
+ [Paper citing Data Set](citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.14.2321&rep=rep1&type=pdf)
