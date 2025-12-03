from solution.iprecord import IPRecord
from solution.service import Service

x = Service("8.8.8.8","google","dns", 53)
print(x.info())
y = Service("4.4.4.4", "att", "dns", 53)
print(y.info())