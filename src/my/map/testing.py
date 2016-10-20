# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import my.map


class MyMapLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=my.map)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'my.map:default')


MY_MAP_FIXTURE = MyMapLayer()


MY_MAP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MY_MAP_FIXTURE,),
    name='MyMapLayer:IntegrationTesting'
)


MY_MAP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MY_MAP_FIXTURE,),
    name='MyMapLayer:FunctionalTesting'
)


MY_MAP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MY_MAP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MyMapLayer:AcceptanceTesting'
)
