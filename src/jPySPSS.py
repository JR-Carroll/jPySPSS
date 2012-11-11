#!/usr/bin/python
# Filename: SPSS_Jpack.py

"""Authored by J. R. Carroll, 2010 in response to an email written to the UGA
Listserve:

"Dear all,

I've been trying to write Python code that mimics the 'to' keyword in SPSS.
So if my variables are v1 through v20 and I enter [v3 v5 to v7 v9]
I'd like it to return [v3 v5 v6 v7 v9]. Could anyone please out why my code is
not working? It doesn't generate any error but simply returns my original varlist.

[code omitted]

TIA!

Ruben van den Berg"
"""

def spssToRange(varss):
    """Allows a set of variable names to be passed to it in the standard SPSS
    variable ranges format.  This function then identifies "to" ranges and
    builds a list of variables that expand/iterate between the start and end variables.

    Example:

    spssToRange(v1, v2, v5 to v9, v11, v13)

    Will produce a return value of "v1, v2, v5, v6, v7, v8, v9, v11, v13"

    NB:  For this to work you must pass variables with the numerical index
    at the END of the variable name.  The function is not case sensitive -
    please consult jrc.csus@gmail.com or jrcarroll@jrcresearch.net if you want
    this altered"""

    varRange = vars.lower().split(' ')                                          #breaks up the variables (all lowercase) into a list separated by the spaces
    varRangePop = vars.split(' ')                                               #copies over the original string - named POP because elements are removed/popped and replaced with iterated values

    while 'to' in varRange:
        varPos = varRange.index('to')
        varPosition = varRangePop.index('to')                               #index of the first occurence of 'to'
        startVarIdx = varPosition - 1                                       #index of the starting variable
        endVarIdx = varPosition + 1                                         #index of the ending variable
        startVar = varRangePop[startVarIdx]                                 #assigns the beginning variable value
        endVar = varRangePop[endVarIdx]                                     #assigns the ending variable value                                         #removes the first occurence of 'to'

        startVarLen = len(startVar)                                         #how long is the variable length
        endVarLen = len(endVar)                                             #how long is the variable length

        startVarInt = ''                                                    #declares a string variable (empty)
        endVarInt = ''                                                      #declares a string variable (empty)
        prependVar = ''                                                     #string used to prepend the variable ranges as it iterates

        for i in range(startVarLen):                                        #checks the "startVar" variable in reverse order to detect if it is digit/alphabetic.  An attempt at 'logic'
            if startVar[-(i + 1)].isdigit() == True:
                startVarInt = startVar[-(i + 1)] + startVarInt

            else:
                break

        for i in range(endVarLen):                                          #checks the "endVar" variable in reverse order to detect if it is digit/alphabetic.  An attempt at 'logic'
            if endVar[-(i + 1)].isdigit() == True:
                endVarInt = endVar[-(i + 1)] + endVarInt

            else:
                break

        prependVarStart = startVar[:(startVarLen - len(startVarInt))]
        prependVarEnd = endVar[:(endVarLen - len(endVarInt))]
        #print prependVarStart, prependVarEnd

        if prependVarStart != prependVarEnd:
            varRTN = "** SPSS_JPack_ERROR:  Starting and Ending variable mismatch - check your syntax**"
            return varRTN
        else:
            pass


        diffVar = int(endVarInt) - int(startVarInt)
        iterList = []

        for i in range(1, diffVar):
            iterList.append((prependVarStart + str(int(startVarInt) + i)))

        varRangePop = (varRangePop[:(endVarIdx - 1)] + iterList +           #concatenates the multitude of lists into a single list
                        varRangePop[(endVarIdx - 1):])



        varRangePop.remove('to')
        varRange.remove('to')

    varRTN = " ".join(["%s" % el for el in varRangePop])
    return varRTN



varTest = 'vR1 vR2 to vR25 vR28 to vR33 erSTART23 to erSTART39'            #testing the code - needs to be removed if you plan on running as a standalone. Else, if ran as a function, no need
varCheck = spssToRange(varTest)                                          #testing the code - needs to be removed if you plan on running as a standalone. Else, if ran as a function, no need

print varCheck                                                                  #test print
