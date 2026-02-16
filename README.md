# python-clamd-fork

A Python client for ClamAV daemon (clamd).

## About

This is a fork of the original [python-clamd](https://github.com/graingert/python-clamd) library.

### Why this fork?

- **Modernization** — Updated to use modern Python packaging and practices
- **Cleanup** — Removed deprecated code and legacy Python 2 compatibility layers
- **Maintenance** — Cleaned up outdated dependencies and build tooling

## Requirements

- Python 3.10+
- ClamAV daemon running

## Installation

```bash
pip install python-clamd-fork
```

## Usage

```python
import clamd

# Connect via Unix socket
cd = clamd.ClamdUnixSocket()

# Or connect via network
cd = clamd.ClamdNetworkSocket(host='127.0.0.1', port=3310)

# Ping the daemon
cd.ping()

# Scan a file
cd.scan('/path/to/file')

# Get version info
cd.version()
```

## License

LGPL - See the original [python-clamd](https://github.com/graingert/python-clamd) for details.

