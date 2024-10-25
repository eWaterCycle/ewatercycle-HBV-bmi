from pathlib import Path
from HBV import HBV

TEST_CONFIG = str(Path(__file__).parent / "data" / "config.json")

def test_full_run():
    model = HBV()
    model.initialize(TEST_CONFIG)

    model.update_until(model.get_end_time())

    model.finalize()
