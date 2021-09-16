#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        total_score = 0
        total_weight = 0
        av_score = 0
        for tupl in my_list:
            (score, weight) = tupl
            total_score += (score * weight)
            total_weight += weight
        if total_weight > 0:
            av_score = total_score/total_weight
        return av_score
    else:
        return (0)
