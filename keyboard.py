#!/usr/bin/env python

import struct
import os

infile_path = "/dev/input/by-id/usb-SONiX_USB_FS_Keyboard-event-kbd"

# struct input_event {
#     struct timeval time;
#     unsigned short type;
#     unsigned short code;
#     unsigned int value;
# };

EVENT_FORMAT = "llHHI"; # long, long, unsigned short, unsigned short, unsigned int
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

with open(infile_path, "rb") as file:
    event = file.read(EVENT_SIZE)
    prev_sec = 0
    while event:
        (tv_sec, tv_usec, type, code, value) = struct.unpack(EVENT_FORMAT, event)
        # print struct.unpack(EVENT_FORMAT, event)
        event = file.read(EVENT_SIZE)
        if prev_sec != tv_sec:
            # print code
            if code == 96:
                os.system("/usr/bin/mocp -G")
            else:
                continue
            prev_sec = tv_sec
