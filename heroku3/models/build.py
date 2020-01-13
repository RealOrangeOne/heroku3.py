from . import BaseResource, User
from .buildpack import Buildpack
from .slug import Slug
from .sourceblob import SourceBlob
import requests


class Build(BaseResource):
    _dates = ['created_at', 'updated_at']
    _strs = ['id', 'status', 'output_stream_url']
    _pks = ['id']
    _map = {'slug': Slug, 'source_blob': SourceBlob, 'user': User }
    _arrays = {'buildpacks': Buildpack }

    def __init__(self):
        super(Build, self).__init__()

    def __repr__(self):
        return "<build '{0} - {1}'>".format(self.id, self.status)

    def stream(self, timeout=None):
        r = requests.get(self.output_stream_url, verify=False, stream=True, timeout=timeout)
        return r.iter_lines()

    def get(self, timeout=None):
        r = requests.get(self.output_stream_url, verify=False, stream=True, timeout=timeout)
        return r.content.decode("utf-8")
