"""
Rotate M * M MATRIX

input
    0   1   2   3
0   1   2   3   4
1   5   6   7   8
2   9   10  11  12
3   13  14  15  16

output
13   9   5   1
14   10  6   2
15   11  7   3
16   12  8   4

for x in rows.length ... 0 :
    for y in 0 ... columns.length :
            copy M[x][y] to new matrix


doing in place swapping :

   Mx,ny  nx,ny  nx,My  Mx,My       
   (3,0)  (0,0)  (0,3)  (3,3)  =>  (0,0)  (0,3)  (3,3)  (3,0)
   (2,0)  (0,1)  (1,3)  (3,2)  =>  (0,1)  (1,3)  (3,2)  (2,0)


   (2,1)  (1,1)  (1,2)  (2,2)  =>  (1,1)  (1,2)  (2,2)  (2,1)

"""

def rotate_inplace_matrix_levels(M) :
    nx = 0
    ny = 0
    Mx = len(M) - 1
    My = Mx

    for levels in range(0 , len(M)//2) :
        for offset in range(levels, len(M) - levels) :
            print(levels, offset)
            left_b = M[Mx - offset][levels]
            left_u = M[nx][ny + offset]
            right_u = M[nx + offset][My]
            right_b = M[Mx][My - offset]

            M[nx][ny + levels + offset] = left_b
            M[nx + levels + offset][My] = left_u
            M[Mx][My - levels - offset] = right_u
            M[Mx - levels - offset][ny] = right_b

    return M


def main() :
    test_data = [
        [1,   2,   3,   4],
        [5,   6,   7,   8],
        [9,  10,   11,  12],
        [13, 14,   15,  16]
    ]

    print("_"*30)
    print("./t", "Test Data :")

    for row in test_data :
        print(row)

    print("result is")

    result = rotate_inplace_matrix_levels(test_data)

    for row in result :
        print(row)

    print("_"*30)

if __name__ == "__main__" :
    main()



def rotate_inplace_matrix(M) :
    nx = 0
    ny = 0
    Mx = len(M) - 1
    My = Mx

    while Mx-nx > 0 :
        left_decreasing_row = Mx
        upper_increasing_col = ny
        right_increasing_row = nx
        bottom_decreasing_col = My

        while left_decreasing_row > nx :

            left_b = M[left_decreasing_row][ny]
            left_u = M[nx][upper_increasing_col]
            right_u = M[right_increasing_row][My]
            right_b = M[Mx][bottom_decreasing_col]

            M[nx][upper_increasing_col] = left_b
            M[right_increasing_row][My] = left_u
            M[Mx][bottom_decreasing_col] = right_u
            M[left_decreasing_row][ny] = right_b

            left_decreasing_row -= 1
            upper_increasing_col += 1
            right_increasing_row += 1
            bottom_decreasing_col -= 1

        Mx -= 1
        nx += 1
        ny += 1
        My -= 1

    return M