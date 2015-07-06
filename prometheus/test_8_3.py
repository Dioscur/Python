import sys
import math

def bouquets(narcissus_price, tulip_price, rose_price, summ):
    num = 0
    for narc in range (int(summ/narcissus_price+1)):
        for tul in range (int((summ-narc*narcissus_price)/tulip_price+1)):
            for rose in range (int((summ-narc*narcissus_price-tul*tulip_price)/rose_price+1)):
                if (narc+tul+rose)%2 and narc+tul+rose != 0:
#                    print narc, tul, rose
                    num += 1
    return num

narcissus_price = int(sys.argv[1])
tulip_price = int(sys.argv[2])
rose_price = int(sys.argv[3])
summ = int(sys.argv[4])

print bouquets(narcissus_price, tulip_price, rose_price, summ)
