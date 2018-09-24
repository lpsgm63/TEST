# Input: User's Input_Data
# Ouput: redirection Address (Fake Info Leak Page, Fake DB Connection Php)

import sys

filter_char = []
attack_char = ['\"','\'','#']

if __name__ == '__main__':
    print "Program Starting..."

    if len(sys.argv) != 2 :
        print "Need a Argument (Input_Data)"
        exit()

    query = sys.argv[1]

    # if Attack Query : redirection Fake Php
    # else : redirection Nomal Page
