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


def success_response(result):
    return {"ok": True, "result": result}


def error_response(message):
    return {"ok": False, "error": message}


def validate_request(request):
    if not isinstance(request, dict):
        return "Request must be an object."
    command = request.get("command")
    if not isinstance(command, str) or not command:
        return "Request command must be a non-empty string."
    params = request.get("params", {})
    if not isinstance(params, dict):
        return "Request params must be an object."
    return None
