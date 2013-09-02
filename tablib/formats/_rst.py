# -*- coding: utf-8 -*-

""" Tablib - TSV (Tab Separated Values) Support.
"""

from tablib.compat import is_py3, StringIO
import os


title = 'rst'
#extensions = ('tsv',)

DEFAULT_ENCODING = 'utf-8'
def makerow(row, widths):
    '''takes a row and the list of widths, returns a joined string in the correct format'''
    return '  '.join([makecell(cell, widths[i])for i, cell in enumerate(row)])


def makecell(cell,width):
    return "{0:^{1}}".format(cell, width)


def export_set(dataset):
    """Returns a ReStructuredText simple table representation of Dataset."""
    #get the width of each column, 
    #maybe this should be moved to within the dataset class. 
    columnwidths = []
    for i in range(dataset.width):
        widest = max((len(str(item)) for item in dataset.get_col(i)))
        if dataset.headers:
            widest = max(widest, len(str(dataset.headers[i])))
        columnwidths.append(widest)
        
    outputlines = []
    separator = '  '.join(['=' * cw for cw in columnwidths])
    outputlines.append(separator)
    if dataset.headers:
        outputlines.append(makerow(dataset.headers,columnwidths))
        outputlines.append(separator)
    for row in dataset:
        outputlines.append(makerow(row,columnwidths))
    outputlines.append(separator)
    
    return os.linesep.join(outputlines)
    #stream = StringIO()


