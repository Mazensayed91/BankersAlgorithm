import numpy as np


def is_safe(alloc_matrix, mx_matrix, need_matrix, avail):
    # Step 1 : Let Work, Finish be vectors of len m, n .. work = available and finish = false
    safe_seq = []
    work = avail.copy()  # copy of the available array
    n = alloc_matrix.shape[0]  # Number of proccesses
    m = alloc_matrix.shape[1]  # Number of resources

    finish = np.array([False for _ in range(n)])

    # Step 2 : Find an i such that both, a) finish[i] = false, Need[i] <= Work
    step4_flag = True
    while True:
        for i in range(n):
            if not finish[i]:  # Find an i such that finish[i] = false
                if len(need_matrix[i] <= work) == (
                        need_matrix[i] <= work).sum():  # Find an i such that Need[i] <= Work
                    process_number = i
                    safe_seq.append("P" + str(i))
                    step4_flag = False
                    work += alloc_matrix[process_number]
                    finish[process_number] = True

        if step4_flag:
            break
        step4_flag = True
    # Step 4: Check if finish = True for all i
    return finish.sum() == len(finish), safe_seq
