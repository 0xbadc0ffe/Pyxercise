# Pyxercise

Python exercises with increasing level.

## Setup

First of all, download [python3](https://www.python.org/downloads/). 
- If your are on Debian you could also use the following commands in your bash:


       sudo apt update 
       sudo apt install python3




## First Exercise

To generate the first exercise use:

    python3 test.py -start
    
## Next Exercise

To generate the next exercises the syntax is the following:
For the exercise n+1 

    python3 test.py -n "solution"
    
where solution is the solution of the exercise n


**Example**:
- I resolved the exercise 2, with solution "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55"

    python3 test.py -2 "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55"
    
In this way, if the solution is correct and there exists a 3rd exercise, it will be generated.


## License
[MIT](https://choosealicense.com/licenses/mit/)
