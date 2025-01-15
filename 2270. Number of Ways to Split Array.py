def foo(numb):

    count = 0
    left_part = 0
    right_part = sum(numb)

    for i in range(len(numb) - 1):
        left_part += numb[i]
        right_part -= numb[i]
        if left_part > right_part:
            count += 1

    return count

print(foo([2,3,1,0]))