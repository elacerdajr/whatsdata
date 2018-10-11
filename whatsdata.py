#Script to see who talks more, etc
import numpy as np
from sys import argv
import re

#add: date range, percentual, openning a day, sentiments ...

def intro():

    head = cg+  "--->  Whatsapp Analytics\n"+end_c
    lin = len(head)*'-'
    print lin,'\n',head,lin,'\n'

def get_lines(inputname):

    ftxt = open(inputname,'r')
    lines = ftxt.readlines()
    return lines

def stat_print(members,feature):

    print '\n'
    th =   '%25s | %30s   %15s'  %("Member",cg+feature+end_c,"Percentual %%") 
    print len(th)*'-'
    print th
    print len(th)*'-'

    tot_feature = float(sum(members.values()))

    for k,v in sorted(members.iteritems(),key=lambda (k,v): (v,k),reverse=True):
        print '%25s | %20d   %15.1f' %(k,v,v*100./tot_feature) 

def print_date_range(lines):

    ini = lines[0][:8]
    end = lines[-1][:8]

    print "-> From %s to %s" %(ini,end)


def run_analysis(lines):

    members = {}
    startname_idx = 16
    members_midia = {}
    members_sym = {}
    for l in lines:
        # print l
        if l[0:1].isdigit()and l[3:4].isdigit() and l[6:7].isdigit():
            endname_idx = l[startname_idx:].find(':') + startname_idx
            #print l[startname_idx:endname_idx]
            mname =l[startname_idx:endname_idx].replace("\s+",'') 
            mmessage = l[endname_idx+1:-1]
            size_msg = len(mmessage)
            if len(mname)>1: 
                if mname not in  members.keys():
                    members[mname] = 0
                    members_sym[mname] = 0
                    members_midia[mname] = 0
                else:
                    members[mname] += 1
                    members_sym[mname] += size_msg
                    if mmessage.count("<Arquivo")>0:
                        members_midia[mname] +=1 

    return members,members_sym,members_midia

def define_colors():

    global cr,cb,cg,cy
    global end_c

    cg = '\33[92m'
    cm = '\33[95m'
    end_c = '\33[0m'

###########################################################################

# INPUT
lines = get_lines(argv[1])

define_colors()
intro()
print_date_range(lines)

# ANALYSIS
members_count,members_sym,members_midia = run_analysis(lines)

#PRINT

stat_print(members_count,"Messages")
stat_print(members_sym,"Text Volume")
stat_print(members_midia,"Midia")
