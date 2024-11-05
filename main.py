import requests
from os import getenv
from apscheduler.schedulers.blocking import BlockingScheduler


URL = getenv("URL", "https://archlinux.org/,https://neovim.io/") # Comma separated URLs
OPSGENIE = bool(int(getenv("OPSGENIE", "0"))) # 0 (disabled) or 1 (enabled)

WORKER_INTERVAL_HOURS = int(getenv("WORKER_INTERVAL_HOURS ", "0"))
WORKER_INTERVAL_MINUTES = int(getenv("WORKER_INTERVAL_MINUTES ", "0"))
WORKER_INTERVAL_SECONDS = int(getenv("WORKER_INTERVAL_SECONDS ", "10"))


def send_opsgenie(texto: str):
    pass # TODO: SEND OPSGENIE


def alarm(msg: str = "TODO ESTA BIEN"):
    print(msg) # TODO: SEND OPSGENIE
    if OPSGENIE == "1":
        send_opsgenie(msg)


def todo_esta_bien() -> bool:
    for url in URL.split(","):
        response = requests.get(url)
        if response.status_code != 200:
            return False
    return True

    
def main():
    print("Revisando si todo esta bien...")
    if todo_esta_bien():
        alarm()
    else:
        print("Algo no esta bien")


if __name__ == "__main__":
    print("Starting worker")
    scheduler = BlockingScheduler()
    scheduler.add_job(main, "interval", hours=WORKER_INTERVAL_HOURS, minutes=WORKER_INTERVAL_MINUTES, seconds=WORKER_INTERVAL_SECONDS)
    scheduler.start()
