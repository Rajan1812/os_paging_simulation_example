import random

secondry_mem_list=[]*100        #assuming hard disk(secondary memory) an large array with fixed size pages
process_number=[1,2,3]          #list of index og pages that cpu want to access.
main_mem_list=[9999]*50         #assuming ram an smaller array with fixed size frames 
process_table={}

def gen_random_for_ram():
  return random.randint(1,50)

#####################
generating random numbers in the hard disk
#####################
def hrdisk():
  for i in range(0,125):
    secondry_mem_list.append(random.randint(1,999))
  #print(secondry_mem_list)
  return secondry_mem_list


#####################
1. copying the required process from hard disk to RAM
2. creating a Process table mapping the pages & frames
#####################
def ram(process_number):
  for i in process_number:
    #print(i)
    while True:
      n=gen_random_for_ram()
      if main_mem_list[n] == 9999:
        break
    #print(n)
    main_mem_list[n]=hrdisk()[i]
    process_table[i]=n
    #print (main_mem_list)
  return main_mem_list,process_table


#####################
printing the value of the process which cpu has asked for in the form of pages from the RAM
#####################
def get_process_info_from_main_mem():
  mm_tuple=ram(process_number)
  pt=mm_tuple[1]
  print (pt)
  mm = mm_tuple[0]
  for keys in pt.keys():
    #print(keys, pt[keys])
    value=pt[keys]
    print (mm[value])

if __name__ == "__main__":
  get_process_info_from_main_mem()     #this will be called by cpu to get the process info which in this case is hard coded as variable "process_number"
