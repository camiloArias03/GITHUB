import time
import threading

def set_alarm(duration):
  time.sleep(duration)
  print("¡Despertar!")
def main():
  duration = int(input("Ingresa la duración de la alarma en segundos: "))
  thread = threading.Timer(duration, set_alarm, [duration])
  thread.start()
  print("Alarma programada para sonar en {} segundos".format(duration))

if __name__ == "__main__":
  main()
