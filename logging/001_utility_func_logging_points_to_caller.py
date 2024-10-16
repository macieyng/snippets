import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
# see https://docs.python.org/3/library/logging.html#logrecord-attributes
handler.setFormatter(
    logging.Formatter(
        'In file %(pathname)s line: %(lineno)s func: %(funcName)s %(levelname)s - %(message)s'
    )
)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def utility_function_1(x):
    if x == 0:
        logger.info('This is a zero')


def utility_function_2(x):
    if x == 0:
        logger.info('This is a zero', stacklevel=2)
    
    
def important_function():
    divisor = 0
    dividend = 10
    utility_function_1(divisor)
    utility_function_2(divisor)
    try:
        return dividend / divisor
    except ZeroDivisionError:
        logger.warning("Division by zero")
    return 0


def main():
    logger.info('Main function is called')
    important_function()
    

if __name__ == '__main__':
    main()
    
"""
Output:
In file ~/001_utility_func_logging_points_to_caller.py line: 39 func: main INFO - Main function is called
In file ~/001_utility_func_logging_points_to_caller.py line: 15 func: utility_function_1 INFO - This is a zero
In file ~/001_utility_func_logging_points_to_caller.py line: 30 func: important_function INFO - This is a zero
In file ~/001_utility_func_logging_points_to_caller.py line: 34 func: important_function WARNING - Division by zero

First one is the default behavior. Useful for unique and/or important logic like in `important_function` or main processess like in `main`.

The second one points to where the logger is called. There is no benefit, because if the function is called by another function, it will point to place where logger is called, not where the function is called.

The third one provides the most useful information. It points to the place where the function is called. This is useful for debugging and understanding the flow of the program.

The fourth one is a warning message. It is useful to know that the function is called and the division by zero is caught.

"""
