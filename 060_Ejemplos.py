########################################################################

numbers = [4, 6, 2, 7, 1]
numbers.sort()
print(numbers)

########################################################################

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(sorted(names))
print(names)
print(sorted(names, key=len))

##########################################################################


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines


###################################################################################


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


##################################################################################
