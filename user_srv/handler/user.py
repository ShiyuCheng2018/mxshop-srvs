import time

import grpc
from loguru import logger
from peewee import DoesNotExist

from user_srv.model.models import User
from user_srv.proto import user_pb2, user_pb2_grpc


class UserServicer(user_pb2_grpc.UserServicer):

    def convert_user_to_rsp(self, user):
        user_info_response = user_pb2.UserInfoResponse()
        user_info_response.id = user.id
        user_info_response.name = user.name
        user_info_response.mobile = user.mobile
        user_info_response.gender = user.gender
        user_info_response.birthday = user.birthday
        user_info_response.role = user.role

        if user.nickname:
            user_info_response.nickname = user.nickname
        if user.gender:
            user_info_response.gender = user.gender
        if user.birthday:
            user_info_response.birthday = int(time.mktime(user.birthday.timetuple()))
        return user_info_response

    @logger.catch
    def GetUserList(self, request: user_pb2.PageInfo, context):
        response = user_pb2.UserListResponse()
        users = User.select()
        response.total = users.count()

        start = 0
        per_page_nums = 10
        if request.size:
            per_page_nums = request.size
        if request.page:
            start = per_page_nums * (request.page - 1)

        users = users.limit(per_page_nums).offset(start)

        for user in users:
            response.data.append(self.convert_user_to_rsp(user))

        return response

    @logger.catch
    def GetUserById(self, request: user_pb2.IdRequest, context):
        try:
            user = User.get(User.id == request.id)
            return self.convert_user_to_rsp(user)

        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found.")
            return user_pb2.UserInfoResponse()

    @logger.catch
    def GetUserByMobile(self, request: user_pb2.MobileRequest, context):
        try:
            user = User.get(User.mobile == request.mobile)
            return self.convert_user_to_rsp(user)

        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found.")
            return user_pb2.UserInfoResponse()
