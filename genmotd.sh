#!/bin/sh

CONFDIR=/share/programs/etc/motd
export CONFDIR

OUTFILE="./motd"

echo "File autogenerated by $PWD/$0 on $(date)" > ${OUTFILE}
/opt/rh/rh-python36/root/usr/bin/python3 $CONFDIR/genmotd.py $CONFDIR/motd.xml >> ${OUTFILE}
