#!/usr/bin/env python3
import argparse
import os.path
import os
import logging


logging.basicConfig(level=logging.WARNING, format="%(msg)s")
LOG = logging.getLogger('logger')


def rename(src, dst, nop):
    if nop:
        print('not renaming', src, dst)
    else:
        print('renaming', src, dst)
        os.rename(src, dst)
        try:
            os.rename(src, dst)
            print("source path renamed to destination path successfully.")
        except IsADirectoryError:
            LOG.error("source is a file but destination is a directory.")
        except NotADirectoryError:
            LOG.error("source is a directory but destination is a file.")
        except PermissionError:
            LOG.error("rename operation not permitted")
        except OSError as error:
            LOG.error(error)


def replace_all(src, invalid, replace):
    dst = src
    for c in invalid:
        dst = dst.replace(c, replace)
    return dst


def run_file(f, nop, invalid, replace):
    folder, src = os.path.split(f)
    name_ext = os.path.splitext(src)
    dst = replace_all(name_ext[0], invalid, replace) + name_ext[1]
    if src != dst:
        fp = os.path.join(folder, dst)
        rename(f, fp, nop)
    else:
        LOG.debug('ok file {}'.format(src))


def run_directory(d, nop, invalid, replace):
    folder, src = os.path.split(d)
    dst = replace_all(src, invalid, replace)
    target = os.path.join(folder, dst)
    if src != dst:
        rename(d, target, nop)
    else:
        LOG.debug('dir {}'.format(src))
    if nop:
        target = d
    for f in os.listdir(target):
        run_file_or_directory(os.path.join(d, f), nop, invalid, replace)


def run_file_or_directory(f, nop, invalid, replace):
    if not os.path.exists(f):
        LOG.error('ERROR: does not exist: {}'.format(f))
    elif os.path.isfile(f):
        run_file(f, nop, invalid, replace)
    elif os.path.isdir(f):
        run_directory(f, nop, invalid, replace)
    else:
        LOG.error('ERROR: neither file nor directory: {}'.format(f))


def main():
    parser = argparse.ArgumentParser(description="rename files to 'safe' files")
    parser.add_argument('input', metavar='f', nargs='+', help='files or directories to rename')
    parser.add_argument('--nop', action='store_true', help="don't do anything")
    parser.add_argument('--verbose', action='store_true', help='verbose logging')
    parser.add_argument('--invalid', default='?<>;:\\/"''')
    parser.add_argument('--replace', default='_', help='replace string')
    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    for a in args.input:
        run_file_or_directory(os.path.abspath(a), args.nop, args.invalid, args.replace)

if __name__ == "__main__":
    main()
