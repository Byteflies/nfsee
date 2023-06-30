# nfsee

nfsee is a script to scan a NFC tag and show the NDEF records

## Installation

You will need Poetry to install the dependencies: https://python-poetry.org/docs/#installation.

```bash
poetry install
```

### macOS

Install libusb:

```
brew install libusb
```

It's possible macOS will claim the NFC reader device as soon as you plug it in, which means nfcpy will be unable to open it. If that's the case, you can try to remove and stop the relevant service:

```bash
sudo launchctl remove com.apple.ifdreader
sudo launchctl stop com.apple.ifdreader
```

## Usage

```bash
poetry run nfsee
```
