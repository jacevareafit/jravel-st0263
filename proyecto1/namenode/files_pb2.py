# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: files.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x66iles.proto\"\x0e\n\x0c\x45mptyMessage\"\x1f\n\rStatusMessage\x12\x0e\n\x06status\x18\x01 \x01(\x05\" \n\x11PingFilesResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t\"2\n\x11ListFilesResponse\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"\'\n\x13\x44ownloadFileRequest\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\"*\n\x14\x44ownloadFileResponse\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\"H\n\x11UploadFileRequest\x12\x12\n\x08\x66ileName\x18\x01 \x01(\tH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x42\t\n\x07request\".\n\x0fNameNodeRequest\x12\x0c\n\x04\x63onn\x18\x01 \x01(\t\x12\r\n\x05\x66iles\x18\x02 \x03(\t\"0\n\x10\x44\x61taNodeResponse\x12\x0c\n\x04\x63onn\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"#\n\x12SearchFilesRequest\x12\r\n\x05regex\x18\x01 \x01(\t2\xbc\x03\n\x05\x46iles\x12.\n\tPingFiles\x12\r.EmptyMessage\x1a\x12.PingFilesResponse\x12.\n\tListFiles\x12\r.EmptyMessage\x1a\x12.ListFilesResponse\x12=\n\x0c\x44ownloadFile\x12\x14.DownloadFileRequest\x1a\x15.DownloadFileResponse0\x01\x12\x31\n\nUploadFile\x12\x12.UploadFileRequest\x1a\r.EmptyMessage(\x01\x12\x30\n\x0cNamenodeConn\x12\x10.NameNodeRequest\x1a\x0e.StatusMessage\x12?\n\x14NamenodeDownloadFile\x12\x14.DownloadFileRequest\x1a\x11.DataNodeResponse\x12\x36\n\x12NamenodeUploadFile\x12\r.EmptyMessage\x1a\x11.DataNodeResponse\x12\x36\n\x0bSearchFiles\x12\x13.SearchFilesRequest\x1a\x12.ListFilesResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'files_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTYMESSAGE']._serialized_start=15
  _globals['_EMPTYMESSAGE']._serialized_end=29
  _globals['_STATUSMESSAGE']._serialized_start=31
  _globals['_STATUSMESSAGE']._serialized_end=62
  _globals['_PINGFILESRESPONSE']._serialized_start=64
  _globals['_PINGFILESRESPONSE']._serialized_end=96
  _globals['_LISTFILESRESPONSE']._serialized_start=98
  _globals['_LISTFILESRESPONSE']._serialized_end=148
  _globals['_DOWNLOADFILEREQUEST']._serialized_start=150
  _globals['_DOWNLOADFILEREQUEST']._serialized_end=189
  _globals['_DOWNLOADFILERESPONSE']._serialized_start=191
  _globals['_DOWNLOADFILERESPONSE']._serialized_end=233
  _globals['_UPLOADFILEREQUEST']._serialized_start=235
  _globals['_UPLOADFILEREQUEST']._serialized_end=307
  _globals['_NAMENODEREQUEST']._serialized_start=309
  _globals['_NAMENODEREQUEST']._serialized_end=355
  _globals['_DATANODERESPONSE']._serialized_start=357
  _globals['_DATANODERESPONSE']._serialized_end=405
  _globals['_SEARCHFILESREQUEST']._serialized_start=407
  _globals['_SEARCHFILESREQUEST']._serialized_end=442
  _globals['_FILES']._serialized_start=445
  _globals['_FILES']._serialized_end=889
# @@protoc_insertion_point(module_scope)
