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

timelines = {}
for k, v in guards.items():
    timeline = {}
    for i in range(60):
        timeline.setdefault(i, 0)
    for loo in v:
        start = convert_time(loo[0])
        end = start + loo[1]
        for i in range(start, end):
            timeline[i] += 1
    timelines[k] = timeline

maxes = {}
for k, v in timelines.items():
    maxes[k] = max(list(v.values()))

most_minute = max(list(maxes.values()))

# guard --> 2917


look = timelines['2917']

for k,v in look.items():
    if v == most_minute:
        print(k)
        # 35
