import psutil

# cpu - if we put logical to false all the physicall cpu will be shown
print(psutil.cpu_count(logical=False))
# if we didn't include the time interval of it the number shown is 0.0 but we have to specify in what period of time cpu will be using 
print(psutil.cpu_percent(interval=1))
# details of cpu frequency:
print(psutil.cpu_freq())
 