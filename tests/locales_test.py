import polib
from pathlib import Path
import logging

logger = logging.getLogger('TEST')
logger.setLevel('INFO')

LOCALES_DIR = Path(__file__).parent.parent
BASE_LOCALE = "en_US"
MODULES_DIR = LOCALES_DIR / BASE_LOCALE / "LC_MESSAGES"
EXCLUDED_LOCALES = {BASE_LOCALE, "tests"}

LOCALE_NAMES = [
    p.name for p in LOCALES_DIR.iterdir()
    if (
        p.is_dir()
        and not p.name.startswith(".")
        and p.name not in EXCLUDED_LOCALES
    )
]


def get_msgid_map(po_path):
    try:
        po = polib.pofile(str(po_path))
        return {entry.msgid: entry.linenum for entry in po if entry.msgid.strip()}
    except Exception as e:
        logger.error(f"Failed to parse {po_path}: {e}")
        return {}

def check_msgids_match(base_file, other_file, locale):
    base_msgids = get_msgid_map(base_file)
    other_msgids = get_msgid_map(other_file)

    base_set = set(base_msgids.keys())
    other_set = set(other_msgids.keys())

    errors = []

    extra = other_set - base_set
    if extra:
        formatted = "\n  ".join(
            f"[Line {other_msgids[msgid]}] {msgid}" for msgid in sorted(extra)
        )
        errors.append(f"{locale}/{other_file.name}: Extra msgids not in base:\n  {formatted}")

    missing = base_set - other_set
    if missing:
        formatted = "\n  ".join(
            f"[Line {base_msgids[msgid]}] {msgid}" for msgid in sorted(missing)
        )
        errors.append(f"{locale}/{other_file.name}: Missing msgids from base:\n  {formatted}")

    if list(base_msgids.keys()) != list(other_msgids.keys()):
        errors.append(f"{locale}/{other_file.name}: ⚠️ msgid order mismatch (non-critical)")

    return errors

def verify_translations() -> int:
    logger.info(f"Verifying msgid consistency across locales (base: {BASE_LOCALE})")

    all_ok = True

    for module_file in MODULES_DIR.glob("*.po"):
        module_name = module_file.name

        for locale in LOCALE_NAMES:
            other_po = LOCALES_DIR / locale / "LC_MESSAGES" / module_name

            if not other_po.exists():
                logger.warning(f"{locale}: Missing module file {module_name}")
                continue

            errors = check_msgids_match(module_file, other_po, locale)
            if errors:
                for err in errors:
                    logger.error(err)
                all_ok = False
            else:
                logger.info(f"{locale}/{module_name}: OK")

    if not all_ok:
        logger.error("One or more msgid mismatches found.")
        return 1

    logger.info("All msgid checks passed.")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(verify_translations())
