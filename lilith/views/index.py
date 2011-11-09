# Copyright 2011 posativ <info@posativ.org>. All rights reserved.
# License: BSD Style, 2 clauses. see lilith.py
# -*- encoding: utf-8 -*-

from lilith.views import View
from lilith.utils import render, mkfile

from jinja2 import Template
from os.path import normpath, join

filters = []
path = '/page/'
items_per_page = 10
paginating = True
enabled = True

class Index(View):
    
    def __init__(self, env):
        pass
        
    def __call__(self, request):
        """Creates nicely paged listing of your posts.  First page is the
        index.hml used to have this nice url: http://yourblog.com/ with a recent
        list of your (e.g. summarized) Posts. Other pages are enumerated to /page/n+1

        required:
        items_per_page -- posts displayed per page (defaults to 6)
        entry.html -- layout of Post's entry
        main.html -- layout of the website
        """
        conf = request['conf']
        env = request['env']
        entrylist = request['entrylist']
        ipp = items_per_page

        tt_entry = Template(env['tt_entry'])
        tt_main = Template(env['tt_main'])

        entrylist = [render(tt_entry, conf, env, entry, type="page") for entry in entrylist]

        for i, mem in enumerate([entrylist[x*ipp:(x+1)*ipp] for x in range(len(entrylist)/ipp+1)]):

            html = render(tt_main, conf, env, type='page', page=i+1,
                        entrylist='\n'.join(mem), num_entries=len(entrylist))
            directory = conf['output_dir']
            if i > 0:
                directory += (path + str(i+1))
                
            p = join(normpath(directory), 'index.html')
            mkfile(html, {'title': '/' if i==0 else (path+str(i+1))}, p)
