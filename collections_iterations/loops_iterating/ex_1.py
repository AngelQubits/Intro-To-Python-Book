# The loop body does not have an update statement that terminates the 
# condition.

counter = 0

while counter < 5:
    print(counter)
    counter += 1  #lacks this update statement