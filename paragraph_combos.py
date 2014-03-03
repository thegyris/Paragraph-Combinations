#!/usr/bin/python
import sys

#Introduce program to user
raw_input("\nThis program allows you to take a bunch of paragraphs (and various versions of\neach) and create output files with all possible combinations.  The order in your\ninput file should be: all versions of paragraph 1, then 2, then 3 and so on.\n\nPress Enter to continue . . . ")

#Request total number of paragrphs and number of version for each paragraph from user
n_para = input("\nHow many paragraphs in each output file? ")
n_versions = input("\nNow enter the number of versions for each paragraph you have by\nseparating each number by a comma and enclosing the group within brackets.\nFor example, if you have three paragraphs and two version for each,\nthen you should enter: [2,2,2].\n")

input_file = raw_input("\nEnter the name of the file that contains all of your paragraphs (ending with .txt):\n")

#Exit the code if the length of n_versions doesn't equal the number of paragraphs
if len(n_versions) != n_para:
    print "\nERROR:\nThe number of paragraphs doesn't match the series of numbers you inputted for the number of versions."
    print "Get your shit together!"
    sys.exit()

#Calculate total number of version to be outputted
total_versions = 1
for i in range(0,len(n_versions)):
    total_versions = total_versions * n_versions[i]
print '\nThis will produce ' + str(total_versions) + ' total versions.'
raw_input("\nPress Enter to produce the output . . . ")

#Open file that contains all of the paragraphs and read in and sparse all data
para_file = open (input_file,"r")
para_data = para_file.read()
split_data = para_data.split("\n\n")

#Confirm that the input makes sense.  If not, spit out an error to the user.
num_from_input = 0
for i in range(0,len(n_versions)):
    num_from_input = num_from_input + n_versions[i]

if len(split_data) != num_from_input:
    print '\nERROR:\nYour file contains ' + str(len(split_data)) + ' paragraph(s) but based on the number of versions\nfor each paragraph you entered, you file should contain ' + str(num_from_input) + ' paragraph(s).\nRemedy this and re-run.'
    sys.exit()

#Organize data in split_data by paragraph number and its versions
#Initialize list that will contain all organized paragraphs
total_num = 0
para_list = []
for i in range(0,n_para):
    para_list.append([i+1])

#Add version to appropriate part of list
for i in range(0,n_para):
    for j in range(0,n_versions[i]):
        para_list[i].append(split_data[total_num])
        total_num = total_num + 1

#Calculate repeat number for each paragraph
calc_times = []
for i in range(len(n_versions),0,-1):
    if i == len(n_versions):
        calc_times.append(1)
    else:
        item = calc_times[0] * n_versions[i]
        calc_times.insert(0,item)

#Create list of indices for appropriate versions
vers_ind = []
for npara in range(0,len(n_versions)):
    for v_num in range(0,total_versions):
        checkmod = (v_num + 1) % calc_times[npara]
        checkdiv = (v_num + 1) / calc_times[npara]
        if npara == 0:
            if checkmod == 0:
                vers_ind.append([checkdiv])
            else:
                vers_ind.append([checkdiv+1])
        elif npara == len(n_versions)-1:
            checkmod = (v_num + 1) % n_versions[-1]
            if checkmod == 0:
                vers_ind[v_num].append(n_versions[-1])
            else:
                vers_ind[v_num].append(checkmod)
        else:
            if checkmod == 0:
                place = checkdiv
            else:
                place = checkdiv + 1
            checkmodplace = place % n_versions[npara]
            if checkmodplace == 0:
                vers_ind[v_num].append(n_versions[npara])
            else:
                vers_ind[v_num].append(checkmodplace)

#Print out to files
for v_num in range(0,total_versions):
    filex_name = 'Version' + str(v_num+1) + '.txt'
    filex = open (filex_name,"w")
    for npara in range(0,len(n_versions)):
        filex.write(para_list[npara][vers_ind[v_num][npara]])
        filex.write('\n\n')
    filex.close()

print '\nAll ' + str(total_versions) + ' version(s) printed out successfully!\n' 
