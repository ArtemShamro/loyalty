# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import stats_pb2 as stats__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in stats_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class StatsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCount = channel.unary_unary(
                '/posts.StatsService/GetCount',
                request_serializer=stats__pb2.GetCountRequest.SerializeToString,
                response_deserializer=stats__pb2.GetCountResponse.FromString,
                _registered_method=True)
        self.GetDynamics = channel.unary_unary(
                '/posts.StatsService/GetDynamics',
                request_serializer=stats__pb2.GetDynamicsRequest.SerializeToString,
                response_deserializer=stats__pb2.GetDynamicsResponse.FromString,
                _registered_method=True)
        self.GetTopPosts = channel.unary_unary(
                '/posts.StatsService/GetTopPosts',
                request_serializer=stats__pb2.GetTopPostsRequest.SerializeToString,
                response_deserializer=stats__pb2.GetTopResponse.FromString,
                _registered_method=True)
        self.GetTopUsers = channel.unary_unary(
                '/posts.StatsService/GetTopUsers',
                request_serializer=stats__pb2.GetTopUsersRequest.SerializeToString,
                response_deserializer=stats__pb2.GetTopResponse.FromString,
                _registered_method=True)
        self.GetPostStats = channel.unary_unary(
                '/posts.StatsService/GetPostStats',
                request_serializer=stats__pb2.GetPostStatsRequest.SerializeToString,
                response_deserializer=stats__pb2.GetPostStatsResponse.FromString,
                _registered_method=True)


class StatsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDynamics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTopPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTopUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPostStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCount,
                    request_deserializer=stats__pb2.GetCountRequest.FromString,
                    response_serializer=stats__pb2.GetCountResponse.SerializeToString,
            ),
            'GetDynamics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDynamics,
                    request_deserializer=stats__pb2.GetDynamicsRequest.FromString,
                    response_serializer=stats__pb2.GetDynamicsResponse.SerializeToString,
            ),
            'GetTopPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTopPosts,
                    request_deserializer=stats__pb2.GetTopPostsRequest.FromString,
                    response_serializer=stats__pb2.GetTopResponse.SerializeToString,
            ),
            'GetTopUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTopUsers,
                    request_deserializer=stats__pb2.GetTopUsersRequest.FromString,
                    response_serializer=stats__pb2.GetTopResponse.SerializeToString,
            ),
            'GetPostStats': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPostStats,
                    request_deserializer=stats__pb2.GetPostStatsRequest.FromString,
                    response_serializer=stats__pb2.GetPostStatsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'posts.StatsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('posts.StatsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StatsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/posts.StatsService/GetCount',
            stats__pb2.GetCountRequest.SerializeToString,
            stats__pb2.GetCountResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetDynamics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/posts.StatsService/GetDynamics',
            stats__pb2.GetDynamicsRequest.SerializeToString,
            stats__pb2.GetDynamicsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTopPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/posts.StatsService/GetTopPosts',
            stats__pb2.GetTopPostsRequest.SerializeToString,
            stats__pb2.GetTopResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTopUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/posts.StatsService/GetTopUsers',
            stats__pb2.GetTopUsersRequest.SerializeToString,
            stats__pb2.GetTopResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPostStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/posts.StatsService/GetPostStats',
            stats__pb2.GetPostStatsRequest.SerializeToString,
            stats__pb2.GetPostStatsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
