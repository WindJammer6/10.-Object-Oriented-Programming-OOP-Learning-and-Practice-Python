#This is an example of how Python's datetime module could have been created using Class Methods from
#Python's time module

import time

class datetime:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    #Construct a date from a POSIX timestamp (like time.time())
    @classmethod
    def from_time_stamp(cls, t):
        year, month, day, hh, mm, ss, weekday, jday, dst = time.localtime(t)
        return cls(year, month, day)
    
    #Construct a date from time.time()
    #It makes use of the 'from_time_stamp(cls, t)' Class Method above to create the 'datetime' object
    #in the form of just the year, month and time only instead of having the hours, mins, seconds that
    #the '.time()' function in the time library returns
    @classmethod
    def today(cls):
        t = time.time()
        return cls.from_time_stamp(t)
    
    #Construct a date from a proleptic Gregorian ordinal.
    #e.g. 'January 1 of year 1 is day 1.' Only the year, month and day are non-zero in this result.
    #   @classmethod
    #   def from_ordinal(cls, n):

    #(p.s. I lazy to get this one to work)

print(time.localtime())
print(time.time())                         #'time.time()' returns the number of seconds, t since epoch
                                           #(Note that the 'epoch' is defined as the start of January 
                                           #1st, 1970 in UTC)
current_date = datetime.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)
