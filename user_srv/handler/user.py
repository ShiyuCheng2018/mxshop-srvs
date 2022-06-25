import time

from user_srv.model.models import User
from user_srv.proto import user_pb2, user_pb2_grpc


class UserServicer(user_pb2_grpc.UserServicer):
    def GetUserList(self, request: user_pb2.PageInfo, context):
        response = user_pb2.UserListResponse()
        users = User.select()
        response.total = users.count()

        start = 0
        page = 1
        per_page_nums = 10
        if request.size:
            per_page_nums = request.size
        if request.page:
            start = per_page_nums * (page - 1)

        users = users.limit(per_page_nums).offset(start)

        for user in users:
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

            response.data.append(user_info_response)

        return response
