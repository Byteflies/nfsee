#!/usr/bin/env python3

import nfc

def on_connect(tag):
    print(f"Tag activated")

    if tag.ndef is None:
        print("No NDEF message found")
    else:
        print("Records:")
        for record in tag.ndef.records:
            print(f"{record.type}: {record.data.decode()}")
    print()
    return True

print("Opening contactless USB reader")
with nfc.ContactlessFrontend('usb') as clf:
    print("Contactless USB reader opened, waiting for tag activation\n")
    while True:
        connect = clf.connect(
            rdwr={
                "targets": ["106A"],
                "on-connect": on_connect,
                "beep-on-connect": False,
            },
        )
        if not connect:
            break
