# Copyright (c) 2007-2009 gocept gmbh & co. kg
# See also LICENSE.txt

import unittest
import gocept.fckeditor
import doctest

import zope.app.wsgi.testlayer


FCKEditorLayer = zope.app.wsgi.testlayer.BrowserLayer(
        gocept.fckeditor, name='FCKEditorLayer', allowTearDown=True)


def test_suite():
    suite = unittest.TestSuite()
    ftest = doctest.DocFileSuite(
        'README.txt',
        optionflags=(doctest.REPORT_NDIFF + doctest.NORMALIZE_WHITESPACE +
                     doctest.ELLIPSIS),
        globs={'layer': FCKEditorLayer})
    ftest.layer = FCKEditorLayer
    suite.addTest(ftest)
    return suite
