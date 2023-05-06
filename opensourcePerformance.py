import time
import psutil

pid =  ''  # Get the process object for the program with the specified PID

    
interval = 60
num_repeats = 5
try:
    process = psutil.Process(pid)

    def measure_performance():
            cpu_usage = psutil.cpu_percent(interval=interval, percpu=None)

            mem_usage_percent = process.memory_percent()
            mem_tomegabytes = psutil.Process(pid).memory_info().rss / (1024 ** 2)

            start_time = time.time()
            end_time = time.time()
            latency = end_time - start_time

            return {
                "cpu_usage(%)": cpu_usage,
                "mem_usage(%)": mem_usage_percent,
                "mem_tomegabytes": mem_tomegabytes,
                "latency": latency
            }

    for i in range(num_repeats):
        print("Simulation", i + 1)
        if (i + 1 <= num_repeats):
            performance_metrics = measure_performance()
            print(performance_metrics)
            continue
        else:
            break
except psutil.NoSuchProcess:
    print(f"No process found with PID {pid}. Exiting...")
