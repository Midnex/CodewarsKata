#! python3
# Build a pil of cubes
# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

# Your task is to construct a building which will be a pile of n cubes. The cube
# at the bottom will have a volume of n ** 3, the cube above will have volume of
# (n-1) ** 3 and so on until the top which will have a volume of 1 ** 3.
#
# You are given the total volume m of the building. Being given m can you find the
# number n of cubes you will have to build?
#
# The parameter of the function findNb find_nb will be an
# integer m and you have to return the integer n such as n^3 + (n-1) ** 3 + ... +
# 1 ** 3 = m if such a n exists or -1 if there is no such n.

def find_nb(m):
    if 1 ** 3 == m:
        return 1
    else:
        n = 2
        volume = 1
        while volume < m:
            volume += n **3
            if volume == m:
                return n
            else:
                n += 1
                continue
        return -1

find_nb(4183059834009)#, 2022)
find_nb(24723578342962)#, -1)
find_nb(135440716410000)#, 4824)
find_nb(40539911473216)#, 3568)
find_nb(26825883955641)#, 3218)
