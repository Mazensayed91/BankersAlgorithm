from safe import *
import numpy as np


def immediate_request(process_num, req, alloc_matrix, mx_matrix, need_matrix, avail):

    can_be_done_flag = False
    nd_matrix = need_matrix.copy()
    av = avail.copy()
    all_mat = alloc_matrix.copy()

    if (req <= nd_matrix[process_num]).sum() == len(req <= nd_matrix[process_num]):
        if (req <= av).sum() == len(req <= av):
            can_be_done_flag = True
            av -= req
            all_mat[process_num] += req
            nd_matrix[process_num] -= req
    if can_be_done_flag:
        return is_safe(all_mat, mx_matrix, nd_matrix, av)
    else:
        return 0, 0
