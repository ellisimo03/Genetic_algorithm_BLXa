CS3CI Experimental Study – Evolutionary (Genetic) Algorithm while also Implementing a 
Blend Crossover (BLX-α Crossover) 
By Ellis Rogers Loredo – 220184634 
Aston University 
Computer Science 
Computational Intelligence (CS3CI) 
December 2025 
Introduction 
The work I am presenting here is part of the module ‘Computational Intelligence’ (CI). 
The task is to predict the daily demand of a logistics company based on their 13 demand 
indicators collected at midday. The prediction model uses 14 parameters, one being a 
bias term and thirteen being weights, and the aim is to optimise these parameters by 
f
inding the best values while minimising prediction error. The company needs to know 
how many trucks to allocate via a prediction made at midday. A bad prediction can cost 
the company money in different ways depending on if there was an underestimation, 
leading to a lack of trucks necessary to complete the day’s work, or an overestimation, 
which can lead to a higher impact on the environment and can also generate 
unnecessary costs. To avoid all this, a strong prediction for the days forecast will 
ultimately bring about operational efficiency in costs, satisfied customers and less 
environmental strain. 
To tackle this optimisation problem, I will use a Genetic Algorithm (GA) consisting of a 
population based global search method. My novel variant aspect of this task will be 
implementing a ‘Blend Crossover’ which will encourage a range of different offspring 
produced and reduce the likelihood of the GA prematurely converging due to population 
lacking in diversity.
