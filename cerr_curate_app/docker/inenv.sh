#! /bin/bash
prog=`basename $0`
execdir=`dirname $0`
[ "$execdir" = "" -o "$execdir" = "." ] && execdir=$PWD

source $execdir/env.sh
cd $execdir

exec "$@"
