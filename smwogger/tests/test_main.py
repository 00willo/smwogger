import unittest

from smwogger.tests.support import set_args, coserver
from smwogger.main import main


WANTED = """\
Scanning spec... \x1b[92mOK\x1b[0m

\t\tThis is project 'ABSearch Server'
\t\tlightweight a/b testing tool for search options
\t\tVersion 0.3.0


Running Scenario from x-smoke-test
1:getHeartbeat... \x1b[92mOK\x1b[0m
2:addUserToCohort... \x1b[92mOK\x1b[0m
3:returnCohortSettings... \x1b[92mOK\x1b[0m"""


class TestMain(unittest.TestCase):

    def test_main(self):

        options = 'smwogger', 'http://localhost:8888/api.json'

        with coserver(), set_args(*options) as out:
            try:
                main()
            except SystemExit:
                pass

        stdout = out[0].read().strip()
        self.assertEqual(stdout, WANTED)
