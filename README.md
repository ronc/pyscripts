pyscripts
=========

Random useful scripts

I ran across a problem recently where some set of tables in a MySQL db were
MyISAM and some other set were InnoDB. This caused foreign key problems when
connecting between the two.

inno.py is a simple little script for a Django environment that scans the table
types and sets any MyISAM tables to be InnoDB instead.
