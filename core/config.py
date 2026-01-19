# -*- coding: utf-8 -*-
import os
from importlib.machinery import SourceFileLoader

# =========================
# LOAD config.cfg (OPTIONAL)
# =========================
try:
    cfg = SourceFileLoader('cfg', 'config.cfg').load_module()
except Exception:
    class DummyCfg:
        pass
    cfg = DummyCfg()

# =========================
# LOAD VERSION SAFELY
# =========================
import os as _os
VERSION_FILE = _os.path.join(_os.path.dirname(__file__), '..', '.version')
try:
    with open(VERSION_FILE, 'r') as f:
        __version__ = f.read().strip()
except FileNotFoundError:
    __version__ = "unknown"

# =========================
# DEFAULT CONFIG VALUES
# =========================

# Logging
if not hasattr(cfg, "LOG_LEVEL"):
    cfg.LOG_LEVEL = "INFO"

# Discord owner (optional but used in permissions)
if not hasattr(cfg, "DC_OWNER_ID"):
    cfg.DC_OWNER_ID = 0

# Slash servers
if not hasattr(cfg, "DC_SLASH_SERVERS"):
    cfg.DC_SLASH_SERVERS = []

# =========================
# DISCORD BOT TOKEN
# =========================
if hasattr(cfg, "DC_BOT_TOKEN"):
    cfg.DC_BOT_TOKEN = os.getenv("DC_BOT_TOKEN", cfg.DC_BOT_TOKEN)
else:
    cfg.DC_BOT_TOKEN = os.getenv("DC_BOT_TOKEN")

if not cfg.DC_BOT_TOKEN:
    raise RuntimeError(
        "DC_BOT_TOKEN is not set. "
        "Set it in config.cfg (local) or as an environment variable (Render)."
    )
