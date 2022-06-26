import argparse
import logging
import os
import signal
import sys
from concurrent import futures

import grpc
from loguru import logger

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASE_DIR)
from proto import user_pb2_grpc
from user_srv.handler.user import UserServicer


def on_exit(signo, frame):
    logger.info("Terminating Thread...")
    sys.exit(0)


def serve():
    # args parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", nargs="?", type=str, default="127.0.0.1", help="binding ip")
    parser.add_argument("--port", nargs="?", type=int, default=50051, help="the listening port")
    args = parser.parse_args()

    logger.add("logs/user_srv_{time}.log")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port(f"{args.ip}:{args.port}")

    # signal disconnection for main thread
    signal.signal(signal.SIGINT, on_exit)
    signal.signal(signal.SIGTERM, on_exit)

    logger.info(f"Sever started: {args.ip}:{args.port}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
