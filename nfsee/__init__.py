#!/usr/bin/env python3

import nfc

def on_connect(tag):
    print(f"Tag activated", end="")

    if tag.ndef is None:
        print(", no NDEF message found")
    else:
        print(", records:")
        for record in tag.ndef.records:
            print(f"- {record.type}: {record.data.decode()}")
    print()
    return True

def main():
    print("Opening contactless USB reader")
    with nfc.ContactlessFrontend('usb') as clf:
        print("Contactless USB reader opened, waiting for tag activation\n")
        while True:
            connect = clf.connect(
                rdwr={
                    "targets": ["106A"],
                    "on-connect": on_connect,
                    "beep-on-connect": True,
                },
            )
            if not connect:
                break

if __name__ == "__main__":
    main()
