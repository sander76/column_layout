import re

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree


def makeExtension(*args, **kwargs):
    return ThreeColumnExtension(*args, **kwargs)


# THREECOL = r'(\%\d\d{0,1}\s[^\%]+)(\%\d\d{0,1}\s[^\%]+|.*)(\%\d\d{0,1}\s[^\%]+|.*)(\%\d\d{0,1}\s[^\%]+|.*)(\%\d\d{0,1}\s[^\%]+|.*)(\%\d\d{0,1}\s[^\%]+|.*)'
# THREECOL = r'\%\d\d{0,1}\s.*?\n'
THREECOL = r'(\%\d{1,2}\s[^\n]*)'
ALLCOLS = re.compile(r'\%(\d{1,2})\s(.+?)(?=\s\%\d|\Z)')


# ALLCOLS = re.compile(r"\%{1}(\d{1,2})")

class ThreeColumnPattern(Pattern):
    def handleMatch(self, m):
        line = m.group(2)
        self._set_columns(line)

        # row column
        el1 = etree.Element("div")
        el1.set('class', 'instruction bg-info row')

        # create the columns.
        for idx, column in enumerate(self.cols):
            width, content = column
            _col = etree.SubElement(el1, "div")
            _col.set('class', 'col-sm-{} col{}'.format(width, idx))
            _col.text = content

        return el1

    # def _get_group(self,m,groupnr):
    #     try:
    #         match = m.group(groupnr+2)  # first group match is group +2
    #         return match
    #     except IndexError:
    #         message = "error parsing: {}".format(m.string)
    #         raise IndexError(message)

    def _set_columns(self, line):
        _cols = re.findall(ALLCOLS, line)
        # _cols=re.split(ALLCOLS,line)
        self.cols = _cols

    def _parse_column(self, column):
        width, content = column.split(maxsplit=1)
        return width[1:], content.strip()

        # def _get_col_width(self, width):
        #     _width = width[-1]
        #     _col_width = "col-md-" + _width
        #     return _col_width


class ThreeColumnExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('threecolumn', ThreeColumnPattern(THREECOL), '<escape')
