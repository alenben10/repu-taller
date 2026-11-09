"""Genera navegando_phd.html (versión pública, sin notas del orador)
a partir de navegando_phd_con_notas.html (copia local, no se sube a GitHub).

Uso:  python3 hacer_publico.py
"""
import re
from pathlib import Path

here = Path(__file__).parent
src = (here / "navegando_phd_con_notas.html").read_text(encoding="utf-8")

out, n = re.subn(r'\s*<aside class="notes">.*?</aside>', "", src, flags=re.S)
replacements = [
    # ocultar el botón "N" y quitar el atajo de teclado
    ("#notesPanel{", "#bNotes,#notesPanel{display:none!important}\n#notesPanel{"),
    ("else if(k==='n'||k==='N'){ toggleNotes(); }", ""),
    (" · <kbd>N</kbd> notas", ""),
]
for old, new in replacements:
    assert out.count(old) >= 1, f"no encontrado: {old!r}"
    out = out.replace(old, new, 1)

assert 'class="notes"' not in out
(here / "navegando_phd.html").write_text(out, encoding="utf-8")
print(f"OK: {n} bloques de notas eliminados -> navegando_phd.html")
