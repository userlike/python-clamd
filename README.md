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
pip install git+https://github.com/userlike/python-clamd.git
```

## Usage

```python
import clamd
from io import BytesIO

# Connect via network
cd = clamd.ClamdNetworkSocket(host='127.0.0.1', port=3310)

# Ping the daemon
cd.ping() # Returns "PONG", otherwise raises ConnectionError or ResponseError

# Scan content using instream (recommended - works with remote ClamAV)
result = cd.instream(BytesIO(b'file content here'))
# Returns: {'stream': ('OK', None)} for clean files
# Returns: {'stream': ('FOUND', 'VirusName')} for infected files

# Scan a file by path (only works if ClamAV can access the path)
cd.scan('/path/to/file')

# Get version info
cd.version()
```

## Disclaimer

**USE AT YOUR OWN RISK.** This software is provided "as is", without warranty of any kind, express or implied. The authors and maintainers do not guarantee the correctness, reliability, or functionality of this package. We shall not be held liable for any damages, losses, or consequences arising from the use of this software. Please review the source code before using it in any production or critical environment.

## License

LGPL - See the original [python-clamd](https://github.com/graingert/python-clamd) for details.

