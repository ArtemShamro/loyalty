# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: stats.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'stats.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bstats.proto\x12\x05posts\"6\n\x0fGetCountRequest\x12\x12\n\ntargetType\x18\x01 \x01(\t\x12\x0f\n\x07post_id\x18\x02 \x01(\x05\"#\n\x10GetCountResponse\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x05\"&\n\x07\x44\x61yData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\"9\n\x12GetDynamicsRequest\x12\x12\n\ntargetType\x18\x01 \x01(\t\x12\x0f\n\x07post_id\x18\x02 \x01(\x05\"6\n\x13GetDynamicsResponse\x12\x1f\n\x07\x64\x61yData\x18\x01 \x03(\x0b\x32\x0e.posts.DayData\"7\n\x12GetTopPostsRequest\x12\x12\n\ntargetType\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\"7\n\x12GetTopUsersRequest\x12\x12\n\ntargetType\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\"-\n\x10TopStatsResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05\"8\n\x0eGetTopResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.posts.TopStatsResponse\"&\n\x13GetPostStatsRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\x05\"F\n\x14GetPostStatsResponse\x12\r\n\x05views\x18\x01 \x01(\x05\x12\x10\n\x08\x63omments\x18\x02 \x01(\x05\x12\r\n\x05likes\x18\x03 \x01(\x05\x32\xdc\x02\n\x0cStatsService\x12;\n\x08GetCount\x12\x16.posts.GetCountRequest\x1a\x17.posts.GetCountResponse\x12\x44\n\x0bGetDynamics\x12\x19.posts.GetDynamicsRequest\x1a\x1a.posts.GetDynamicsResponse\x12?\n\x0bGetTopPosts\x12\x19.posts.GetTopPostsRequest\x1a\x15.posts.GetTopResponse\x12?\n\x0bGetTopUsers\x12\x19.posts.GetTopUsersRequest\x1a\x15.posts.GetTopResponse\x12G\n\x0cGetPostStats\x12\x1a.posts.GetPostStatsRequest\x1a\x1b.posts.GetPostStatsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETCOUNTREQUEST']._serialized_start=22
  _globals['_GETCOUNTREQUEST']._serialized_end=76
  _globals['_GETCOUNTRESPONSE']._serialized_start=78
  _globals['_GETCOUNTRESPONSE']._serialized_end=113
  _globals['_DAYDATA']._serialized_start=115
  _globals['_DAYDATA']._serialized_end=153
  _globals['_GETDYNAMICSREQUEST']._serialized_start=155
  _globals['_GETDYNAMICSREQUEST']._serialized_end=212
  _globals['_GETDYNAMICSRESPONSE']._serialized_start=214
  _globals['_GETDYNAMICSRESPONSE']._serialized_end=268
  _globals['_GETTOPPOSTSREQUEST']._serialized_start=270
  _globals['_GETTOPPOSTSREQUEST']._serialized_end=325
  _globals['_GETTOPUSERSREQUEST']._serialized_start=327
  _globals['_GETTOPUSERSREQUEST']._serialized_end=382
  _globals['_TOPSTATSRESPONSE']._serialized_start=384
  _globals['_TOPSTATSRESPONSE']._serialized_end=429
  _globals['_GETTOPRESPONSE']._serialized_start=431
  _globals['_GETTOPRESPONSE']._serialized_end=487
  _globals['_GETPOSTSTATSREQUEST']._serialized_start=489
  _globals['_GETPOSTSTATSREQUEST']._serialized_end=527
  _globals['_GETPOSTSTATSRESPONSE']._serialized_start=529
  _globals['_GETPOSTSTATSRESPONSE']._serialized_end=599
  _globals['_STATSSERVICE']._serialized_start=602
  _globals['_STATSSERVICE']._serialized_end=950
# @@protoc_insertion_point(module_scope)
