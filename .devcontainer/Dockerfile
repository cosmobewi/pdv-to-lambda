# Devcontainer for CLASS (xi_interact patch) + Cobaya + GetDist (+ MontePython optional)
FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1

# System deps
RUN apt-get update && apt-get install -y \
    git wget curl ca-certificates cmake pkg-config \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# --- External tools in /opt (hors workspace monté par VS Code) ---


# On place le patch dans /opt (il sera appliqué en postCreate pour éviter les collisions avec le bind-mount)
# Si ton patch est dans le repo local, VS Code le montera en /workspaces/<repo>/interacting_vacuum.diff
# et on l’utilisera depuis le postCreateCommand côté devcontainer.json (recommandé).
# Sinon, pour avoir un patch "baked-in" dans l'image, décommente la ligne COPY suivante et ajuste le chemin :
# COPY interacting_vacuum.diff /opt/interacting_vacuum.diff

RUN pip install --upgrade pip

# Python sphinx deps
RUN pip install sphinx sphinx-rtd-theme sphinxcontrib-bibtex myst-parser sphinx-autobuild sphinxcontrib-mermaid sphinxcontrib-datatemplates pyyaml --root-user-action=ignore

# Dossier de travail par défaut = racine des workspaces
WORKDIR /workspace

CMD ["/bin/bash"]