def file_read_from_head(fname, nlines):
    from itertools import islice
    with open('C:/Users/nilan/Desktop/obito.txt') as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('test.txt',1)
