import psutil

def battery_percent():

    return psutil.sensors_battery().percent

def network_info():
    stats = psutil.net_if_stats()

    return [
        {
            'network': key, 
            'up': "Up" if stats[key].isup else "Down", 
            'speed': stats[key].speed}
        for key in stats
    ]

def memory_info():
    # Fetch the memory information
    vm = psutil.virtual_memory()
    return {
        "total": vm.total,
        "used": vm.used,
        "available": vm.available,
        "percentage": vm.percent
    }

def process_info():

    processes = []

    for process in psutil.pids():

        # While fetching the processes, some of the subprocesses may exit
        # Hence we need to put this code in try-except block
        try:
            p = psutil.Process(process)
            processes.append({
                'pid': process,
                'name': p.name(),
                'status': p.status(),
                'cpu': str(p.cpu_percent())+"%",
                'num_threads': p.num_threads()
            })
        except psutil.NoSuchProcess:
            pass
        except psutil.AccessDenied:
            print("Warning: We just hit an Access Denied. Try running the app with admin/superuser priviledges")
            pass
        except Exception as e:
            raise e

    return processes

def main_channel():
    return {
        'battery': battery_percent(),
        'network': network_info(),
        'memory': memory_info(),
        'processor': process_info()
    }
