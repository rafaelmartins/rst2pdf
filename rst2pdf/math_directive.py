# -*- coding: utf-8 -*-
# See LICENSE.txt for licensing terms

from docutils.parsers import rst
from docutils.parsers.rst import directives
from docutils.nodes import General, Inline, Element
from docutils import utils
from docutils.parsers.rst import roles

import basenodehandler, math_flowable

if 'Directive' in rst.__dict__:

    class Math(rst.Directive):
        has_content = True
        required_arguments = 0
        optional_arguments = 1
        final_argument_whitespace = True
        option_spec = {
            'label': directives.unchanged,
            'nowrap': directives.flag,
        }

        def run(self):
            latex = '\n'.join(self.content)
            if self.arguments and self.arguments[0]:
                latex = self.arguments[0] + '\n\n' + latex
            return [math_node(latex=latex,
                              rawsource=''.join(self.content))]

        def __repr__(self):
            return u''.join(self.content)

else:

    def Math(name, arguments, options, content, lineno,
            content_offset, block_text, state, state_machine):
        return [math_node(latex=''.join(content), rawsource=''.join(content))]

    Math.content = True

directives.register_directive('math', Math)


class math_node(General, Inline, Element):
    children = ()

    def __init__(self, rawsource='', *children, **attributes):
        self.rawsource = rawsource
        self.math_data = attributes['latex']
        Element.__init__(self, rawsource, *children, **attributes)


def math_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    latex = utils.unescape(text, restore_backslashes=True)
    return [math_node(latex, latex=latex)], []


roles.register_local_role('math', math_role)

class HandleMath(basenodehandler.NodeHandler, math_node):
    def gather_elements(self, client, node, style):
        return [math_flowable.Math(node.math_data)]

    def get_text(self, client, node, replaceEnt):
        mf = math_flowable.Math(node.math_data)
        w, h = mf.wrap(0, 0)
        descent = mf.descent()
        img = mf.genImage()
        client.to_unlink.append(img)
        return '<img src="%s" width=%f height=%f valign=%f/>' % (
            img, w, h, -descent)

