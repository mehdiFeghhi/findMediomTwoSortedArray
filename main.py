
def find_mediom(array, size):
    if size == 1:
        return array[0]
    if size == 2:
        return (array[0]+array[1]) / 2
    if size % 2 == 1:
       return array[size//2]
    else:
        return (array[size//2] + array[size//2+1])/2


def mid_two_array(left ,n ,right ,m ):

    left_mid = find_mediom(left, n)
    right_mid = find_mediom(right, m)

    if left_mid == right_mid:
        return left_mid
    elif n == 1 and m == 1 :
        return (left[0]+right[0])/2
    elif n == 1 and m == 2 :

        if left[0] > right[1]:
            return right[1]

        if left[0] > right[0]:
            return left[0]
        else:
            return right[0]

    elif n == 2 and m == 1 :

        if right[0] > left[1]:
            return left[1]
        if right[0] > left[0]:
            return right[0]
        else:
            return left[0]

    elif n == 2 and m == 2:

        return (max(left[0],right[0])+min(left[1],right[1]))/2

    else:
        if left_mid < right_mid:

            return mid_two_array(right[:(m // 2) + 1], m // 2, left[n // 2 :], n - (n // 2))
        else:
            return mid_two_array(left[:(n // 2) + 1], n // 2, right[m // 2:], m - (m // 2))

def main():

        print(mid_two_array([-11,8,11],3,[1,2,3,6],4))


if __name__ == '__main__':
    main()