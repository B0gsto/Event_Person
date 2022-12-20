from datetime import datetime


def findMaxVal(array):
    lenArray = len(array)

    if lenArray > 1:
        maxVal = findMaxVal(array[1:])
        if array[0] > maxVal:
            return array[0]
        else:
            return maxVal
    elif lenArray == 1:
        return array[0]
    else:  # lenArray < 1
        return None


def timp_shell_sort(d):
    gap = len(d) // 2
    while gap > 0:
        for i in range(gap, len(d)):
            temp = d[i]
            j = i
            while j >= gap and d[j - gap].timp > temp.timp:
                d[j] = d[j - gap]
                j -= gap
            d[j] = temp
        gap //= 2
    return d


def timp_bubble_sort(d):
    # Get the keys and values of the dictionary
    keys = list(d.keys())
    values = list(d.values())
    items = list(d.items())
    # Perform the bubble sort algorithm
    n = len(values)
    for i in range(n):
        for j in range(0, n - i - 1):
            if values[j].timp > values[j + 1].timp:
                # Swap the elements
                items[j], items[j + 1] = items[j + 1], items[j]

    # Create a new dictionary with the sorted keys and values
    sorted_d = d

    # Return the sorted dictionary
    return sorted_d


def nume_shell_sort(d):
    gap = len(d) // 2
    while gap > 0:
        for i in range(gap, len(d)):
            temp = d[i]
            j = i
            while j >= gap and d[j - gap].nume > temp.nume:
                d[j] = d[j - gap]
                j -= gap
            d[j] = temp
        gap //= 2
    return d


def nume_bubble_sort(items):
    # Get the length of the list
    n = len(items)

    # Perform the bubble sort algorithm
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j].nume > items[j + 1].nume:
                # Swap the elements
                items[j], items[j + 1] = items[j + 1], items[j]

    # Return the sorted list
    return items


def adresa_shell_sort(d):
    gap = len(d) // 2
    while gap > 0:
        for i in range(gap, len(d)):
            temp = d[i]
            j = i
            while j >= gap and d[j - gap].adresa > temp.adresa:
                d[j] = d[j - gap]
                j -= gap
            d[j] = temp
        gap //= 2
    return d


def adresa_bubble_sort(items):
    # Get the length of the list
    n = len(items)

    # Perform the bubble sort algorithm
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j].adresa > items[j + 1].adresa:
                # Swap the elements
                items[j], items[j + 1] = items[j + 1], items[j]

    # Return the sorted list
    return items


def data_shell_sort(d):
    gap = len(d) // 2
    while gap > 0:
        for i in range(gap, len(d)):
            temp = d[i]
            j = i
            while j >= gap and datetime.strptime(d[j - gap].data, '%d.%m.%Y') > datetime.strptime(
                    temp.data, '%d.%m.%Y'):
                d[j] = d[j - gap]
                j -= gap
            d[j] = temp
        gap //= 2
    return d


def data_bubble_sort(d):
    # Convert the values (dates) to datetime objects
    values = list(d.values())
    datetime_values = [datetime.strptime(value.data, '%d.%m.%Y') for value in values]

    # Get the keys of the dictionary
    keys = list(d.keys())

    # Perform the bubble sort algorithm
    n = len(d)
    for i in range(n):
        for j in range(0, n - i - 1):
            if datetime.strptime(d[j].data, '%d.%m.%Y') > datetime.strptime(d[j + 1].data, '%d.%m.%Y'):
                # Swap the elements
                d[j], d[j + 1] = d[j + 1], d[j]

    # Create a new dictionary with the sorted keys and values
    sorted_d = d

    # Return the sorted dictionary
    return sorted_d


def BubbleSort(object, param, l, reverse=False):
    if object == 'Event':
        if param == 'data':
            d = {}
            no = 0
            for i in l:
                d[no] = i
                no += 1
            sorted_data = data_bubble_sort(d)
            if reverse == False:
                return sorted_data
            else:
                return dict(reversed(list(sorted_data.items())))
        elif param == 'timp':
            d = {}
            no = 1
            for i in l:
                d[no] = i
                no += 1
            sorted_data = timp_bubble_sort(d)
            if reverse == False:
                return sorted_data
            else:
                return dict(reversed(list(sorted_data.items())))
    elif object == 'Person':
        if param == 'nume':
            d = {}
            no = 0
            for i in l:
                d[no] = i
                no += 1
            if not reverse:
                return nume_bubble_sort(d)
            elif reverse:
                return dict(reversed(list(nume_bubble_sort(d).items())))
        elif param == 'adresa':
            d = {}
            no = 0
            for i in l:
                d[no] = i
                no += 1
            if not reverse:
                return adresa_bubble_sort(d)
            elif reverse:
                return dict(reversed(list(adresa_bubble_sort(d).items())))

    else:
        print('Invalid object')


def ShellSort(object, param, l, reverse=False):
    if object == 'Event':
        if param == 'data':
            d = {}
            no = 0
            for i in l:
                d[no] = i
                no += 1
            sorted_data = data_shell_sort(d)
            if reverse == False:
                return sorted_data
            else:
                return dict(reversed(list(sorted_data.items())))
        elif param == 'timp':
            d = {}
            no = 0
            for i in l:
                d[no] = i
                no += 1
            sorted_data = timp_shell_sort(d)
            if reverse == False:
                return sorted_data
            else:
                return dict(reversed(list(sorted_data.items())))
    elif object == 'Person':
        if param == 'nume':
            d = {}
            no = 0
            for i in l:
                d[no] = i
                no += 1
            if not reverse:
                return nume_shell_sort(d)
            elif reverse:
                return dict(reversed(list(nume_bubble_sort(d).items())))
        elif param == 'adresa':
            d = {}
            no = 0
            for i in l:
                d[no] = i
                no += 1
            if not reverse:
                return adresa_shell_sort(d)
            elif reverse:
                return dict(reversed(list(adresa_bubble_sort(d).items())))

    else:
        print('Invalid object')


def test_Event():
    from DOMAIN.event import Event
    l = []
    l.append(Event('1.5.2023', 1, 'a'))
    l.append(Event('5.1.2023', 2, 'b'))
    l.append(Event('3.6.2120', 3, 'c'))
    l.append(Event('4.3.2021', 4, 'd'))
    d1 = BubbleSort('Event', 'data', l, reverse=True)
    for i in d1:
        print(d1[i])
    print()
    d2 = ShellSort('Event', 'data', l, reverse=True)

    for i in d2:
        print(d2[i])
    print()
    print('-------------------')
    d = BubbleSort('Event', 'timp', l, reverse=False)
    for i in d:
        print(d[i])
    print()
    d = ShellSort('Event', 'timp', l, reverse=False)
    for i in d:
        print(d[i])
    print()


def test_Person():
    from DOMAIN.person import Person
    l = []
    l.append(Person('h', 'x'))
    l.append(Person('b', 'q'))
    l.append(Person('w', 't'))
    l.append(Person('d', 'a'))
    d1 = (BubbleSort('Person', 'nume', l, reverse=True))
    for i in d1:
        print(d1[i])
    print()
    d3 = (ShellSort('Person', 'nume', l, reverse=False))
    for i in d3:
        print(d3[i])
    print()
    print('-------------------')
    d2 = (BubbleSort('Person', 'adresa', l, reverse=False))
    for i in d2:
        print(d2[i])
    print()
    d4 = (ShellSort('Person', 'adresa', l, reverse=False))
    for i in d4:
        print(d4[i])
