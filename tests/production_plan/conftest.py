import json

import pytest

from utils import project_root


@pytest.fixture
def sample_province_data():
    with open(project_root / "resources" / "production_plan" / "province_data.json", "r") as f:
        return json.load(f)
