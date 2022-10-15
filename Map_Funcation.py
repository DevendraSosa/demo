from re import I


def multiply(i):

    return i*i

#using map function

x = map(multiply,(3,5,7,11,13,19))
print(list(x))


# example = ["Welcome","to","Sem 3"]

# x = list(map(len,example))

# print(x)

# using map() with set 

# def example(i):
#     return i%3

# set_exam = {33,102,62,96,44,28,227}

# upd_itms = map(example,set_exam)

# print(set(upd_itms))
