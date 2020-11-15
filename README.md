# columbus-wildlife-workshop

Hello! In this workshop, we will be introducing you to the process of gathering your own data for machine learning applications, and understanding how you can refine your queries/search terms to protect for underlying biases (e.g multilingual queries) and maximize the amount of results you get back.

As an undergraduate researcher, you can begin laying the foundation for a successful path in research by being mindful of potential biases, and what you can do to correct for them. 

## Query Terms ##
In this workshop, we will be working with wildlife species native to Ohio, and analyzing the results we retrieve from Flickr. As you will notice, not all results retrieved with a general search will include species native to Ohio - some may look a bit more exotic than others. That's ok! Think about what you can do to filter out these less relevant results and refine your query to generate a higher volume of true Ohio-native wildlife species. 

Query term to start out with: https://www.flickr.com/search/?text=Columbus%20AND%20ohio%20AND%20wildlife

## Classification ##
Now that we've figured out how to maximize our true Ohio wildlife results, let's see how well our data performs with machine learning classification.
We'll use our results with Microsoft's Azure API for species classification and observe our results. 

You can access the Microsoft Azure API here, and read more on what it does and how it works: https://github.com/Microsoft/speciesclassification

If you get a result that you were not expecting, generate insights on how we can improve the accuracy of classification and discuss different approaches that can be taken to avoid misclassification. Oftentimes, our model will perform as well as the data we feed it is representative of what we want to classify. Consider what steps can be taken in the earlier stage of gathering data and building your datasets that may help your machine learning pipeline generate better results.
