def sol (day, k):
    ref = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
    # ref = {}
    # ref['Mon'] = 1
    # ref['Tue'] = 2
    # ref['Wed'] = 3
    # ref['Thur'] = 4
    # ref['Fri'] = 5
    # ref['Sat'] = 6
    # ref['Sun'] = 0


    print(ref.index(day), k%7)
    print(ref[(ref.index(day)+k%7)%7])