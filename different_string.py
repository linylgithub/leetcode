#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: different_string.py
@time: 2018/8/18 18:39
"""
class Different:
    def checkDifferent(self, iniString):
        # write code here
        pass

class Zipper:
    def zipString(self,iniString):
        current_str = ''
        count = 1
        current_char = ''
        i = 0
        for item in iniString:
            print(item)
            i += 1
            if current_char == item:
                count += 1
                print i,len(iniString)
                if i == len(iniString):
                    current_str += str(count)
            else:
                if len(current_str) > 1 or count > 1:
                    current_str = current_str + str(count)+item
                else:
                    current_str = current_str + item
                count = 1
                current_char = item
        if len(current_str) < len(iniString):
            return current_str
        else:
            return iniString




if __name__ == '__main__':
    # different = Different()
    # print different.checkDifferent('hjhjhjha')
    zip_string = Zipper()
    print zip_string.zipString('jjjjjjxxxxxxxooZLLLLLLLLQQQQQQQQQLLLLLLLLECXXXXXXXIIIIIIIIIhjjyyySSooooooooommmuuEEEEEEEEEnnnnnnnffffffAAAAAllllllllbbbbkkkkkkkkkkkkKKKKKKhhhhhhhhhooooooooooYCCCCCCOOOOOOOOOMMMMMMMMMMiiiiiivvvvvvvWWWWkkkkkkwwwwwwwMmmmmmmmmLLLwwwwwwwkkkjjjjjjttttQQQQQQQQQaaaaaaaFFFFFFFlllllllllggggggggggPPPPPPuuuuuuuuaYYYYYYwQQQFFFFFFFFFFaaaaapXXXXXXXxxxxxxQQQQQQQQQsssssGGGGfffffffddddddpppQQQQQQHHHTTTaaaaaaGGGGGGddyyyyyMhhllllllllllNNNNNNNNUUUWWWWWWLLLLLLLLLYYYYYYYYYYTTKKKKKKKKiiiiiiitttttttXXXXXXXXXLLLHZZZZZZZssssjjJJJEEEEEOOOOOttttttttttBBttttttTTTTTTTTTTrrrrttttRRRRRyyooooooaaaaaaaaarrrrrrrPPPPPPPjjPPPPddddddddddHHHHnnnnnnnnnnSSSSSSSSSSzzHHHHHHHHHddddddDDDzzzhhhhhfffffffffftttttteeeeeeeeEEEEEEEEEaaaaaaccccccccccFFFFFFFF')
