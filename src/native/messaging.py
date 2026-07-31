"""Native Messaging protocol helpers.

Chrome frames every Native Messaging message with a 4-byte little-endian
length prefix followed by a UTF-8 JSON payload.
"""

import json
import struct

_LENGTH_FORMAT = "=I"
_LENGTH_SIZE = struct.calcsize(_LENGTH_FORMAT)


def read_message(stream):
    header = stream.read(_LENGTH_SIZE)
    if not header:
        return None
    (length,) = struct.unpack(_LENGTH_FORMAT, header)
    payload = stream.read(length)
    return json.loads(payload.decode("utf-8"))


def write_message(stream, message):
    payload = json.dumps(message).encode("utf-8")
    stream.write(struct.pack(_LENGTH_FORMAT, len(payload)))
    stream.write(payload)
    stream.flush()
