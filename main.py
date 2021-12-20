from server.scheduler import Scheduler
from server.socket_server import SocketServer
from multiprocessing import Process


def scheduler_server():
    scheduler = Scheduler()
    scheduler.dev_dispatch()


def socker_server():
    socket_server = SocketServer('192.168.31.104', 8081)
    socket_server.run()


def main():
    p = Process(target=socker_server)
    p.start()
    p = Process(target=scheduler_server)
    p.start()


if __name__ == '__main__':
    main()
