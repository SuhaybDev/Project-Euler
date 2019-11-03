# Program to find the product of a pythagorean triplet whose sum of the squares is equal to 1000


def findTripletPro(sum):
    for a in range(1, sum + 1):
        for b in range(1, sum + 1):
            c = sum - a - b
            if a*a + b*b == c*c:
                return (a * b * c)


print(findTripletPro(1000))