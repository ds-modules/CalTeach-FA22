# Avocado Analysis

## Inspiration

- [Curriculum Idea](https://www.jmp.com/en_us/statistics-knowledge-portal/t-test/two-sample-t-test.html)

- Objective: Students will be able to understand, perform, and analyze results of a t-test using data that they have collected. 

- Idea should be similar to the [Gecko Physics Example](https://datahub.berkeley.edu/user/ailynnguyen/notebooks/IB-C32/Final/Gecko_Inspired_Adhesive_Analysis.ipynb)

- Target Audience: High school (AP) statistic students (need to try to make language engaging, maybe add visual elements?)



## Introduction

Avocados. From guacamole to morning toast, avocados have risen in popularity immensely. They are used in salads and salsas, spring rolls and sandwiches–they are even snuck into chocolatey brownies! But of course, if more and more people want a product, what do you think will happen to the price?

Let’s make a hypothesis of what you expect the price of avocados to look like overtime if more and more people continue to want them? In your hypothesis, include your

Claim: “Avocado prices will rise/drop/stay the same/etc.”

Explanation: “because….”

Type below:

<center><code>Insert Cell here</code></center>


# t-Test

How can we look at changes overtime? Well, luckily the Hass Avocado Board has an extensive national dataset of avocado prices (and more!) from 2015 and onwards.

Let’s take a look at a random sample of the avocado prices in 2019 and 2022 from California:
> [FOR JONATHAN: here is a link for the dataset from 2019 and here is the link for the dataset from 2022 you may need to scroll down until you find the “Totals by PLU” box and download the csv that says “Download 2019/22 Weekly Retail Volume and Price Report”; I had to make an account to access this, but it is free and takes a couple of seconds! I’m not sure how to access this data and get a random sample of about 50 prices from each data set, so let’s talk further about that! Ideally, the random sample should be formatted in a graph that shows some sort of distribution (like scatter plot or bar graph!) I’m not sure of the extent for Jupyter graphs/visuals, but if it could have the option to display the 2019 graph only, 2022 graph only, and both at the same time, that would be awesome here!]

What are some observations (trend, mean/median, variability/range, outliers, significant data points, etc.) you have about the data in 2019? 




What are some observations (trend, mean/median, variability/range, outliers, significant data points, etc.) you have about the data in 2022? 




What specific value(s) in each data set should we use to determine if there was a change overtime?




Looking at the dataset, what would you hypothesize? Do you think there is a change in price between the two years? In which direction? How confident are you and why? 




In most cases, when we look at two different data sets to compare, there may be some overlapping points. For example, even though the overall graph shows the price of avocados in 2022 being greater than the price of avocados in 2019, we still see some points in the 2022 graph that are less than points of the 2019 graph. If there is a lot of overlap, looking at a visual or single calculated value may not be enough!

In this case, it may be best to use a two sample t-test. A two sample t-test is a statistical test that can help us compare the means, or average, of the two dataset. T-tests have a specific criteria that the data must abide by to work:

The data has to be:
independent (the data do not affect each other)
randomly selected sample
large (sample size recommended to be over 30, otherwise, it MUST be normally distributed)
but not too large (sample size is at MOST 10% of the total population)

Keep in note, we are using samples of the entire population. That is why we can use a t-test! Otherwise we would use a different test. In most cases, you will not be able to collect data about an entire population, so t-tests are incredibly useful here!

Remember our question is: Did the price of avocados increase from 2019 to 2022?

The first t-test step is to create our null hypothesis (H0) and alternative hypothesis (Ha). A null hypothesis is our assumption that says there is no difference between the two means. Typically, the format would follow μa = μb, where a and b are your identifying titles to separate the two samples. The alternative hypothesis is what we want to test. Typically, the format would follow μa < μb, μa > μb, or μa ≠ μb.

Write down what you think the null hypothesis and alternative hypothesis would be using the variables μ2019 and μ2022: 
H0: 
Ha:

Let’s check if your hypotheses are correct! 
H0: μ2019 = μ2022
Ha: μ2019 < μ2022  (note: μ2022 > μ2019 would also be correct! The process to solve this is the same, but let’s follow using the first inequality.)

At the end, we will receive a p-value. That p-value is compared to the probability “limit,” helping us determine if we are able to reject our null hypothesis. The “limit” is called the significance level, denoted as α. Typically, α is set to 0.05, but it can vary depending on the field of study. Essentially, α = 0.05 just means there is a 5% risk that we reject the null hypothesis (or conclude that there is a significant change) even though there is actually no difference between the means (null is actually true!). So in the context of avocados, if we have a p-value that is lower than α = 0.05, we can assert with 95% confidence that the prices of avocados from 2019 and 2022 are not the same. That is, there is a 5% chance that the prices are the same, even though our calculations state otherwise. For this problem, let’s set our α = 0.05. 

There are two ways to perform a t-test with this data: with a calculator function and without a calculator function. Let’s look at without first:
 
t-Test without using direct calculator function

We start by finding the means, standard deviations, and the count of each data sample. 

We can find the mean by adding up each of the values and dividing the sum by the count. 
mean = sum of the termsnumber of terms

Standard deviation for a sample is the square root of the sum of the square of each term subtracted by the mean divided by the number of terms minus one. A mouthful! Let’s look at the formula to understand this better:
s = (x - x)2n-1, where x is the value, x is the mean, and n is the count

The count is simply the number of data points you have in the sample.

All of these values can be determined manually through a calculator, or you can use the 2-Var Stats function under [STAT] on a TI-84.

To use a TI-84:
Press [STAT].
Press [ENTER] or [1] to get into Edit…
Input your data into the lists. Each list should correspond to a sample.
Press [STAT] again.
Scroll over to CALC and hit [2] or select 2-Var Stats.
Set Xlist as one of your filled lists. Set Ylist as your other filled list. You can change the list by hitting [2ND][LIST] and scrolling down on NAMES to select your desired list.
Leave FreqList empty. 
Hit Calculate
You specifically want to record x, Sx, y, Sy, and n. Note that if the two samples are different sizes, then you can do two 1-Var Stats tests for each sample. Make sure to note nx and ny.

Let the x-variables represent the data sample from 2019 (. Let the y-variables represent the data sample from 2022. 

What did you get for each of the values?
x2019:
S2019:
x2022:
S2022:
n:

Let’s check your work! [FOR JONATHAN: Because the random sample is going to be determined later, I can fill in these samples, or we can maybe develop a formula that automatically fills these in?]
x2019: 
s2019:
x2022:
s2022:
n:


Great job finding the main data statistics! Let’s use this information to help us form a t-test now!
The general formula to find the t-statistic is:
t=xa -  xbsa2na - sb2nb

In this case, we can rewrite the formula in terms of our own variables:
t=x2019 -  x2022s20192- s20222n

Go ahead and plug in the values to see what you get:
t =

Let’s check our work again. 
t = [CALCULATED ANSWER]

We are almost there! Now we have to find the probability of the t-distribution of becoming more extreme than the t-statistic. Let’s visualize this! [IS IT POSSIBLE TO DRAW NORMAL CURVES ON JUPYTER NOTEBOOK? THESE VISUALS ARE NOT THE BEST!]

This is a standard normal curve. The mean is at the middle line where x=0. Let’s now try to graph where a generic t-statistic would land from both ends of the mean–let’s say t-statistic = 1. 

When we deal with finding the probability, we actually want to look at the tail(s) of the graph, so focus on the white areas instead of the green!


If we want to find the probability that: 
μa < μb: Find the probability of the left tail end.
μa > μb: Find the probability of the right tail end.
μa ≠ μb: Find the probability of the left tail end and the right tail end (double the value).

Describe what portion of the normal curve you are wanting to find the probability of for our avocado problem! Make sure to include the t-statistic by drawing a rough sketch.




The normal graph should look something like:

And you want to find the probability of the white portion! [NEED TO ADJUST TO MATCH THE CALCULATED T-STATISTIC]

So how do we find the probability? We can use a test in our calculators called tcdf!

To find the probability:
Press [2ND][DISTR]
Press [6] or scroll to tdcf(
Enter your lower bound (if your lower bound is the end of the curve, put -1E99; to enter E, press [2ND][EE])
Enter your upper bound (if your upper bound is the end of the curve, put 1E99; to enter E, press [2ND][EE])
Enter the smallest sample size minus 1 as the df. 
Hit Paste

Determine the probability for our avocado data:
tcdf( ____, _____, _____) = ______

Check your work!
tcdf(-1E99, [T-STAT], 49) = [ANS]

Great! We got our numbers and now it is time to interpret the data! Remember that significance level we talked about before? We are going to compare our probability, commonly known as p-value, to α. There are two outcomes:
p-value < α
This is great! We can reject the null hypothesis and suggest the alternative hypothesis. 
“Since the p-value of [p-value] is less than 0.05, we can reject the null hypothesis of no difference in favor of the alternative and conclude that, on average, [describe Ha in words]. ”
p-value > α
Here, we cannot reject the null hypothesis! Note that we DO NOT accept the null hypothesis, it just means we cannot make a firm conclusion.
“Because the p-value of [p-value] is larger than 0.05, we fail to reject the null hypothesis. There is not convincing evidence that [describe Ha in words].”

With our p-value, analyze your results by comparing it to α = 0.05. 




Check your work!
[TWO ANSWERS:
p-value < α
“Since the p-value of [p-value] is less than 0.05, we can reject the null hypothesis of no difference in favor of the alternative and conclude that, on average, the price of avocados in 2019 is less than the price of avocados in 2022. ”
p-value > α
Here, we cannot reject the null hypothesis! Note that we DO NOT accept the null hypothesis, it just means we cannot make a firm conclusion.
“Because the p-value of [p-value] is larger than 0.05, we fail to reject the null hypothesis. There is not convincing evidence that the price of avocados in 2019 is less than the price of avocados in 2022.”
]

And that’s how you perform a t-test!  

## Survey

This survey is all anonymous. You are not required to answer any questions, but responses are highly encouraged! These answers will be used to study curriculum and how to improve (online) lessons.

- Grade:
- Have you taken or are you currently taking a statistics course: Yes No
- What did you like about this lesson:
- What did you not like about this lesson (What would you like changed?):
- On a scale of 1-10, how effective was the lesson (How much information did you retain):
- On a scale of 1-10, how likely are you to recommend this lesson to others:
