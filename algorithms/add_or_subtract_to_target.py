# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'minNum' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER threshold
# #  2. INTEGER_ARRAY happy
# #
#
#     def minNum(threshold, happy):
#
#
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     threshold = int(input().strip())
#
#     happy_count = int(input().strip())
#
#     happy = []
#
#     for _ in range(happy_count):
#         happy_item = int(input().strip())
#         happy.append(happy_item)
#
#     result = minNum(threshold, happy)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()