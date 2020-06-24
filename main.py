
'''
 Gizem Pesen
 170709050
 github.com/GPS199/ceng_2034_2020_makeup
#!/urs/bin/env python
'''






import time # to check elapsed times 

start_import = time.time()
import os, os.path # to create child and parent process 
import requests # to download images
from os import path # to check path 
import uuid # to create random image name if images dont have 
import hashlib # to use hashlib -md5/sha256-
import threading # to download images with thread
import multiprocessing # to learn cpu the number of CPU cores
from multiprocessing import Pool, Process # for multiprocessing
import psutil #to learn memory and cpu usage
import subprocess # to clean orphans
import sys #to animation
import signal 
import shutil #for removing file

end_import = time.time()






initial_directory = '.'
source = 'Images/'
file_name_list = [] 
threads = []
hashes = {}
duplicates = []
duplicate_first = []




required_memory_mb = 30  # minimum required amount of memory in Megabytes
hash_buffer_size = 30000  # buffer size in bytes 
movie_file_path = None  #  the movie file path is not exist 




#Just an animation for loading 
def animation():
  animation = "|/-\\" 

  for i in range(10):
      time.sleep(0.1)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()



      

# The links which given to download
urls = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg","http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"] 








#Create a file with os.mkdir
def createDirectory(path): 
    access_rights = 0o777

    try:
        os.mkdir(path, access_rights)
    except OSError:
        print('Creation of the directory %s failed' % path)
    else:
        print('Successfully created the directory %s' % path)



def changeDirectory(getDirectory):  # Change Directory 
    first_directory = os.getcwd()
    os.chdir(getDirectory)
    print('Directory Changed as', first_directory + '/' + getDirectory)





def filesinFolder():  # Find count of file in folder that download images.
    print('Images folder contains', len(os.listdir(initial_directory)), 'files.')
  
  
  
def remove_file():
  shutil.rmtree(source)









#2.1 Download the files with child process using multi threading for retrieving the files

start_download_thread = time.time()  

def check_path_exist(file_name): 
        isExist = path.exists(file_name) # path exists or not 
        if isExist == 0: # if there is no file name
                print ("directory not exists:" + str(path.exists(source)))
                file = file_name if file_name else str(uuid.uuid4()) # random file name 
        else:
                print ("directory exists:" + str(path.exists(source)))



def download_file(url, file_name_list, file_name = None, ):
    r = requests.get(url, allow_redirects=True) #requests.get method makes a request to a url, and return the status code.
    file = file_name if file_name else str(uuid.uuid4())
    #check_file_exist(file_name)
    open(file, 'wb').write(r.content) # open the downloaded file
    file_name_list.append(file) #I wanted to add to list that I create
  

def create_download_thread(urls,file_name_list):

    for url in urls: #in urls array take loop 
        print("{} files downloading...\n".format(len(urls)))
        download_thread = threading.Thread(target=download_file,args=(url,file_name_list,))
        download_thread.start() 
        threads.append(download_thread) #add downloaded threads to list
        
    for thread in threads:
        thread.join()


    

proc = Process(target=create_download_thread,args=(urls,file_name_list,))
proc.start()
proc.join()

#create_download_thread(urls,file_name_list)
end_download_thread = time.time()






#1: Create a new child process with syscall and print its PID

start_child = time.time()  #I wanted to check time of every operation and list them

# Create Parent and Child Process
def parent_child_process():
    pid = os.fork()                 

    if(pid > 0):# n greater than 0  means parent process 
      animation()
      print("parent process id: {}" .format(os.getpid()))

    elif (pid == 0):# Pid is equal to 0 means child process
      animation()
      print("child process id: {}".format(os.getpid())) 





      
#If you want to direct download files with child process 
def download_file2():
  #print("{} files downloading...\n".format(len(urls)))
  for i in range(len(urls)):
    try:
        download_file(urls[i], "file{}".format(i))
    except AttributeError:
        print("it is running")
    print("file{0} downloaded from\n{1}\n".format(i, urls[i]))



#download_file2()
end_child = time.time()  










# 2.2 : Clean Orphans 
start_clean_orphans = time.time()

def clear_orphans(): 
  process= subprocess.Popen( ('ls', '-l', '/tmp'), stdout=subprocess.PIPE)
  for line in process.stdout:
        pass
    
  subprocess.call( ('ps', '-l') )
  process.wait()
  #print( "clearing...\n")
  print("\n")
  subprocess.call( ('ps', '-l') )

end_clean_orphans = time.time()







#3 Multiprocessing

#3.1 : Check the system and learn the number of CPU cores. Create n processes if there are n cores.

print("The number of cpu count is:",multiprocessing.cpu_count())

