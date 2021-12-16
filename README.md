# Levo.ai's eBPF demonstration application

## Note
If you run into any problems or have any suggested edits to this README, 
especially system requirements for Linux distributions not already listed,
Please file an issue against this project in GitHub.

Questions are also welcome as GitHub issues.  And as we find time, we will
answer them and collect the most common ones into a `FAQ.md`.

## System requirements
### General
* Root access.  (Most eBPF programs cannot be loaded by unprivileged users.)
* Working internet connection to download python dependencies for `tools/demo_server`
* Port 8080 available
* Compilers
  * Clang version 10 or newer
  * GCC version 10 or newer

### Debian / Ubuntu / Kali
* Other packages: `cmake curl git libelf-dev libc6-dev linux-libc-dev make python3 python3-venv zlib1g-dev`

### Manjaro ###
`run.sh` appears to work "out of the box" without requiring any additional packages.

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

## References
### eBPF
* https://man7.org/linux/man-pages/man2/bpf.2.html
* https://man7.org/linux/man-pages/man7/bpf-helpers.7.html
### `libbpf`
* https://github.com/libbpf/libbpf/
* https://github.com/libbpf/libbpf/wiki/Libbpf:-the-road-to-v1.0
* https://github.com/libbpf/libbpf/wiki/Libbpf-1.0-migration-guide
* https://github.com/libbpf/libbpf-bootstrap
* https://nakryiko.com/posts/bpf-core-reference-guide/
### CMake
* https://cmake.org/cmake/help/latest/index.html
  * https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html
  * https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html
  * https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html