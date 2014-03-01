 
import cgi

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
  if month:
    cap_month = month.capitalize()
    if cap_month in months:
      return cap_month
    
    return None


def valid_day(day):
  try:
    if day:
        ret = int(day)
        if ret in range(1,31):
          return ret
  except ValueError:
    return None


def valid_year(year):
  if year and year.isdigit():
    ret = int (year)
    if ret in range(1900,2014):
      return ret


# def escape_html(s):
#     if s == '<':
#         return "&lt;"
    
#     if s == '>':
#         return "&gt;"
    
#     if s == '"':
#         return "&quote;"
    
#     if s == '&':
#         return "&amp;"

def escape_html(s):
  return cgi.escape(s, quote=True)

x = 20
y = 1
def variable_scope(x):
    y = 2
    print 'x %s' % str(x)
    print 'y %s' % str(y)

    z = 'a'
    if z == 'a':
        print 'z %s' % z
        z = ''
        print 'z %s' %z
        if 1:
            z = 'c'
            print 'z %s' %z

        print 'z %s' %z



# variable_scope(10)
# print 'y %s' %y