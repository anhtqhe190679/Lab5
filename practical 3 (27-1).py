dict1 = {"Ten": 10, 'twenty': 20, 'thirty': 30}
dict2 = {'thirty': 30, 'fourty': 40, 'fifty': 50}
merged_dict = {**dict1, **dict2}
print(merged_dict)

employees = ['Kelly', 'Emma']
defaults = {'designation': 'Developer', 'salary': 8000}
defaults = str(defaults)
for i in employees:
    output = []
    a = (i + ':' + defaults)
    output.append(a)
    print(a)


    