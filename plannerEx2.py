meetings = int(input('How many meetings today?\n'))
meetings_list = []
line_list = []
ordered_list = []


for _ in range(meetings):
    meeting = {}
    races_list = []
    meeting_name = input('What is the name of the meeting?\n')
    number_races = int(input('How many races?\n'))
    race_type = input('Flat or Jumps?\n')
    operator = input('What is the name of the operator?\n')
    runners = ''
    for _ in range(number_races):
        races = {}
        hour = input('Enter hour\n')
        runners = input('How many runners?\n')
        races['hour'] = hour
        races['runners'] = runners
        races_list.append(races)
    meeting['name'] = meeting_name
    meeting['type'] = race_type
    meeting['operator'] = operator
    meeting['races'] = races_list
    meetings_list.append(meeting)

print(meetings_list)

for meeting in meetings_list:
    teller = 1
    for race in meeting['races']:
        line = f"{race['hour']} {meeting['name']} R{teller} ({race['runners']} runners - {meeting['type']}" \
               f" - {meeting['operator']})"
        teller += 1
        line_list.append(line)

teller = 1
for line in sorted(line_list):
    print(f"{line} ->{teller}")
    print("\t1\t\t6\t\t11")
    print("\t2\t\t7\t\t12")
    print("\t3\t\t8\t\t13")
    print("\t4\t\t9\t\t14")
    print("\t5\t\t10\t\t15")
    print('')
    print('')
    teller += 1






