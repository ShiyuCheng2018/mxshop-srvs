import grpc
from loguru import logger

from user_srv.proto import user_pb2_grpc, user_pb2


class UserTest:
    def __init__(self):
        # grpc server connection
        channel = grpc.insecure_channel("127.0.0.1:50051")
        self.stub = user_pb2_grpc.UserStub(channel)

    def user_list(self):
        response: user_pb2.UserListResponse = self.stub.GetUserList(user_pb2.PageInfo())
        logger.info(f"[user_list] total users: {response.total}")
        for user in response.data:
            print(user)

    def get_user_by_id(self, id):
        response: user_pb2.UserInfoResponse = self.stub.GetUserById(user_pb2.IdRequest(id))
        logger.info(f"[user info] {response}")

    def get_user_by_mobile(self, mobile):
        response: user_pb2.UserInfoResponse = self.stub.GetUserByMobile(user_pb2.MobileRequest(mobile))
        logger.info(f"[user info] {response}")


if __name__ == "__main__":
    user = UserTest()
    user.user_list()
