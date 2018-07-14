# Trinity 2.0
Project Trinity 2.0 is an extension of the first Trinity project.
<br>
In the first Trinity project the researchers tried to establish what is the safe withdrawal rate (SWR) from a given portfolio, considering past S&P500 performance. 
<br>
As a conclusion the researchers established that the SWR is 4% in 96% of the time periods that were tested.
<br>
Each time period tested was 30 years.  

# So why reproducing their research?
The aim of this project is to extend the results of the Trinity project.
<br>
Using this repository, anyone can input the length of time periods that are relevant for him.
<br>
In a world where more people aspire to retire as soon as possible, it is important to examine the S&P500 results over longer periods (40+).
<br>
Also, the withdrawal percentage is configurable so tests can be performed on varying percentage.

# Usage Example:
After setting the right configuration in configuration.py, all that is needed is:
<br>

```python
trinity = Trinity2()
trinity.calculate()
```