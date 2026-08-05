"""MkDocs hook: expõe iac/*.json como assets estáticos do build.

Copia cada arquivo de iac/ (raiz do repo) para site/iac-data/ e gera
site/iac-data/index.json com a lista de slugs disponíveis, para a página
docs/iac-viewer.md consumir via fetch. Não duplica os arquivos dentro de
docs/ — a cópia acontece só no momento do build (on_post_build).
"""

import json
import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    repo_root = Path(config.config_file_path).parent
    iac_dir = repo_root / "iac"
    out_dir = Path(config["site_dir"]) / "iac-data"
    out_dir.mkdir(parents=True, exist_ok=True)

    slugs = []
    if iac_dir.is_dir():
        for json_path in sorted(iac_dir.glob("*.json")):
            shutil.copy2(json_path, out_dir / json_path.name)
            slugs.append(json_path.stem)

    (out_dir / "index.json").write_text(
        json.dumps(slugs, ensure_ascii=False, indent=2)
    )
