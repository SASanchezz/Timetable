import Getting_info as gi
#nweek = int(input("What's the week? "))

days = gi.df[['Day', 'Time', 'Subject', 'Group', 'Week'][0]]
times = gi.df[['Day', 'Time', 'Subject', 'Group', 'Week'][1]]
subjects = gi.df[['Day', 'Time', 'Subject', 'Group', 'Week'][2]]
groups = gi.df[['Day', 'Time', 'Subject', 'Group', 'Week'][3]]
weeks = gi.df[['Day', 'Time', 'Subject', 'Group', 'Week'][4]]
nweek = 10
table = [
    'Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П`ятниця'
]


def day_of_week(nweek, wday):
    for i in range(0, len(weeks)):
        if type(weeks[i]) != float and nweek in weeks[i]:
            #for wday in table:
            if days[i] == wday:
                    #print(times[i])
                if subjects[i] == 'Англійська мова' or subjects[i] == 'Фізичне виховання':
                    try:
                        if subjects[i] != subjects[i+1] or times[i] != times[i+1]:
                            print(times[i], end='')
                            if subjects[i] != 'Англійська мова' and subjects[i] != 'Фізичне виховання' and subjects[i] != 'Українська мова (за професійним спрямуванням)':
                                print(' -', subjects[i],'(',groups[i],'група)')
                            elif (subjects[i] == 'Українська мова (за професійним спрямуванням)'):
                                print(' -', subjects[i].split('(')[0],'(',groups[i],'група)')
                            else: print(' -', subjects[i])

                    except KeyError:
                        if subjects[i] != subjects[i] or times[i] != times[i]:
                            print(times[i], end='')
                            if subjects[i] != 'Англійська мова' and subjects[i] != 'Фізичне виховання' and subjects[i] != 'Українська мова (за професійним спрямуванням)':
                                print(' -', subjects[i], '(', groups[i], 'група)')
                            elif (subjects[i] == 'Українська мова (за професійним спрямуванням)'):
                                print(' -', subjects[i].split('(')[0], '(', groups[i], 'група)')
                            else:
                                print(' -', subjects[i])


                else:
                    try:
                        if subjects[i] != subjects[i+1] or times[i] != times[i+1] or groups[i] != groups[i+1]:
                            print(times[i], end='')
                            if subjects[i] != 'Англійська мова' and subjects[i] != 'Фізичне виховання' and subjects[i] != 'Українська мова (за професійним спрямуванням)':
                                print(' -', subjects[i],'(',groups[i],'група)')
                            elif (subjects[i] == 'Українська мова (за професійним спрямуванням)'):
                                print(' -', subjects[i].split('(')[0],'(',groups[i],'група)')
                            else: print(' -', subjects[i])

                    except KeyError:
                        if subjects[i] != subjects[i] or times[i] != times[i]:
                            print(times[i], end='')
                            if subjects[i] != 'Англійська мова' and subjects[i] != 'Фізичне виховання' and subjects[i] != 'Українська мова (за професійним спрямуванням)':
                                print(' -', subjects[i], '(', groups[i], 'група)')
                            elif (subjects[i] == 'Українська мова (за професійним спрямуванням)'):
                                print(' -', subjects[i].split('(')[0], '(', groups[i], 'група)')
                            else:
                                print(' -', subjects[i])


for d in table:
    print(d)
    day_of_week(12, d)

