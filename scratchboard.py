for diry in [-1, 0, 1]:
    print('==============')
    print('diry=' + str(diry))
    print('-----------')
    for dirx in [-1, 0, 1]:
        print('dirx=' + str(dirx))
        if diry == 0 and dirx == 0:
            print(str(diry) + ' ' + str(dirx) + ' skipped')
            continue
        print('OK!')
        stop = 0
        while stop < 9:
            if stop == 3:
                print('triggered at 3')
                stop += 4
                continue
            stop += 1
            print('stopvalue: ' + str(stop))
