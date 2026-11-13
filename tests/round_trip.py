#!/usr/bin/env python3
"""Round-trip test: encode then decode a file with lzfse and compare checksums."""

import hashlib
import os
import subprocess
import sys
import tempfile


def sha256(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    lzfse_cli, input_path = sys.argv[1], sys.argv[2]

    with tempfile.TemporaryDirectory() as tmp_dir:
        compressed = os.path.join(tmp_dir, 'compressed.lzfse')
        decompressed = os.path.join(tmp_dir, 'decompressed')

        subprocess.run([lzfse_cli, '-encode', '-i', input_path, '-o', compressed], check=True)
        subprocess.run([lzfse_cli, '-decode', '-i', compressed, '-o', decompressed], check=True)

        if sha256(input_path) != sha256(decompressed):
            sys.exit(f'round-trip mismatch for {input_path}')


if __name__ == '__main__':
    main()
