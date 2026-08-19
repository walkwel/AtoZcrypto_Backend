"""The Academy curriculum: fifteen modules across five phases, ~20 hours.

Each module lives in its own file so a single module can be edited, reviewed or
replaced without touching the rest. This package assembles them in reading
order; `CURRICULUM` order *is* the order readers see, and each module's
`position` is derived from its index here rather than stored per file — so
reordering the programme is a change in one place.

Content is seeded into the database (see `courses/seed.py`) rather than served
from here: once seeded, editors own it through the admin panel, and re-running
the seed will not overwrite their edits.
"""

from app.modules.courses.curriculum.m01_foundations import MODULE as M01
from app.modules.courses.curriculum.m02_exchanges import MODULE as M02
from app.modules.courses.curriculum.m03_wallets import MODULE as M03
from app.modules.courses.curriculum.m04_market_structure import MODULE as M04
from app.modules.courses.curriculum.m05_orders import MODULE as M05
from app.modules.courses.curriculum.m06_charts import MODULE as M06
from app.modules.courses.curriculum.m07_setups import MODULE as M07
from app.modules.courses.curriculum.m08_indicators import MODULE as M08
from app.modules.courses.curriculum.m09_fundamentals import MODULE as M09
from app.modules.courses.curriculum.m10_onchain import MODULE as M10
from app.modules.courses.curriculum.m11_macro import MODULE as M11
from app.modules.courses.curriculum.m12_risk import MODULE as M12
from app.modules.courses.curriculum.m13_psychology import MODULE as M13
from app.modules.courses.curriculum.m14_strategy import MODULE as M14
from app.modules.courses.curriculum.m15_portfolio import MODULE as M15
from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec

CURRICULUM: list[ModuleSpec] = [
    M01,
    M02,
    M03,
    M04,
    M05,
    M06,
    M07,
    M08,
    M09,
    M10,
    M11,
    M12,
    M13,
    M14,
    M15,
]


def total_minutes() -> int:
    """Reading time for the whole programme."""
    return sum(module.minutes for module in CURRICULUM)


def total_lessons() -> int:
    return sum(len(module.lessons) for module in CURRICULUM)


__all__ = ["CURRICULUM", "LessonSpec", "ModuleSpec", "total_lessons", "total_minutes"]