#3.2 : Control duplicate files within the downloaded files of your python code. You should do it by using multi processing techniques. 



start_find_duplicates = time.time()

def findDuplicates():  
    for index, filename in enumerate(os.listdir('.')): #count each iteration
        if os.path.isfile(filename):  #used path library and checked
            index = filename
            with open(filename, 'rb') as f:  #open file 
                image_hash = hashlib.md5(f.read()).hexdigest()  #using md5 for each file

            if image_hash not in hashes:
                hashes[image_hash] = index  # create new key and stored has_keys dict()

            else:
                duplicates.append((index, hashes[image_hash]))  #adding the duplicate list that I create before
                print('Image ' + hashes[image_hash] + ' is duplicate of Image ' + index)





def remove_dup():
  print("\nDo you want to delete duplicate images? [y/n]")             
  while(True):
    remove = input("\nPlease enter the command number:\n")  
    if(remove == "y"): 
      try:
        files_list = os.listdir()#list of the all files located
      #delete files after printing:
        for index in duplicates:
          index = 0
          os.remove(files_list[index]) ##remove duplicate files
      except:
         print("there is a problem but it is correct algorithm, please control your function and try again.")

    else:
      print("you did't delete duplicte images")

#findDuplicates()
end_find_duplicates = time.time()



# Before Multiprocessing get hashes from image.
def takegethash():  
    for index, filename in enumerate(os.listdir('.')):
        if os.path.isfile(filename):
            index = filename
            with open(filename, 'rb') as f:
                image_hash = hashlib.md5(f.read()).hexdigest()
            duplicate_first.append((index, image_hash))




def duplicateFinder(element,array): #Take hash list and find Duplicated elements
    c = 0
    for i in range(len(array)):
        if element[1] == array[i][1]:
            c += 1

        if c > 1 :
            return element




start_find_duplicates_multiproc = time.time()

def multiProcessFindDuplicates(): 
  # p0 = multiprocessing.Process(target=duplicateFinder, args=((os.listdir(initial_directory)[0])))
  # p1 = multiprocessing.Process(target=duplicateFinder, args=((os.listdir(initial_directory)[1])))
  # p2 = multiprocessing.Process(target=duplicateFinder, args=((os.listdir(initial_directory)[2])))
  # p3 = multiprocessing.Process(target=duplicateFinder, args=((os.listdir(initial_directory)[3])))
  # p4 = multiprocessing.Process(target=duplicateFinder, args=((os.listdir(initial_directory)[4])))
  #
  # p0.start()
  # time.sleep(0.1)
  # p1.start()
  # time.sleep(0.1)
  # p2.start()
  # time.sleep(0.1)
  # p3.start()
  # time.sleep(0.1)
  # p4.start()

#Using Pool() it would meaningless to use more than your cpu count.  So it used os.cpu_count() as an argument,because your OS can only use how much you have. 

    with multiprocessing.Pool(os.cpu_count()) as Pool:
        
      
        list_duplicate = Pool.starmap(duplicateFinder,([duplicate_first[0],duplicate_first],[duplicate_first[1],duplicate_first],[duplicate_first[2],duplicate_first],[duplicate_first[3],duplicate_first],[duplicate_first[4],duplicate_first]))

    for value in list_duplicate:
        if value != None:
            duplicates.append(value)
    print(duplicates)
    print('Image ' + duplicates[1][0] + ' and Image ' + duplicates[0][0] + ' are duplicated.') 
    print('Image ' + duplicates[3][0] + ' and Image ' + duplicates[2][0] + ' are duplicated.')


#multiProcessFindDuplicates()
end_find_duplicates_multiproc = time.time()




# It is the same with Find duplicate but for multiThread
def multiThreadDuplicates(filename):  
        if os.path.isfile(filename):
            index = filename
            with open(filename, 'rb') as f:
                image_hash = hashlib.md5(f.read()).hexdigest()

            if image_hash not in hashes:
                hashes[image_hash] = index

            else:
                duplicates.append((index, hashes[image_hash]))
                print('Image ' + hashes[image_hash] + ' is duplicate of Image ' + index)







def multiThreadFindDuplicates(): # MultiThreading function the process
    print("here")
    for image in os.listdir(initial_directory):
        print("here")
        process = threading.Thread(target=multiThreadDuplicates, args=image)
        process.start()
        threads.append(process)

    for process in threads:
        process.join()






def wait_timeout(proc, seconds):
    """Wait for a process to finish, or raise exception after timeout"""
    start = time.time()
    end = start + seconds
    interval = min(seconds / 1000.0, .25)

    while True:
        result = proc.poll()
        if result is not None:
            return result
        if time.time() >= end:
            raise RuntimeError("Process timed out")
        time.sleep(interval)
        
