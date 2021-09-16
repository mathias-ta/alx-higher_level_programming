#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_str = roman_string[::-1]
    c_num = 0
    p_num = 0
    t_int = 0
    if rom_str is not None:
        for char in rom_str:
            if ord(char) == ord("I"):
                c_num = 1
            elif ord(char) == ord("V"):
                c_num = 5
            elif ord(char) == ord("X"):
                c_num = 10
            elif ord(char) == ord("L"):
                c_num = 50
            elif ord(char) == ord("C"):
                c_num = 100
            elif ord(char) == ord("D"):
                c_num = 500
            elif ord(char) == ord("M"):
                c_num = 1000
            else:
                return 0
            if c_num < p_num:
                c_num = c_num * -1
            t_int = t_int + c_num
            p_num = c_num
        return t_int
    return 0
