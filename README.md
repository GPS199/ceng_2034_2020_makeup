# ceng_2034_2020_makeup

1) Create a new child process with syscall and print its PID. (5 pts)

2) Multi Threading: Child process should do the following: 

● Download the files via the given URL list. Should use multi threading for retrieving the files. Create n threads if there are n different elements in the url (10pts) 

● Child process should check its status; that means if it understands that it is orphan, it should then remove the downloaded files at the system and then exit (10pts).  
 
3) Multiprocessing (40 pts Total) 

● Check the system and learn the number of CPU cores. Create n processes if there are n cores. (10 pts) 

● Use processes for the correct task! 

● Control duplicate files within the downloaded files of your python code. You should do it by using multi processing techniques. 
(Hint: you can use hashlib -md5/sha256- in python to check file checksum) (10 pts)

● The main process should check the other created  processes and if takes more than 30 seconds, kill those processes (by sending signal from the main process) (10 pts) 

● The main process should check If the other processes didn't end successfully, then it should try again that process's job. (10 pts) 

4) Think about the previous questions. Your script should: 

a. Check available memory of the system. (5 pts)

b. Estimate what should be the minimum required memory. (5 pts) 

c. Include the routine that will wait until the system frees that memory. (5 pts).

d. Take a movie file (> 1GB) in your disk and try to hash it. How can you handle when hashing files that don't fit in the memory? (BONUS - 10 pts) 
 
5) Write a report on what you did and you learnt during the assignment (20 points)  

● You should use this template and write the report by using Latex. https://www.overleaf.com/read/zqcfzrfkphfb  

● You should define the methods that you have written

● You should explain the results and conclusion 
 
 
Notes: 

● If your final exam repo exists on the github then create a new branch name “makeup”. 
If it does not exist, open a repo (github.com/username/ceng_2034_2020_makeup) and write your github user name in the document report. Also write it in the 
following address:

https://docs.google.com/spreadsheets/d/1r3YwfK6vYWgs7Oy6qFOiG-Zzqj3_QFcbvu _XNyWaelM/edit?usp=sharing  

● Ensure that this repo is kept private until the deadline!  

● We will take your code from your GitHub, so you should have it there and we should see your progress from the commits. 

● Upload your code to your github account.

● Don’t use static variables in the assignment code. Make sure that it can be run on any machine. 

● Make sure that your script runs according to system characteristics (cpu core, memory). 

● All of the codes should be available in only one file, there shouldn’t be a 3rd party dependency.

● At the top of the source code; add (comment) your name, surname.

● You will upload the assignment on dys.mu.edu.tr. Please use only zip format to compression (no rar!) 
