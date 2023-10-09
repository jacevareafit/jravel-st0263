# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: files.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='files.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x66iles.proto\"\x0e\n\x0c\x45mptyMessage\" \n\x11PingFilesResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t\"2\n\x11ListFilesResponse\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"\'\n\x13\x44ownloadFileRequest\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\"*\n\x14\x44ownloadFileResponse\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\"H\n\x11UploadFileRequest\x12\x12\n\x08\x66ileName\x18\x01 \x01(\tH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x42\t\n\x07request2\xd9\x01\n\x05\x46iles\x12.\n\tPingFiles\x12\r.EmptyMessage\x1a\x12.PingFilesResponse\x12.\n\tListFiles\x12\r.EmptyMessage\x1a\x12.ListFilesResponse\x12=\n\x0c\x44ownloadFile\x12\x14.DownloadFileRequest\x1a\x15.DownloadFileResponse0\x01\x12\x31\n\nUploadFile\x12\x12.UploadFileRequest\x1a\r.EmptyMessage(\x01\x62\x06proto3'
)




_EMPTYMESSAGE = _descriptor.Descriptor(
  name='EmptyMessage',
  full_name='EmptyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=29,
)


_PINGFILESRESPONSE = _descriptor.Descriptor(
  name='PingFilesResponse',
  full_name='PingFilesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='PingFilesResponse.ack', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=63,
)


_LISTFILESRESPONSE = _descriptor.Descriptor(
  name='ListFilesResponse',
  full_name='ListFilesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='ListFilesResponse.files', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='ListFilesResponse.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=115,
)


_DOWNLOADFILEREQUEST = _descriptor.Descriptor(
  name='DownloadFileRequest',
  full_name='DownloadFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='DownloadFileRequest.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=156,
)


_DOWNLOADFILERESPONSE = _descriptor.Descriptor(
  name='DownloadFileResponse',
  full_name='DownloadFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_data', full_name='DownloadFileResponse.chunk_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=200,
)


_UPLOADFILEREQUEST = _descriptor.Descriptor(
  name='UploadFileRequest',
  full_name='UploadFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='UploadFileRequest.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_data', full_name='UploadFileRequest.chunk_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='request', full_name='UploadFileRequest.request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=202,
  serialized_end=274,
)

_UPLOADFILEREQUEST.oneofs_by_name['request'].fields.append(
  _UPLOADFILEREQUEST.fields_by_name['fileName'])
_UPLOADFILEREQUEST.fields_by_name['fileName'].containing_oneof = _UPLOADFILEREQUEST.oneofs_by_name['request']
_UPLOADFILEREQUEST.oneofs_by_name['request'].fields.append(
  _UPLOADFILEREQUEST.fields_by_name['chunk_data'])
_UPLOADFILEREQUEST.fields_by_name['chunk_data'].containing_oneof = _UPLOADFILEREQUEST.oneofs_by_name['request']
DESCRIPTOR.message_types_by_name['EmptyMessage'] = _EMPTYMESSAGE
DESCRIPTOR.message_types_by_name['PingFilesResponse'] = _PINGFILESRESPONSE
DESCRIPTOR.message_types_by_name['ListFilesResponse'] = _LISTFILESRESPONSE
DESCRIPTOR.message_types_by_name['DownloadFileRequest'] = _DOWNLOADFILEREQUEST
DESCRIPTOR.message_types_by_name['DownloadFileResponse'] = _DOWNLOADFILERESPONSE
DESCRIPTOR.message_types_by_name['UploadFileRequest'] = _UPLOADFILEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyMessage = _reflection.GeneratedProtocolMessageType('EmptyMessage', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMESSAGE,
  '__module__' : 'files_pb2'
  # @@protoc_insertion_point(class_scope:EmptyMessage)
  })
_sym_db.RegisterMessage(EmptyMessage)

PingFilesResponse = _reflection.GeneratedProtocolMessageType('PingFilesResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGFILESRESPONSE,
  '__module__' : 'files_pb2'
  # @@protoc_insertion_point(class_scope:PingFilesResponse)
  })
_sym_db.RegisterMessage(PingFilesResponse)

ListFilesResponse = _reflection.GeneratedProtocolMessageType('ListFilesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESRESPONSE,
  '__module__' : 'files_pb2'
  # @@protoc_insertion_point(class_scope:ListFilesResponse)
  })
_sym_db.RegisterMessage(ListFilesResponse)

DownloadFileRequest = _reflection.GeneratedProtocolMessageType('DownloadFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADFILEREQUEST,
  '__module__' : 'files_pb2'
  # @@protoc_insertion_point(class_scope:DownloadFileRequest)
  })
_sym_db.RegisterMessage(DownloadFileRequest)

DownloadFileResponse = _reflection.GeneratedProtocolMessageType('DownloadFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADFILERESPONSE,
  '__module__' : 'files_pb2'
  # @@protoc_insertion_point(class_scope:DownloadFileResponse)
  })
_sym_db.RegisterMessage(DownloadFileResponse)

UploadFileRequest = _reflection.GeneratedProtocolMessageType('UploadFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADFILEREQUEST,
  '__module__' : 'files_pb2'
  # @@protoc_insertion_point(class_scope:UploadFileRequest)
  })
_sym_db.RegisterMessage(UploadFileRequest)



_FILES = _descriptor.ServiceDescriptor(
  name='Files',
  full_name='Files',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=277,
  serialized_end=494,
  methods=[
  _descriptor.MethodDescriptor(
    name='PingFiles',
    full_name='Files.PingFiles',
    index=0,
    containing_service=None,
    input_type=_EMPTYMESSAGE,
    output_type=_PINGFILESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListFiles',
    full_name='Files.ListFiles',
    index=1,
    containing_service=None,
    input_type=_EMPTYMESSAGE,
    output_type=_LISTFILESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadFile',
    full_name='Files.DownloadFile',
    index=2,
    containing_service=None,
    input_type=_DOWNLOADFILEREQUEST,
    output_type=_DOWNLOADFILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadFile',
    full_name='Files.UploadFile',
    index=3,
    containing_service=None,
    input_type=_UPLOADFILEREQUEST,
    output_type=_EMPTYMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILES)

DESCRIPTOR.services_by_name['Files'] = _FILES

# @@protoc_insertion_point(module_scope)
