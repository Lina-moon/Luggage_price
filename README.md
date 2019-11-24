# Luggage_price
In order to opti find the optimal price for luggage overweight:

  1. Open input and change the values for you particular case. Don't forget to save.
  
    a. Current median of the price is very inaccurate evaluation of the price that is suggested currently. 
       Default value = 0.6342, which is 634.2 rubles for the kilogram.
       
    b. Parameter beta is the value of importance of the particular attribute that affect the price. 
       In the extended case should be found in a number not bigger than 10. Like b_1, b_2.... b_10.
       Due to the complexity of the problem. Sum of the coefficients beta tends to be 1, 
       however in this particular case should not be bigger than 0.8 for the price of 1 kilogram. 
       Default value = 0.7
       
    c. Parameter alpha normolizes the model. Several times bigger than current median in order to make exponent
       value strictly negative, but mostly because of the original function graph. 
       Default value = -6
       
    d. Number of the avarage overweight kilograms per person, overall on the flight during certain period of time.  
       Default = 0.1
       
    e. Market share or the number of customers furing certain period of time.
       Default = 10000
    
  2. Change the deviation of the cost at the 59th line of the .py file (strictly not equal to the
     cost itself). Change the sample space at the 58th line, as bigger the sample space as closer the culculations.
  
  3. Run the python file
