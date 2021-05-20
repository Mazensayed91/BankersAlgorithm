from safe import *
from request import *
import numpy as np

allocation_input = input("Enter the allocation Matrix, ex.. for 2x2: 1 2,2 3 with spaces between numbers:")
max_input = input("Enter the max Matrix, ex.. for 2x2: 1 2,2 3 with spaces between numbers:")
available_input = input("Enter the available vector, ex.. 1 3 0 with spaces between numbers:")

allocation_matrix = []
for row in allocation_input.split(','):
    all_row = []
    for number in row.split(' '):
        all_row.append(int(number))
    allocation_matrix.append(np.array(all_row))

allocation_matrix = np.array(allocation_matrix)

max_matrix = []
for row in max_input.split(','):
    mx_row = []
    for number in row.split(' '):
        mx_row.append(int(number))
    max_matrix.append(np.array(mx_row))

max_matrix = np.array(max_matrix)

# Calculate need matrix, Need = Max - Allocation

available = []
for number in available_input.split(' '):
    available.append(int(number))
available = np.array(available)

need_matrix = max_matrix - allocation_matrix
print("need matrix : ")
print(need_matrix)

want_safe = int(input("Do you want to know if the state is safe?  1 for yes, 0 for no"))
if want_safe:
    safe, seq = is_safe(allocation_matrix, max_matrix, need_matrix, available)
    if safe:
        print("Yes, Safe state <", *seq, ">")
    else:
        print("No safe state")

want_req = int(input("Do you want to know if an immediate request can be granted?  1 for yes, 0 for no"))
if want_req:
    process_number = int(input("What is the process number?"))
    request_input = input("What is the request?")
    request = []
    for number in request_input.split(' '):
        request.append(int(number))
    request = np.array(request)

    granted, seq = immediate_request(process_number, request, allocation_matrix, max_matrix, need_matrix, available)

    if granted:
        print("Yes request can be granted with safe state , Safe state <P" + str(process_number) + "req,", *seq, ">")
    else:
        print("No request can't be granted with safe state")

    input()
