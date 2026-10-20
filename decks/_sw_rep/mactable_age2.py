# -*- coding: utf-8 -*-
"""MACTABLE_AGE2 — та же инфографика, что mactable_age (повтор в лекции): переиспользуем вёрстку."""
import os
_f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mactable_age.py")
exec(compile(open(_f, encoding="utf-8").read(), _f, "exec"))