#wait_timeout(p, seconds)




def movie_file():
  if movie_file_path:
        movie_hash = takegethash(movie_file_path)
        print("The hash of the movie using {} byte chunks: {}".format(hash_buffer_size, movie_hash))
        print("\nExiting...")


#If files are huge ... use this
def read_chunk(fobj, chunk_size = 2048):
    """ Files can be huge so read them in chunks of bytes. """
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk


#Memory and CPU Usage

max_cpu_percent = 50
max_memory_percent = 50
    
print(psutil.cpu_times())

def cpu_usage():
  print("CPU Percent=\n")
  print(psutil.cpu_percent(interval=1))
  psutil.cpu_percent(interval=1)
  cpu_percent = psutil.cpu_percent(interval=1)
  if(cpu_percent > max_cpu_percent):
      print("Warning")
      print("CPU Usage Greter than 50%")
    
def memory_usage():
  print(psutil.virtual_memory())
  mem =  psutil.virtual_memory()

  print("Memory Percent="+str(mem.percent))
  if(mem.percent > max_memory_percent):
      print("Memory Usage Greter than 50%")
    


 



os.system("clear")

#-----------------------------------------------------------------------------------------------------------------------------
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

# A List of Items
items = list(range(0, 57))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
#--------------------------------------------------------------------------------------------------------------------------------










print("\nWelcome Screen\n")
print("------------------------------------------------------------")


#On the Screen ..
print("General Information")
print("------------------------------------------------------------")
print("Operating System Type: ", os.name, "\n") #Windows = nt / Linux = posix
print("Your Destination: ", os.getcwd(), "\n") #current path
print("CPU (Core) Count: ", str(os.cpu_count()), "\n") 
print("Load avg:", os.getloadavg(), "\n")
print("------------------------------------------------------------")
print("Python version:")
os.system("python3 --version")
print("\n")
print("Kernel version:")
os.system("uname -srm")
print("------------------------------------------------------------")
print("\n \n  Please enter the command number to execute the script: \n"
      " 1 : Create a New Parent and Child Process and Print Process ID (PID). \n"
      " 2 : Check is there a directory or not. \n"
      " 3 : Create a New Directory, Change Directory and Find count of File in it. \n"
      " 4 : Change Directory \n"      
      " 5 : Download the Files With Child Process.(and Avoid Orphans) \n"
      " 6 : Download Files With Threads. \n"
      " 7 : Clean Out the Orphans. \n"
      " 8 : Find Duplicates. \n"
      #" 9 : Control Duplicate Files With Multi Thread. \n"
      " 9 : Control Duplicate Files With Multi Processing. \n"
      " 10 : Check Memory Usage and CPU Usage. (psutil library)\n"
      " 11 : Memory Information.\n"
      " 12 : Print Elapsed Time of Every Programs . \n"
      " 13 : Is Memory Available , Wait it. \n"
      " 14 : Remove File \n"

      " 0 : Exit the script.\n")
print("------------------------------------------------------------\n")


 



 

Elapsed_import = end_import - start_import
Elapsed_child_down = end_child - start_child
Elapsed_thread_down = end_download_thread - start_download_thread
Elapsed_clean_orphan = end_clean_orphans - start_clean_orphans
Elapsed_find_duplicates = end_find_duplicates - start_find_duplicates
#Elapsed_find_duplicates_thread = end_find_duplicates_thread - start_find_duplicates_thread
Elapsed_find_duplicates_multiproc = end_find_duplicates_multiproc - start_find_duplicates_multiproc


def print_times_of_programs():
  print("------------------------------------------------------------")
  print("\nElapsed time with importing: " ,round(Elapsed_import,3), "\n")
  print("\nElapsed time with downloading : ",round(Elapsed_child_down,3),"\n")
  print("\nElapsed time with downloading with thread:",round(Elapsed_thread_down,3),"\n")
  print("\nElapsed time with cleaning orphan process :",round(Elapsed_clean_orphan,3),"\n")
  print("\nElapsed time with finding duplicate files :",round(Elapsed_find_duplicates,3),"\n")
 # print("\nElapsed time with find duplicate images with multithread:",round(Elapsed_find_duplicates_thread,3),"\n")
  print("\nElapsed time with find duplicate images with multiprocessing:",round(Elapsed_find_duplicates_multiproc,3),"\n")
   








 

