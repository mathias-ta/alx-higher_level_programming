#!/usr/bin/python3
def best_score(a_dictionary):
    highest_value = 0
    if a_dictionary is not None:
        for key, value in sorted(a_dictionary.items()):
            if value >= highest_value:
                highest_value = value
        return key
    return None
