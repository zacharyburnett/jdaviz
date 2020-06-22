from warnings import warn

from ipyvuetify import VuetifyTemplate
from glue.core import HubListener

__all__ = ['TemplateMixin']


class TemplateMixin(VuetifyTemplate, HubListener):
    def __new__(cls, *args, **kwargs):
        """
        Overload object creation so that we can inject a reference to the
        ``Hub`` class before components can be initialized. This makes it so
        hub references on plugins can be passed along to components in the
        call to the initialization method.
        """
        obj = super().__new__(cls, *args, **kwargs)
        obj._app = kwargs.pop('app', None)

        return obj

    @property
    def app(self):
        warn(DeprecationWarning('The usage `.app` from a jdaviz application is'
                                ' deprecated and should be replaced by '
                                '`.glueapp` to prevent confusion with other '
                                'meanings of "app"'))
        return self._app

    @property
    def glueapp(self):
        return self._app

    @property
    def hub(self):
        return self._app.session.hub

    @property
    def session(self):
        return self._app.session

    @property
    def data_collection(self):
        return self._app.session.data_collection
