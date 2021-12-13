# Levo.ai's eBPF demonstration application

## System requirements
### General
* Root access.  (Most eBPF programs cannot be loaded by unprivileged users.)
* Working internet connection to download python dependencies for `tools/demo_server`
* Port 8080 available
* Compilers
  * Clang version 10 or newer
  * GCC version 10 or newer

### Debian / Ubuntu
* Other packages: `python3 python3-venv libelf-dev linux-libc-dev zlib1g-dev cmake make curl`

## Usage
`run.sh` will create a temporary directory, download the necessary Python dependencies,
build and launch the Levo eBPF demo API server and application, and clean up after itself
as it exits.

## NOTICE
Copyright (C) 2021 Levo Inc.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA