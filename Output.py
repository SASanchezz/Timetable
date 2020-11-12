import Getting_info as gi
#nweek = int(input("What's the week? "))

hdf = gi.df

days = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][0]]
times = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][1]]
subjects = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][2]]
groups = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][3]]
weeks = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][4]]
table = [
    'Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П`ятниця'
]


def day_of_week(nweek, wday, hdf):
    weeks = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][4]]
    for il in range(0, len(weeks)):
        if (type(weeks[il]) == float or nweek not in weeks[il]):
            hdf = hdf.drop([il])
    hdf = hdf.reset_index(drop=True)

    days = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][0]]
    times = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][1]]
    subjects = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][2]]
    groups = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][3]]
    weeks = hdf[['Day', 'Time', 'Subject', 'Group', 'Week'][4]]

    for i in range(0, len(weeks)):
        if days[i] == wday:
            if subjects[i] == 'Англійська мова' or subjects[i] == 'Фізичне виховання':
                try:
                    if subjects[i] != subjects[i+1] or times[i] != times[i+1]:
                        print(times[i], end='')
                        print(' -', subjects[i])

                except KeyError:
                    print(times[i], end='')
                    print(' -', subjects[i])


            else:
                try:
                    if subjects[i] != subjects[i+1] or times[i] != times[i+1] or groups[i] != groups[i+1]:
                        if i >= 2:
                            if times[i] != times[i - 1]:
                                print(times[i], end='')
                            else: print('       ', end='')
                        else: print(times[i], end='')
                        if subjects[i] != 'Англійська мова' and subjects[i] != 'Фізичне виховання' and subjects[i] != 'Українська мова (за професійним спрямуванням)':
                            print(' -', subjects[i],'(',groups[i],'група)')
                        elif (subjects[i] == 'Українська мова (за професійним спрямуванням)'):
                            print(' -', subjects[i].split('(')[0],'(',groups[i],'група)')
                        else: print(' -', subjects[i])

                except KeyError:
                    if i >= 2:
                        if times[i] != times[i - 1]:
                            print(times[i], end='')
                        else: print('       ', end='')
                    else: print(times[i], end='')
                    if subjects[i] != 'Англійська мова' and subjects[i] != 'Фізичне виховання' and subjects[i] != 'Українська мова (за професійним спрямуванням)':
                        print(' -', subjects[i], '(', groups[i], 'група)')
                    elif (subjects[i] == 'Українська мова (за професійним спрямуванням)'):
                        print(' -', subjects[i].split('(')[0], '(', groups[i], 'група)')
                    else:
                        print(' -', subjects[i])


for d in table:
    print("")
    print(d)
    day_of_week(13, d, hdf)