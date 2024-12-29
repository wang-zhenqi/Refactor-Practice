import json

import pytest

from production_plan.province import Province
from utils import project_root


def sample_province_data():
    with open(project_root / "resources" / "production_plan" / "province_data.json", "r") as f:
        return json.load(f)


@pytest.fixture
def asia():
    return Province(sample_province_data())
