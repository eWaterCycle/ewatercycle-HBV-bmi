from pathlib import Path

import numpy as np
from HBV import HBV

TEST_CONFIG = str(Path(__file__).parent / "data" / "config.json")

def test_full_run():
    model = HBV()
    model.initialize(TEST_CONFIG)

    for _ in range(3):
        model.update()
    discharge = model.get_value("Q", np.array([0.]))
    assert discharge > 0.01

    model.update_until(model.get_end_time())

    model.finalize()

test_full_run()