from cmlibs.zinc.context import Context
from cmlibs.zinc.result import RESULT_OK
from src.query_structure import query_branches
import os
import unittest


here = os.path.abspath(os.path.dirname(__file__))


class VagusSSVTestCase(unittest.TestCase):

    def test_query_branches(self):
        """
        Get positions and orientations of branches from a test subject-specific-vagus SSV.
        Uses a simple test scaffold, but any vagus scaffold output by SPARC Mapping Tools
        Scaffold Creator, including from REVA data should work.
        """
        data_file = os.path.join(here, "resources", "vagus_test_scaffold1.exf")
        context = Context("Test")
        region = context.getDefaultRegion()
        self.assertEqual(RESULT_OK, region.readFile(data_file))
        branch_info, common_branch_map = query_branches(region)
        print(branch_info)
        print(common_branch_map)


if __name__ == "__main__":
    unittest.main()
