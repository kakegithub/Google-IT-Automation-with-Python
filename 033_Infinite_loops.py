###################################################
while x % 2 == 0:
    x = x / 2
# No output
####################################################
if x != 0:
    while x % 2 == 0:
        x = x / 2
# No output
######################################################
while x != 0 and x % 2 == 0:
    x = x / 2
# No output
#######################################################
while True:
    do_something_cool()
    if user_requested_to_stop():
        break
# This code will give an error because do_something_cool is not defined
#########################################################
