=========
FCKEditor
=========

Initialize::
    >>> from zope.testbrowser.wsgi import Browser
    >>> browser = Browser(wsgi_app=layer.make_wsgi_app())

Initlally Broken Pages
======================

There are some pages which are just plain broken. Assert we have fixed those::

    >>> browser.open(
    ...    'http://localhost:8080/@@/gocept.fckeditor/'
    ...    'editor/filemanager/browser/default/frmresourceslist.html')
    >>> print (browser.contents)
    <!DOCTYPE ...
    >>> browser.open(
    ...    'http://localhost:8080/@@/gocept.fckeditor/'
    ...    'editor/filemanager/browser/default/frmfolders.html')
    >>> print (browser.contents)
    <!DOCTYPE ...
