#Chapter 3 review  Questions#
### Name: Jiaxing Liu###
### Course: 5143 Operating Systems ###
### Date: Feb 29 2016 ###
_______________________________

## Question 1##
  Process preemption occurs when an executing process is interrupted by the processor so that another process can be executed
  
## Question 2##
  Swapping involves moving part or all of a process from main memory to disk. When none of the processes in main memory is in the Ready state, the operating system swaps one of the blocked processes out onto disk into a suspend queue, so that another process may be brought into main memory to execute.
  
## Question 3##
-Process identification
-processor state information
-process control information

## Question 4##
The user mode has restrictions on the instructions that can be executed and the memory areas that can be accessed. This is to protect the operating system from damage or alteration. In kernel mode, the operating system does not have these restrictions, so that it can perform its tasks.

## Question 5##
An interrupt is due to some sort of event that is external to and independent of the currently running process, such as the completion of an I/O operation. A trap relates to an error or exception condition generated within the currently running process, such as an illegal file access attempt.

## Question 6##
-Clock interrupt
-I/O interrupt
-Memory fault

## Question 7##
A mode switch may occur without changing the state of the process that is currently in the Running state. A process switch involves taking the currently executing process out of the Running state in favor of another process. The process switch involves saving more state information

