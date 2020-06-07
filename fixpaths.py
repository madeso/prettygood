#!/usr/bin/env python3
import argparse
import os.path
import os
import logging


logging.basicConfig(level=logging.WARNING, format="%(msg)s")
LOG = logging.getLogger('logger')


def rename(src, dst, args):
    if args.nop:
        print('not renaming', os.path.basename(src), os.path.basename(dst))
    else:
        print('renaming', src, dst)
        if os.path.exists(dst):
            LOG.error("ERROR: destination already exists")
            return
        try:
            os.rename(src, dst)
            print("source path renamed to destination path successfully.")
        except IsADirectoryError:
            LOG.error("ERROR: source is a file but destination is a directory.")
        except NotADirectoryError:
            LOG.error("ERROR: source is a directory but destination is a file.")
        except PermissionError:
            LOG.error("ERROR: rename operation not permitted")
        except OSError as error:
            LOG.error(error)


def replace_all(src, args):
    dst = src
    for c in args.invalid:
        dst = dst.replace(c, args.replace)
    if args.trim:
        dst = dst.strip()
    return dst


def run_file(f, args):
    folder, src = os.path.split(f)
    name_ext = os.path.splitext(src)
    dst = replace_all(name_ext[0], args) + name_ext[1]
    if src != dst:
        fp = os.path.join(folder, dst)
        rename(f, fp, args)
    else:
        LOG.debug('ok file {}'.format(src))


def run_directory(d, args):
    folder, src = os.path.split(d)
    dst = replace_all(src, args)
    target = os.path.join(folder, dst)
    if src != dst:
        rename(d, target, args)
    else:
        LOG.debug('dir {}'.format(src))
    if args.nop:
        target = d
    for f in os.listdir(target):
        run_file_or_directory(os.path.join(target, f), args)


def run_file_or_directory(f, args):
    if not os.path.exists(f):
        LOG.error('ERROR: does not exist: {}'.format(f))
    elif os.path.isfile(f):
        run_file(f, args)
    elif os.path.isdir(f):
        run_directory(f, args)
    else:
        LOG.error('ERROR: neither file nor directory: {}'.format(f))


def main():
    parser = argparse.ArgumentParser(description="rename files to 'safe' files")
    parser.add_argument('input', metavar='f', nargs='+', help='files or directories to rename')
    parser.add_argument('--nop', action='store_true', help="don't do anything")
    parser.add_argument('--verbose', action='store_true', help='verbose logging')
    parser.add_argument('--invalid', default='[]|#$%^?<>;:\\/"''')
    parser.add_argument('--replace', default='_', help='replace string')
    parser.add_argument('--no-trim', action='store_false', dest='trim', help="don't remove spaces at start and end")
    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    for a in args.input:
        run_file_or_directory(os.path.abspath(a), args)

if __name__ == "__main__":
    main()
