import subprocess
import os
import signal

def start_server_on_port(port):
    try:
        subprocess.check_output(['lsof', '-i', f':{port}'])
        print('port already in use')

        # Находим pid процесса, занимающего порт
        output=subprocess.check_output(['lsof', '-ti', f':{port}']).decode().strip()

        if output:
            pid = int(output)
            print(f"Found process with pid: {pid}")

            os.kill(pid, signal.SIGKILL)
            print(f"Process with pid {pid} has been terminated.")

            print('search server again')

        else:
            print('port is free')
    except subprocess.CalledProcessError:
        # Если нет процессов на порту
        print(f"Starting server on port {port}...")

start_server_on_port(5000)