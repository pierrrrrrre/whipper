# -*- Mode: Python; test-case-name: morituri.test.test_common_config -*-
# vi:si:et:sw=4:sts=4:ts=4

import os
import tempfile

from morituri.common import config

from morituri.test import common as tcommon


class OffsetTestCase(tcommon.TestCase):

    def setUp(self):
        fd, self._path = tempfile.mkstemp(suffix=u'.morituri.test.config')
        os.close(fd)
        self._config = config.Config(self._path)

    def tearDown(self):
        os.unlink(self._path)

    def testAddReadOffset(self):
        self.assertRaises(KeyError,
            self._config.getReadOffset, 'PLEXTOR ', 'DVDR   PX-L890SA', '1.05')
        self._config.setReadOffset('PLEXTOR ', 'DVDR   PX-L890SA', '1.05', 6)

        # getting it from memory should work
        offset = self._config.getReadOffset('PLEXTOR ', 'DVDR   PX-L890SA',
            '1.05')
        self.assertEquals(offset, 6)

        # and so should getting it after reading it again
        self._config.open()
        offset = self._config.getReadOffset('PLEXTOR ', 'DVDR   PX-L890SA',
            '1.05')
        self.assertEquals(offset, 6)

    def testAddReadOffsetSpaced(self):
        self.assertRaises(KeyError,
            self._config.getReadOffset, 'Slimtype', 'eSAU208   2     ', 'ML03')
        self._config.setReadOffset('Slimtype', 'eSAU208   2     ', 'ML03', 6)

        # getting it from memory should work
        offset = self._config.getReadOffset(
            'Slimtype', 'eSAU208   2     ', 'ML03')
        self.assertEquals(offset, 6)

        # and so should getting it after reading it again
        self._config.open()
        offset = self._config.getReadOffset(
            'Slimtype', 'eSAU208   2     ', 'ML03')
        self.assertEquals(offset, 6)
