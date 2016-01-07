from markdown import markdown
from three_columns import ThreeColumnExtension

def test_output1():
    input = "%1 test1 %4 test 4 "
    txt = markdown(input,extensions=[ThreeColumnExtension()])
    assert txt == '<p>\n<div class="instruction bg-info row">\n<div class="col-md-1 col0">test1</div>\n<div class="col-md-4 col1">test 4 </div>\n</div>\n</p>'

def test_output2():
    input = "%1 test1 %4 value = 10%"
    txt = markdown(input,extensions=[ThreeColumnExtension()])
    assert txt == '<p>\n<div class="instruction bg-info row">\n<div class="col-md-1 col0">test1</div>\n<div class="col-md-4 col1">value = 10%</div>\n</div>\n</p>'

def test_output3():
    input = "%1 test1 %4 test 4 \n%1 test1 %4 test 4 "
    txt = markdown(input,extensions=[ThreeColumnExtension()])
    assert txt == '<p>\n<div class="instruction bg-info row">\n<div class="col-md-1 col0">test1</div>\n<div class="col-md-4 col1">test 4 </div>\n</div>\n</p>'