class FreeMemLinux(object):

    def __init__(self, unit='kB'):

        with open('/proc/meminfo', 'r') as mem:
            lines = mem.readlines()

        self._tot = int(lines[0].split()[1])
        self._free = int(lines[1].split()[1])
        self._buff = int(lines[2].split()[1])
        self._cached = int(lines[3].split()[1])
        self._shared = int(lines[20].split()[1])
        self._swapt = int(lines[14].split()[1])
        self._swapf = int(lines[15].split()[1])
        self._swapu = self._swapt - self._swapf

        self.unit = unit
        self._convert = self._factor()

    def _factor(self):
        """determine the convertion factor"""
        if self.unit == 'kB':
            return 1
        if self.unit == 'k':
            return 1024.0
        if self.unit == 'MB':
            return 1/1024.0
        if self.unit == 'GB':
            return 1/1024.0/1024.0
        if self.unit == '%':
            return 1.0/self._tot
        else:
            raise Exception("Unit not understood")

    @property
    def total(self):
        return self._convert * self._tot

    @property
    def used(self):
        return self._convert * (self._tot - self._free)

    @property
    def used_real(self):
        """memory used which is not cache or buffers"""
        return self._convert * (self._tot - self._free -
                                self._buff - self._cached)

    @property
    def shared(self):
        return self._convert * (self._tot - self._free)

    @property
    def buffers(self):
        return self._convert * (self._buff)

    @property
    def cached(self):
        return self._convert * self._cached

    @property
    def user_free(self):
        """This is the free memory available for the user"""
        return self._convert *(self._free + self._buff + self._cached)

    @property
    def swap(self):
        return self._convert * self._swapt

    @property
    def swap_free(self):
        return self._convert * self._swapf

    @property
    def swap_used(self):
        return self._convert * self._swapu






def print_memory_info():

  f = FreeMemLinux()
  print("Total Memory:",f.total,"\n")
  print("Used Memory:",f.used,"\n")
  print("Free Memory:",f.user_free,"\n")


  f_mb = FreeMemLinux(unit='MB')
  print("Total Memory (MB):",f_mb.total,"MB\n")
  print("Used Memory (MB):",f_mb.used,"MB\n")
  print("Free Memory (MB):",f_mb.user_free,"MB\n")


  f_percent = FreeMemLinux(unit='%')
  print("Percentage of Total Memory:",f_percent.total,"%\n")
  print("Percentage ofUsed Memory:",f_percent.used,"%\n")
  print("Percentage ofFree Memory:",f_percent.user_free,"%\n")





#4 a: Check available memory of the system, minimum required memory.


def available_memory() -> int:
    # open this file for memory information  
    with open('/proc/meminfo', 'r') as mem:
        ret = {}
        free = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) == 'MemTotal:':
                ret['total'] = int(sline[1])
            elif str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free += int(sline[1])
        return free


#4 c: Include the routine that will wait until the system frees that memory.


def wait_until_memory_is_available():
    while True:  # wait until memory becomes available
        print("memory is available")
        available_memory_mb = available_memory() / 1000
        if available_memory_mb < required_memory_mb:  
            print(
                "memory is not enough! Available: {} MB | Required: {} MB".format(available_memory_mb, required_memory_mb))
            time.sleep(1)  # wait 
        else:
            return  



  








while(True):
  command = input("\nPlease enter the command number:\n")
  if(command==None or command=="" or command==" "):     #base case
    print("Unvalid command number was sended.")
  
  
  elif(command=="1"):
    animation()
    parent_child_process()
  
  elif(command=="2"):
    animation()
    check_path_exist(source)


  elif(command=="3"):
    animation()
    createDirectory(source)
    filesinFolder()

  elif(command=="4"):
    animation()
    changeDirectory(source)
    
  elif(command=="5"):
    animation()
    print("\n")
    pid = os.fork() 
    if pid > 0: 
        os.waitpid(pid, 0) #For avoiding orphan process 
        print("")    
    else: 
        download_file2()
 
  elif(command=="6"):
     animation()
     create_download_thread(urls,file_name_list)
     

  elif(command=="7"):
    animation()
    print("\n")
    clear_orphans()
    print("\nit takes",Elapsed_clean_orphan,"seconds")

  elif(command=="8"):
    animation()
    print("\n")
    findDuplicates()
#    remove_dup()


  elif(command=="9"):
    animation()
    print("\n")
    takegethash()
    multiProcessFindDuplicates()

  elif(command=="10"):
    animation()
    memory_usage()
    print("\n")
    cpu_usage()
  

  elif(command=="12"):
    animation()
    print("\n")
    print_times_of_programs()

  elif(command=="11"):
    animation()
    print("\n")
    print_memory_info()

  elif(command=="13"):
    animation()
    print("\n")
    wait_until_memory_is_available()

  elif(command=="14"):
    animation()
    print("\n")
    remove_file()
    print(" File Removed.")


  elif(command=="0"):
    print("Exiting from the script.")






