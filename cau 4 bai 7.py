def file_read_from_head(fname, nlines):
    from itertools import islice
    with open('D:/bài tập thưc hành/file txt.txt') as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('test.txt',1)
