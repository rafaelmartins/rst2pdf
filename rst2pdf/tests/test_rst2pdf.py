# -*- coding: utf-8 -*-
#$HeadURL$
#$LastChangedDate$
#$LastChangedRevision$
from unittest import TestCase, makeSuite
from pyPdf import PdfFileReader
import cStringIO

from docutils.core import publish_doctree

import rst2pdf
from utils import *

import pdb
#import pdb; pdb.set_trace()

def input_file_path(file):
    return join(PREFIX, 'input', file)

class FullGenerationTests(TestCase):
    """ broken since createPdf is no longer a function
    """
    def test_bullet_chars_full(self):
        self.output=cStringIO.StringIO()
        input_file = input_file_path('test_bullet_chars.txt')
        input=open(input_file,'r').read()
        createPdf(text=input, output=self.output, styleSheet=None)
        self.output.seek(0)
        result = PdfFileReader(self.output)
        text_result = result.getPage(0).extractText()
        self.assertEqual(text_result, u'\nTest\nItem 1\nItem 2\n')
        


    
class GenerationTests(rst2pdfTests):

    def test_bullet_chars(self):
        input_file = input_file_path('test_bullet_chars.txt')
        input=open(input_file,'r').read()
        doctree=publish_doctree(input)
        elements=self.converter.gen_elements(doctree,0)
        self.assertEqual(len(elements), 4)
        self.assertEqual(elements[1].text, 'Test')
        self.assertEqual(elements[2]._cellvalues[0][0][0].text, 'Item 1')
        self.assertEqual(elements[2]._cellvalues[0][0][0].bulletText, u'\u2022')
        self.assertEqual(elements[3]._cellvalues[0][0][0].text, 'Item 2')
        self.assertEqual(elements[3]._cellvalues[0][0][0].bulletText, u'\u2022')
        
    def test_transition(self):
        input="""
Transitions
-----------

Here's a transition:

---------

It divides the section.
"""
        doctree=publish_doctree(input)
        elements=self.converter.gen_elements(doctree,0)
        self.assertEqual(len(elements), 5)
        assert(isinstance(elements[3],rst2pdf.flowables.Separation))
        
    def test_strong(self):
        input="""
**strong**"""
        doctree=publish_doctree(input)
        elements=self.converter.gen_elements(doctree,0)
        self.assertEqual(len(elements), 1)
        para = elements[0]
        self.assertEqual(para.text, '<b>strong</b>')
        parafrag = para.frags[0]
        self.assertEqual(parafrag.bold, 1)
        
    def test_emphasis(self):
        input="""
*emphasis*"""
        doctree=publish_doctree(input)
        elements=self.converter.gen_elements(doctree,0)
        self.assertEqual(len(elements), 1)
        para = elements[0]
        self.assertEqual(para.text, '<i>emphasis</i>')
        parafrag = para.frags[0]
        self.assertEqual(parafrag.italic, 1)
        # pdb.set_trace()
        
    def test_raw_pagebreak(self):
        input="""
One page

.. raw:: pdf

   PageBreak

Another page.
"""
        doctree=publish_doctree(input)
        elements=self.converter.gen_elements(doctree,0)
        self.assertEqual(len(elements), 3)
        pagebreak = elements[1]
        self.assertEqual(pagebreak.__class__, rst2pdf.flowables.MyPageBreak)
        #pdb.set_trace()
        
        
def test_suite():
    suite = makeSuite(GenerationTests)
    return suite
    
if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')