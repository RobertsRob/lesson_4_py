def func_1(num_1, num_2):
    for y_i in range(num_2):
        for x_i in range(num_1):
            print(" "+str((x_i+y_i)%10)+" ", end="")
        print()

func_1(10,10)  # x, y
