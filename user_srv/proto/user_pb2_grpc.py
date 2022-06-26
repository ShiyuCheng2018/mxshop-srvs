# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from . import user_pb2 as user__pb2


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserList = channel.unary_unary(
            '/User/GetUserList',
            request_serializer=user__pb2.PageInfo.SerializeToString,
            response_deserializer=user__pb2.UserListResponse.FromString,
        )
        self.GetUserByMobile = channel.unary_unary(
            '/User/GetUserByMobile',
            request_serializer=user__pb2.MobileRequest.SerializeToString,
            response_deserializer=user__pb2.UserInfoResponse.FromString,
        )
        self.GetUserById = channel.unary_unary(
            '/User/GetUserById',
            request_serializer=user__pb2.IdRequest.SerializeToString,
            response_deserializer=user__pb2.UserInfoResponse.FromString,
        )
        self.CreateUser = channel.unary_unary(
            '/User/CreateUser',
            request_serializer=user__pb2.CreateUserInfo.SerializeToString,
            response_deserializer=user__pb2.UserInfoResponse.FromString,
        )
        self.UpdateUser = channel.unary_unary(
            '/User/UpdateUser',
            request_serializer=user__pb2.UpdateUserInfo.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUserList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByMobile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetUserList': grpc.unary_unary_rpc_method_handler(
            servicer.GetUserList,
            request_deserializer=user__pb2.PageInfo.FromString,
            response_serializer=user__pb2.UserListResponse.SerializeToString,
        ),
        'GetUserByMobile': grpc.unary_unary_rpc_method_handler(
            servicer.GetUserByMobile,
            request_deserializer=user__pb2.MobileRequest.FromString,
            response_serializer=user__pb2.UserInfoResponse.SerializeToString,
        ),
        'GetUserById': grpc.unary_unary_rpc_method_handler(
            servicer.GetUserById,
            request_deserializer=user__pb2.IdRequest.FromString,
            response_serializer=user__pb2.UserInfoResponse.SerializeToString,
        ),
        'CreateUser': grpc.unary_unary_rpc_method_handler(
            servicer.CreateUser,
            request_deserializer=user__pb2.CreateUserInfo.FromString,
            response_serializer=user__pb2.UserInfoResponse.SerializeToString,
        ),
        'UpdateUser': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateUser,
            request_deserializer=user__pb2.UpdateUserInfo.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUserList(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/User/GetUserList',
                                             user__pb2.PageInfo.SerializeToString,
                                             user__pb2.UserListResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByMobile(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/User/GetUserByMobile',
                                             user__pb2.MobileRequest.SerializeToString,
                                             user__pb2.UserInfoResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserById(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/User/GetUserById',
                                             user__pb2.IdRequest.SerializeToString,
                                             user__pb2.UserInfoResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/User/CreateUser',
                                             user__pb2.CreateUserInfo.SerializeToString,
                                             user__pb2.UserInfoResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/User/UpdateUser',
                                             user__pb2.UpdateUserInfo.SerializeToString,
                                             google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
