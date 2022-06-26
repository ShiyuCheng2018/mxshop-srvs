import logging
from concurrent import futures

import grpc
from loguru import logger

from proto import user_pb2_grpc
from user_srv.handler.user import UserServicer


def serve():
    logger.add("logs/user_srv_{time}.log")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:50051')
    logger.info(f"Sever started: 127.0.0.1:50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
