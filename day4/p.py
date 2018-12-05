f = open('input.txt', 'r')
l = f.readlines()
l = sorted(l)

def convert_time(time):
    time = time.split(' ')[1]
    return int(time.split(':')[1])

def subtract_time(time1, time2):
    return convert_time(time2) - convert_time(time1)

guards = {}
cur_guard = None
cur_guard_sleep = None
for i in l:
    s = i.split(']')
    time = s[0].replace('[', '')
    action = s[1]
    if 'Guard' in action:
        guard_id = action[action.find('#') + 1:action.find('b')-1]
        guards.setdefault(guard_id, [])
        cur_guard = guard_id
    if 'falls asleep' in action:
        cur_guard_sleep = time
    if 'wakes up' in action:
        time_asleep = subtract_time(cur_guard_sleep, time)
        guards[cur_guard].append([cur_guard_sleep, time_asleep])

sleep_times = []
for k, v in guards.items():
    slept = 0
    for intervals in v:
        slept += intervals[1]
    sleep_times.append(slept)

sleepiest = list(guards.keys())[sleep_times.index(max(sleep_times))]
print('Guard with most sleep time:', sleepiest)
look = guards[sleepiest]

timeline = {}

for i in range(60):
    timeline.setdefault(i, 0)

for loo in look:
    start = convert_time(loo[0])
    asleep = loo[1]
    end = start + asleep
    for i in range(start, end):
        #print(i)
        timeline[i] += 1

best = max(list(timeline.values()))
minute = 0
for k,v in timeline.items():
    if v == best:
        print('Minute:', k)
        minute = k

print('Answer to part 1:', int(sleepiest) * int(minute))

