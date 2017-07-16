months = ['jan' , 'feb' , 'mar' , 'apr' ]
months.append ('may')
months.append ('july')
print 'adding may and july:' , months
months.insert (5 , 'jun')
print 'current list is:' , months
print 'index of may is: ' , months.index ('may')
months.remove ('jun')
print 'remove june list is' , months
months.sort()
print 'sort list is' ,months
months.reverse()
print 'reverse list is' , months


