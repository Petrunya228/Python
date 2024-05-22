import json
from itertools import groupby
from collections import Counter

with open ('skillbox_json_messages.log', 'r') as file:
    logs=[json.loads(line) for line in file] # loads- преобразует каждую строку в словарь

    logs_by_level = {}
    for log in logs:
        if log['level'] not in logs_by_level:
            logs_by_level[log['level']] = 1
        else:
            logs_by_level[log['level']] += 1

print(logs_by_level)

'-----------------------------------------'

with open ('skillbox_json_messages.log', 'r') as file:
    logs=[json.loads(line) for line in file]
    logs_by_time = {}
    for log in logs:
        if log['time'][11:-10] not in logs_by_time:
            logs_by_time[log['time'][11:-10]] = 1
        else:
            logs_by_time[log['time'][11:-10]] += 1
        max_key = max(logs_by_time, key=lambda x: logs_by_time[x])
        max_value = logs_by_time[max_key]
print(logs_by_time)
print(max_value)

'-----------------------------------------'

with open ('skillbox_json_messages.log', 'r') as file:
    logs=[json.loads(line) for line in file]
    count=0
    for log in logs:
        if log['level']=='CRITICAL':
            if log['time']=='05:00:00' and log['time'] <= '05:20:00':
                count+=1
print(count)

'-----------------------------------------'

with open ('skillbox_json_messages.log', 'r') as file:
    logs=[json.loads(line) for line in file]
    count=0
    for log in logs:
        if log['message'].lower()=='dog':
            count+=1
print(count)

'-----------------------------------------'

with open ('skillbox_json_messages.log', 'r') as file:
    logs=[json.loads(line) for line in file]
    warn_mes=[]
    for log in logs:
        if log['level']=='warning':
            warn_mes.append(log['message'])

    words_counter = Counter()
    for message in warn_mes:
        for word in message.lower().split():
            words_counter[word] += 1
    most_common_word = max(words_counter, key=words_counter.get)
print(most_common_word)