from cisc108 import assert_equal

def parse_date_month(month: str) -> int:
    
    '''
    This function takes in the date as a string and returns only the month
    value of that particular date.  
    
    Args:
        month (str): Takes in the whole date as a string, but since
                     the function focuses on the month, so the argument
                     is just called month. 
    Returns:
        int: The month value of the date. If the date doesn't have a vaild
        month, than a constant value (-1) is returned.
    '''
    
    splitted_month = month.split("/")
    month = splitted_month[0]
    if month.isdigit():
        month = int(month)
    else:
        return(-1)
    if month >= 1 and month <= 12: 
        return (month)
    else:
        return(-1)
    
assert_equal(parse_date_month("1/30/2015"), 1)
assert_equal(parse_date_month("14/3/2020"), -1)
assert_equal(parse_date_month("0/19/1989"), -1)
assert_equal(parse_date_month("12/23/2001"), 12)
assert_equal(parse_date_month("4/21/2003"), 4)



def parse_date_day(day: str) -> int:
    
    '''
    This function takes in the date as a string and returns only the day value
    of that particular date. 
    
    Args:
        day (str): Takes in the whole date as a string, but since
                   the function focuses on the day, so the argument
                   is just called day.
    Returns:
        int: The day value of the date. If the date doesn't have a valid day,
        than a constant value of (-1) is returned.
    '''
    
    splitted_day = day.split("/")
    day = splitted_day[1]
    if day.isdigit():
        day = int(day)
    else:
        return(-1)
    day = int(day)
    if day >= 1 and day <= 31:
        return(day)
    else:
        return(-1)
    
assert_equal(parse_date_day("1/31/2015"), 31)
assert_equal(parse_date_day("4/3/2020"), 3)
assert_equal(parse_date_day("12/35/1945"), -1)
assert_equal(parse_date_day("2/0/2014"), -1)
assert_equal(parse_date_day("11/11/2007"), 11)



def parse_date_year(year: str) -> int:
    
    '''
    This function takes in the date as a string and returns only the year value of that
    particular date. 
    
    Args:
        year (str): Takes in the whole date as a string, but since the function
                    focuses on the year, so the argument is called year.
    Returns:
        int: The four-digit year value of the date. If the date doesn't have a valid year,
        than a constant value of (-1) is returned. If the year is two-digits, than
        it is automatically considered to be in the 2000's and will return 4 digits. 
    '''
    
    splitted_year = year.split("/")
    year = splitted_year[2]
    if year.isdigit():
        length_year = len(year)
        year = int(year)
    else:
        return(-1)
    if length_year == 2:
        return(2000 + year)
    elif length_year == 3 or length_year == 1:
        return(-1)
    else:
        return(year)
    
assert_equal(parse_date_year("7/23/9"), -1)
assert_equal(parse_date_year("3/12/2005"), 2005)
assert_equal(parse_date_year("9/30/20"), 2020)
assert_equal(parse_date_year("6/22/16"), 2016)
assert_equal(parse_date_year("12/23/124"), -1)



def is_date(date: str) -> bool:
    
    '''
    This function takes in the date as a string, and using the other three functions (above)
    will return a boolean value depedning if a particular date is a valid date or not.
    
    Args:
        date (str): Takes in the whole date as a string type.
        
    Returns:
        bool: A valid date will return True, a not valid date will return False. 
    '''

    if parse_date_month(date) == -1 or parse_date_day(date) == -1 or parse_date_year(date) == -1:
        return(False)
    else:
        return(True)
    
    
assert_equal(is_date("12/25/2021"), True)
assert_equal(is_date("0/12/2007"), False)
assert_equal(is_date("3/45/2013"), False)
assert_equal(is_date("5/6/156"), False)
assert_equal(is_date("32/54/1"), False)
assert_equal(is_date("2/14/10"), True)



def earlier(first_date: str, second_date: str) -> str:
    
    '''
    This function takes in two different dates and returns the date which is the earliest
    out of the two dates. It uses the other helper function to check each part of the date
    to see which date comes first. 
    
    Args:
        first_date (str): Takes the first whole date as a string for comparison. 
        second_date (str): Takes the second whole date as a string for comparison.
        
    Returns:
        str: The earliest date is returned out of the two dates. Otherwise, if the two dates
        are the same than "equal" is returned, If either string is not valid than "error" is
        returned. 
    '''
    
    if is_date(first_date) and is_date(second_date):
        if parse_date_year(first_date) < parse_date_year(second_date):
            return(first_date)
        elif parse_date_year(first_date) > parse_date_year(second_date):
            return(second_date)
        else:
            if parse_date_month(first_date) < parse_date_month(second_date):
                return(first_date)
            elif parse_date_month(first_date) > parse_date_month(second_date):
                return(second_date)
            else:
                if parse_date_day(first_date) < parse_date_day(second_date):
                    return(first_date)
                elif parse_date_day(first_date) > parse_date_day(second_date):
                    return(second_date)
                else:
                    return("equal")
    else:
        return("error")

assert_equal(earlier("4/23/2005", "3/2/1989"), "3/2/1989")
assert_equal(earlier("15/31/2001", "7/12/2006"), "error")
assert_equal(earlier("11/45/2004", "3/8/123"), "error")
assert_equal(earlier("5/27/2009", "67/9/05"), "error")
assert_equal(earlier("3/2/2013", "3/2/2014"), "3/2/2013")
assert_equal(earlier("4/12/2019", "4/13/2019"), "4/12/2019")
assert_equal(earlier("2/5/2003", "1/5/2003"), "1/5/2003")
assert_equal(earlier("4/21/2003", "4/21/03"), "equal")
assert_equal(earlier("7/4/2021", "10/31/2021"), "7/4/2021")
