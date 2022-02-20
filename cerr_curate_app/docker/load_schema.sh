#!/bin/bash
#
prog=`basename $0`
execdir=`dirname $0`
[ "$execdir" = "" -o "$execdir" = "." ] && execdir=$PWD
pkgdir=`dirname $execdir`
[ "$pkgdir" = "" -o "$pkgdir" = "." ] && pkgdir=$PWD
repodir=`dirname $pkgdir`

source $execdir/env.sh

export CERR_SCHEMA="$repodir/schemas/ce-res-md.xsd"
[ -z "$1" ] || CERR_SCHEMA="$1"

script="
from core_main_app.components.template.models import Template;
from core_main_app.components.template_version_manager.models import TemplateVersionManager;
import os;
fd = open(os.environ['CERR_SCHEMA']);
schemastr = fd.read();
t=Template(filename=os.path.basename(os.environ['CERR_SCHEMA']),content=schemastr,user=None,hash='xxxx').save();
v=TemplateVersionManager(title='registry schema',versions=[1],current=str(t.id)).save()
print(str(t.id))
"

cd $pkgdir
set -x
python manage.py shell -c "$script"
