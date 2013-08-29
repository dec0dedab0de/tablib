# -*- coding: utf-8 -*-

""" Tablib - TSV (Tab Separated Values) Support.
"""

from tablib.compat import is_py3, StringIO


title = 'mediawiki'
#extensions = ('tsv',)

DEFAULT_ENCODING = 'utf-8'

def export_set(dataset):
    """Returns a mediawiki table representation of Dataset."""
    #
    #stream = StringIO()
    rows = []
    if dataset.headers:
        headerline = "!" + "!!".join(header for header in dataset.headers) + "!"
        rows.append(headerline)
    for row in dataset:
        rowline = "|" + "||".join(cell for cell in row)
        rows.append(rowline)
    
    return '{| class="wikitable"\r\n' + '\r\n|-\r\n'.join(rows) + '\r\n|}'
#
#def import_set(dset, in_stream, headers=True):
#    """Returns dataset from TSV stream."""
#
#    dset.wipe()
#
#    if is_py3:
#        rows = csv.reader(in_stream.splitlines(), delimiter='\t')
#    else:
#        rows = csv.reader(in_stream.splitlines(), delimiter='\t',
#                          encoding=DEFAULT_ENCODING)
#
#    for i, row in enumerate(rows):
#        # Skip empty rows
#        if not row:
#            continue
#
#        if (i == 0) and (headers):
#            dset.headers = row
#        else:
#            dset.append(row)
#
#
#def detect(stream):
#    """Returns True if given stream is valid TSV."""
#    try:
#        csv.Sniffer().sniff(stream, delimiters='\t')
#        return True
#    except (csv.Error, TypeError):
#        return False
