#!/usr/bin/env python
# coding: utf-8

import sys
from os import path

from bat import Bat
from util import console
from admin import Management

VIM_PATH = path.join(path.expanduser('~'), '.vim')

class CmdDispatcher(Management):

    def doinit(self, args):
        """intialize enviroment"""
        bat = Bat()
        bat.install_base()

    def doremove_all(self, args):
        """remove all scripts
        """
        bat = Bat()
        bat.remove_all()

    def doupdate_all(self, args):
        """update all scripts"""
        bat = Bat()
        bat.update_all()

    def dolist_installed(self, args):
        """list installed scripts"""
        bat = Bat()
        bat.list_installed()

    def doinstall(self, args):
        """install scripts"""
        scripts = args.scripts
        if len(scripts) >= 1:
            for index in xrange(0, len(scripts)):
                bat = Bat(scripts[index])
                bat.install()
        else:
             console('Please use `vimpyre install <script-name>` and try again!')

    def _setargsinstall(self):
        self.parser_install.add_argument('scripts', type=str, nargs='*', help='script1 script2 ...')

    def dosearch(self, args):
        """search script"""
        bat = Bat(args.script)
        rets = bat.search()

        console('=> => Send bats to search vim-scripts ...')
        if rets:
            for item in rets:
                if path.isdir(path.join(VIM_PATH, 'vimpyre', item['name'])):
                    console('\033[1m%s\033[m => %s \033[1m[installed]\033[m' % (item['name'].encode('utf-8'), item['description'].encode('utf-8')))
                else:
                    console('\033[1m%s\033[m => %s' % (item['name'].encode('utf-8'), item['description'].encode('utf-8')))
        else:
            console('No such vim-scripts!')

    def _setargssearch(self):
        self.parser_search.add_argument('script', type=str, help='script name')

    def doremove(self, args):
        """remove scripts"""
        scripts = args.scripts
        if len(scripts) >= 1:
            for index in xrange(0, len(scripts)):
                bat = Bat(scripts[index])
                bat.remove()
        else:
            console('Please use `vimpyre remove <script-name>` and try again!')

    def _setargsremove(self):
        self.parser_remove.add_argument('scripts', type=str, nargs='*', help='script1 script2 ...')

    def douninstall(self, args):
        """remove scripts"""
        self.doremove(args)

    def _setargsuninstall(self):
        self.parser_uninstall.add_argument('scripts', type=str, nargs='*', help='script1 script2 ...')

    def doupdate(self, args):
        """update scripts"""
        scripts = args.scripts
        if len(scripts) >= 1:
            for index in xrange(0, len(scripts)):
                bat = Bat(scripts[index])
                bat.update()
        else:
            console('Please use `vimpyre update <script-name>` and try again!')

    def _setargsupdate(self):
        self.parser_update.add_argument('scripts', type=str, nargs='*', help='script1 script2 ...')

    def dobrowse(self, args):
        """browse script's homepage in your web browser"""
        scripts = args.scripts
        if len(scripts) >= 1:
            for index in xrange(0, len(scripts)):
                bat = Bat(scripts[index])
                bat.open_homepage()
        else:
            console('Please use `vimpyre browse <script-name>` and try again!')

    def _setargsbrowse(self):
        self.parser_browse.add_argument('scripts', type=str, nargs='*', help='script1 script2 ...')

def main():
    import sys
    CmdDispatcher.douninstall_all = CmdDispatcher.doremove_all
    CmdDispatcher().run(sys.argv[1:])

if __name__ == '__main__':
    main()
