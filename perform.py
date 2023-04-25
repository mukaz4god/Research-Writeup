import os
import time
import psutil
import requests
#from scapy.all import *

# Define the target web server URL
target_url = "192.168.151.139"

# Define the IP address of the machine launching the DoS attack
attacker_ip = "192.168.151.163"
attacker_username ="root";
attacker_password ="";

# Define the parameters for the simulated DoS attack
# hping3_command = f"sudo hping3 -S --flood -p 80 {target_url}"
# scapy_command = f"sudo python3 ./scapy_attack.py {target_url}"

# Define the time interval for measuring performance metrics
interval = 30

# Define the number of times to repeat the simulation
num_repeats = 3

# Define a function to launch the simulated DoS attack
#def launch_dos_attack():
    # Launch the hping3 command in the background on the attacker machine
   # os.system(f"ssh qhast@{attacker_ip} '{hping3_command}' &")

    # Launch the scapy command in the background on the attacker machine
    #  os.system(f"ssh {attacker_ip} '{scapy_command}' &")

# Define a function to stop the simulated DoS attack
#def stop_dos_attack():
    # Kill the hping3 and scapy processes on the attacker machine
  #  os.system(f"ssh qhast@{attacker_ip} 'sudo pkill -f hping3'")
    # os.system(f"ssh {attacker_ip} 'sudo pkill -f scapy'")

# Define a function to measure performance metrics
def measure_performance():
    # Measure CPU and memory usage of Snort and Suricata
  #  snort_cpu_usage = psutil.cpu_percent(interval=interval, percpu=True, process_name="snort")
 #  suricata_cpu_usage = psutil.cpu_percent(interval=interval, percpu=True, process_name="suricata")
    #snort_mem_usage = psutil.Process(psutil.pids()[psutil.pids().index(psutil.Process().pid)-1]).memory_info().rss / (1024 ** 2)
   # snort_mem_usage = psutil.Process(3609).memory_info().rss / (1024 ** 2)
    suricata_mem_usage = psutil.Process(5895).memory_info().rss / (1024 ** 2)
    # #suricata_mem_usage = psutil.Process(psutil.pids()[psutil.pids().index(psutil.Process().pid)-2]).memory_info().rss / (1024 ** 2)

    # Measure latency and response time of the web server
    start_time = time.time()
   # response = requests.get(target_url)
   # response = requests.get(target_url, auth=(attacker_username, attacker_password))
    end_time = time.time()
    latency = end_time - start_time
  #  response_time = response.elapsed.total_seconds()

    # Return the performance metrics as a dictionary
    return {
     #   "snort_cpu_usage": snort_cpu_usage,
    #    "suricata_cpu_usage": suricata_cpu_usage,
     #   "snort_mem_usage": snort_mem_usage,
        "suricata_mem_usage": suricata_mem_usage,
        "latency": latency,
     #   response_time": response_time
    }

# Repeat the simulation and measure performance metrics
for i in range(num_repeats):
    print("Simulation", i+1)
  #  launch_dos_attack()
    time.sleep(interval)
    performance_metrics = measure_performance()
  #  stop_dos_attack()
    print(performance_metrics)
