def print_floyds_triangle(n):
    """ print Floyd's Triangle with n rows."""
    count = 1

    for i in range(1, n+1):
        for j in range(i):
            print(count, end= " ")
            count += 1
        print()

print_floyds_triangle(7)