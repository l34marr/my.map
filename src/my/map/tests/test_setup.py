# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from my.map.testing import MY_MAP_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that my.map is properly installed."""

    layer = MY_MAP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if my.map is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'my.map'))

    def test_browserlayer(self):
        """Test that IMyMapLayer is registered."""
        from my.map.interfaces import (
            IMyMapLayer)
        from plone.browserlayer import utils
        self.assertIn(IMyMapLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MY_MAP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['my.map'])

    def test_product_uninstalled(self):
        """Test if my.map is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'my.map'))

    def test_browserlayer_removed(self):
        """Test that IMyMapLayer is removed."""
        from my.map.interfaces import IMyMapLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMyMapLayer, utils.registered_layers())
