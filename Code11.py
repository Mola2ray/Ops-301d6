#!/usr/bin/env python3
# Script: Ops301d6 Challenge-09
# Author: Lamin Touray
# Purpose: Create a Python script that fetches this information using Psutil:

# Time spent by normal processes executing in user mode
# Time spent by processes executing in kernel mode
# Time when system was idle
# Time spent by priority processes executing in user mode
# Time spent waiting for I/O to complete.
# Time spent for servicing hardware interrupts
# Time spent for servicing software interrupts
# Time spent by other operating systems running in a virtualized environment
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel




import psutil

# Time spent by normal processes executing in user mode
print("Time spent by normal processes executing in user mode:", psutil.cpu_times().user)

# Time spent by processes executing in kernel mode
print("Time spent by processes executing in kernel mode:", psutil.cpu_times().system)

# Time when system was idle
print("Time when system was idle:", psutil.cpu_times().idle)

# Time spent by priority processes executing in user mode
print("Time spent by priority processes executing in user mode:", psutil.cpu_times().nice)

# Time spent waiting for I/O to complete.
print("Time spent waiting for I/O to complete:", psutil.cpu_times().iowait)

# Time spent for servicing hardware interrupts
print("Time spent for servicing hardware interrupts:", psutil.cpu_times().irq)

# Time spent for servicing software interrupts
print("Time spent for servicing software interrupts:", psutil.cpu_times().softirq)

# Time spent by other operating systems running in a virtualized environment
print("Time spent by other operating systems running in a virtualized environment:", psutil.cpu_times().steal)

# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", psutil.cpu_times().guest)
#End


# Source: chatGPT