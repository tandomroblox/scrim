# -*- coding: utf-8 -*-
import os
from importlib.machinery import SourceFileLoader

# Load config.cfg if it exists (local use)
try:
    cfg = SourceFileLoader('cfg', 'config.cfg').load_module()
except Exception:
    class DummyCfg:
        pass
    cfg = DummyCfg()

# Load version
with open('.version', 'r') as f:
    __version__ = f.read().strip()

# =========================
# ENVIRONMENT OVERRIDES
# =========================

# Discord Bot Token
if hasattr(cfg, "DC_TOKEN"):
    cfg.DC_TOKEN = os.getenv("DC_TOKEN", cfg.DC_TOKEN)
else:
    cfg.DC_TOKEN = os.getenv("DC_TOKEN")

# Safety check
if not cfg.DC_TOKEN:
    raise RuntimeError(
        "DC_TOKEN is not set. "
        "Set it in config.cfg (local) or as an environment variable (Render)."
    )
