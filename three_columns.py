from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree


def makeExtension(*args, **kwargs):
    return ThreeColumnExtension(*args, **kwargs)


THREECOL = r'(\%\d\d{0,1}\s[^\%]+)(\%\d\d{0,1}\s[^\%]+|.*)(\%\d\d{0,1}\s[^\%]+|.*)(\%\d\d{0,1}\s[^\%]+|.*)(\%\d\d{0,1}\s[^\%]+|.*)(\%\d\d{0,1}\s[^\%]+|.*)'


class ThreeColumnPattern(Pattern):
    def handleMatch(self, m):
        #line = m.string
        #self._set_columns(line)

        # row column
        el1 = etree.Element("div")
        el1.set('class', 'instruction bg-info row')

        groupnr=1
        match = self._get_group(m,groupnr)
        while match:
            print()
            groupnr+=1
            match = self._get_group(m,groupnr)
        for idx,match in m.group:
        # create the columns.
        #for idx, col in enumerate(self.cols):
            width, content = self._parse_column(col)
            _col = etree.SubElement(el1, "div")
            _col.set('class','col-md-{} col{}'.format(width,idx))
            _col.text = content

        return el1

    def _get_group(self,m,groupnr):
        match = m.group(groupnr)
        return match

    def _set_columns(self, line):
        self.cols = line.split('%')[1:]

    def _parse_column(self, column):
        width, content = column.split(maxsplit=1)
        return width, content.strip()

        # def _get_col_width(self, width):
        #     _width = width[-1]
        #     _col_width = "col-md-" + _width
        #     return _col_width


class ThreeColumnExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('threecolumn', ThreeColumnPattern(THREECOL), '<escape')
