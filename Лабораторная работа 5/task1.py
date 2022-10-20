# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
def f_list(num):

    lis_dict = [dict([('bin', bin(i)),('dec',i),('hex', hex(i)),('oct', oct(i))]) for i in range(num+1)]
    return(lis_dict)

pprint(f_list(15))
