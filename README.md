# Price Analyser

Purpose - To determine if particular patterns in price would form the basis of a profitable trading strategy, based on GBPUSD csv data.

## Strategy 1
Pick out structural high and low points from price, if price returns to these, determine if placing a trade at these structural points of support or resistance would result in a profitable trade. 

## Strategy 1 Execution in Code
- Iterate through rows of price data to find lowest price point. 
- Determine if 