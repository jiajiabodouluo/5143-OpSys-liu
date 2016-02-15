#Chapter 2 review  Questions#
### Name: Jiaxing Liu###
### Course: 5143 Operating Systems ###
### Date: 14 Feb 2016 ###
_______________________________

## Question 1##
  - Convenience: An OS makes a computer more convenient to use.
  - Efficiency: An OS allows the computer system resources to be used in an efficient manner.
  - Ability to evolve: An OS should be constructed in such a way as to permit the effective development, testing, and introduction of new system functions without interfering with service.
  
## Question 2##
   The kernel is a portion of the operating system that includes the most heavily used portions of software. Generally, the kernel is maintained permanently in main memory. The kernel runs in a privileged mode and responds to calls from processes and interrupts from devices.

## Question 3##
   Multiprogramming is a mode of operation that provides for the interleaved execution of two or more computer programs by a single processor.
  
## Question 4##
- A process is a program in execution. 
- An instance of a program running on a computer. 
- The entity that can be assigned to and executed on a processor.
- A unit of activity characterized by a single sequential thread of execution, a current state, and an associated set of system resources. 

## Question 5##
The execution context, or process state,is the internal data by which the OS is able to supervise and control the process. This internal information is separated from the process, because the operating system has information not permitted to the process. The context includes all of the information that the operating system needs to manage the process and that the processor needs to execute the process properly. The context includes the contents of the various processor registers, such as the program counter and data registers. It also includes information of use to the operating system, such as the priority of the process and whether the process is waiting for the completion of a particular I/O event.

## Question 6##
- Process isolation: The operating system must prevent independent processes from interfering with each other's memory, both data and instructions.
- Automatic allocation and management: Programs should be dynamically allocated across the memory hierarchy as required. Allocation should be transparent to the programmer. Thus, the programmer is relieved of concerns relating to memory limitations, and the operating system can achieve efficiency by assigning memory to jobs only as needed.
- Support of modular programming: Programmers should be able to define program modules, and to create, destroy, and alter the size of modules dynamically.
- Protection and access control: Sharing of memory, at any level of the memory hierarchy, creates the potential for one program to address the memory space of another. This is desirable when sharing is needed by particular applications. At other times, it threatens the integrity of programs and even of the operating system itself. The operating system must allow portions of memory to be accessible in various ways by various users.
- Long-term storage: Many application programs require means for storing information for extended periods of time, after the computer has been powered down.

## Question 7##
- A virtual address refers to a memory location in virtual memory. That location is on disk and at some times in main memory.
- A real address is an address in main memory

## Question 8##
Round robin is a scheduling algorithm in which processes are activated in a fixed cyclic order; that is, all processes are in a circular queue. A process that cannot proceed because it is waiting for some event

## Question 9##
- A monolithic kernel is a large kernel containing virtually the complete operating system, including scheduling, file system, device drivers, and memory management. All the functional components of the kernel have access to all of its internal data structures and routines. Typically, a monolithic kernel is implemented as a single process, with all elements sharing the same address space. 
- A microkernel is a small privileged operating system core that provides process scheduling, memory management, and communication services and relies on other processes to perform some of the functions traditionally associated with the operating system kernel.

## Question 10##
Multithreading is a technique in which a process, executing an application, is divided into threads that can run concurrently.

## Question 11##
- Simultaneous concurrent processes or threads.
- Scheduling.
- Synchronization.
- Memory management.
- Reliability and fault tolerance.
