#!/usr/bin/env python3

import os
from sys import argv
import multiprocessing
import subprocess


PROCESS_LIMIT = multiprocessing.cpu_count()
VALID_EXTENSIONS = {'wav', 'm4a'}

def get_outfile_path(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise ValueError(f'file {file_path} not found')
    fn, ext = os.path.splitext(file_path)
    ext = ext[1:]
    if ext not in VALID_EXTENSIONS:
        raise ValueError(f'expected extension in {VALID_EXTENSIONS}, got {ext} file')
    out_path = f'{fn}.mp3'
    print(out_path)
    if os.path.exists(out_path):
        raise ValueError(f'{out_path} exists already')
    return out_path


def cvt_single_wav(io_tup):
    infile, outfile = io_tup
    subprocess.run([
        '/usr/bin/ffmpeg', '-i', infile, '-vn', '-ar', '44100',
        '-ac', '2',
        '-b:a', '320k',
        outfile
    ])


def main():
    argc = len(argv)
    if argc < 2:
        raise ValueError('expected at least 1 input')
    out_paths = (get_outfile_path(p) for p in argv[1:])
    par_args = list(zip(argv[1:], out_paths))
    p: multiprocessing.Pool = multiprocessing.Pool(min(PROCESS_LIMIT, argc - 1))
    p.map(cvt_single_wav, par_args)


if __name__ == '__main__':
    main()
