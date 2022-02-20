#! /bin/bash
prog=`basename $0`
execdir=`dirname $0`
[ "$execdir" = "" -o "$execdir" = "." ] && execdir=$PWD

source $execdir/env.sh
cd $execdir

dcop=
case "$1" in
    start)
        dcop="up -d"
        ;;
    stop)
        dcop="down"
        ;;
    "")
        echo ${prog}: Missing command argument
        echo Usage: $prog start\|stop
        exit 1
        ;;
    *)
        echo ${prog}: Unrecognized command: $1 1>&2
        exit 1
        ;;
esac

echo '+' docker-compose $dcop
exec docker-compose $dcop


