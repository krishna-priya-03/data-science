import numpy as np

def create_matrix(mc):
    print("\nArray " + str(mc) + " Elements:")
    array_1 = map(int, input().split())
    array_1 = np.array(list(array_1))

    print("\nArray " + str(mc) + " Row & Column:")
    row, column = map(int, input().split())

    if len(array_1) != (row * column):
        print("\nRow and column size not match with total elements!!! Retry!!!")
        return create_matrix(mc)

    array_1 = array_1.reshape(row, column)

    print("\nArray " + str(mc))
    print(array_1)

    print("\nTranspose:")
    return array_1.transpose()


print(create_matrix(1))