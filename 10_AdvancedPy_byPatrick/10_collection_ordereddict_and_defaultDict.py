#collections -->> OrderedDict and defaultdict

from collections import OrderedDict
from collections import defaultdict

ordered_dict = {}

ordered_dict['name'] = 'vasu'
ordered_dict['age'] = 19
ordered_dict['rollno'] = 3
ordered_dict['language'] = 'Py'

print(ordered_dict)


##### default dict jzt returns default value i.e 0 incase of error


default_dict = defaultdict(int)

default_dict['name'] = 'vasu'
default_dict['age'] = 19
default_dict['rollno'] = 3
default_dict['language'] = 'Py'

print(default_dict['agee']) 