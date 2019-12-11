from os import path
from urllib import request
from zipfile import ZipFile

class StixShifterUtils():
    @staticmethod
    def load_module(external_modules):
        if external_modules is not None:
            external_links = external_modules
            if isinstance(external_links, str):
                external_links = [external_links]
            basepath = path.abspath(path.join( path.dirname(__file__), '..'))
            for link in external_links:
                filename = link[link.rfind("/")+1:]
                filepath = path.join(basepath, filename)
                request.urlretrieve(link, filepath)
                print('StixShifterUtils.load_module downloading {}'.format(link))
                with ZipFile(filepath, 'r') as zipObj:
                    zipObj.extractall(basepath)