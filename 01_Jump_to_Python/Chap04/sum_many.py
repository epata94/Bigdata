def sum_mul(choice, *args):
    if choice == 'sub':
        result = args[0]

        for i in args[1:]:
            result = result -i

    return result


result = sum_mul('sub',1,2,3)

print(result)
