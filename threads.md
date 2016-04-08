#Threads questions#
### Name: Jiaxing Liu###
### Course: 5143 Operating Systems ###
### Date: 8 Mar 2016 ###
### M20227487 ###
_______________________________
## Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.##
   In thread2 , we used “global sharedCounter”, and “sharedCounter += 1” in both classes, it is a shared resource, it shows how many times the two threads run totally.

## After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?##
   Yes it fixed, we used threading.lock() instead of race condition. The downside is the thread3 runs so slowly. 
   
## Comment out the join statements at the bottom of the program and describe what happens.##
   If Comment out the join statements, and run the program. The two thread are still working after print out “Goodbye from the main program”. That means the main program terminates.
   
## What happens if you try to Ctrl-C out of the program before it terminates?##
   There is nothing happened. Program is still working.

## Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.##


## Does uncommenting the lock operations clear up the problem in question 5?##
   Yes it does. But the program runs very very slowly.
