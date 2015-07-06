import sys
import datetime
import calendar

def create_calendar_page(month = None,year = None):
     import datetime
     import calendar

     today = datetime.datetime.today()
     if month == None: month = today.month
     if year == None: year = today.year
     day = datetime.datetime (year, month, 1)
     weekday = day.weekday()
     max_days = calendar.monthrange(year, month)
     line = ""
     for i in range(20):
         line += "-"
     line += "\nMO TU WE TH FR SA SU\n"
     for i in range(20):
         line += "-"
     line += "\n"
     line += '   '*weekday + '01'
     for i in range (max_days[1]+1)[2:]:
         day = datetime.datetime (year, month, i)
         if i < 10 and day.weekday() == 0:
             line += '\n' + '0' + str(i)
         elif i < 10 and day.weekday() != 0:
             line += ' ' + '0' + str(i)
         elif i >= 10 and day.weekday() == 0:
             line += '\n' + str(i)
         elif i >= 10 and day.weekday() != 0:
             line += ' ' + str(i)
     return line

print create_calendar_page(1)
print create_calendar_page()
print create_calendar_page(2, 2016)
print create_calendar_page(3)
print create_calendar_page(04, 1992)
