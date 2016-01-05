from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree


def makeExtension(*args, **kwargs):
    return ThreeColumnExtension(*args, **kwargs)


THREECOL = r'(\%\d)([^\%]+)(\%\d)([^\%^\n]+)(\%*\d*)([^\n]*)'


class ThreeColumnPattern(Pattern):
    def handleMatch(self, m):
        _col_width1 = m.group(2)
        _col_nr = m.group(3)
        _col_width2 = m.group(4)
        _text = m.group(5)
        _col_width3 = m.group(6)
        _image = m.group(7)

        # row column
        el1 = etree.Element("div")
        el1.set('class', 'instruction bg-info row')

        # first column

        col1 = etree.SubElement(el1, "div")
        col1.set('class', self._get_col_width(_col_width1) + ' col1')
        col1.text = _col_nr.strip()

        col2 = etree.SubElement(el1, "div")
        col2.set('class', self._get_col_width(_col_width2) + ' col2')
        col2.text = _text.strip()

        if _image == '':
            pass
        else:
            col3 = etree.SubElement(el1, "div")
            col3.set('class', self._get_col_width(_col_width3) + ' col3')
            col3.text = _image

        return el1

    def _get_col_width(self, width):
        _width = width[-1]
        _col_width = "col-md-" + _width
        return _col_width


class ThreeColumnExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('threecolumn', ThreeColumnPattern(THREECOL), '<escape')
