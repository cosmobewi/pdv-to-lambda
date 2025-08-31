# 📚 Cosmobewi — Sphinx Runner

This repository serves as the **central portal** to build and publish all **Cosmobewi** articles and documentation using **GitHub Pages**.

Each article or project lives in its own repository and is included here as a **Git submodule**.  
The GitHub Actions CI pipeline automatically rebuilds and deploys the documentation.

---

## 🚀 Overview

### Structure
- `projects.yml` : registry of projects (id, submodule path, output directory).  
- `conf/` : shared Sphinx configuration and theme (CSS, templates).  
- `scripts/` : helper scripts for building all projects and generating the portal.  
- `submodules/` : linked repositories containing articles or documentation.  
- `_site/` : final generated site, deployed automatically to GitHub Pages.  

### Build Pipeline
1. **Checkout + submodules** → retrieves this repository and initializes the submodules.  
2. **Sphinx build** → each project is compiled with Sphinx.  
   - If the project defines its own `conf.py`, it is used.  
   - Otherwise, the shared configuration in `conf/` is applied.  
3. **Portal generation** → a script creates `portal/index.rst` listing all projects.  
4. **Deployment** → the final site is deployed via GitHub Actions to GitHub Pages.  

### Adding a new project

```bash
# Add the remote repository as a submodule
git submodule add https://github.com/cosmobewi/my-article.git submodules/my-article

# Edit projects.yml and declare the project
vim projects.yml

# Commit and push
git commit -am "Added project my-article"
git push
````

The project will be included in the next build and published at:

```
https://cosmobewi.github.io/<project-id>
```

---

## 🐳 Development with Docker / Devcontainer

A **Dockerfile** is provided to ensure a reproducible environment for building the documentation with Sphinx.

* Base: Python 3.12 (slim)
* Minimal system dependencies (`git`, `cmake`, `pkg-config`, etc.)
* Python packages:

  * sphinx
  * sphinx-rtd-theme
  * myst-parser
  * sphinxcontrib-bibtex
  * sphinxcontrib-mermaid
  * sphinxcontrib-datatemplates
  * sphinx-autobuild
  * pyyaml

### Command-line usage

```bash
# Build the image
docker build -t sphinx-runner .

# Run an interactive container with port 8000 exposed
docker run -it --rm -v $(pwd):/workspace -p 8000:8000 sphinx-runner

# Inside the container, build the documentation
sphinx-build -b html portal _build/html
```

### VS Code Devcontainer

A `devcontainer.json` is provided for integration with Visual Studio Code.
It configures the environment, extensions, and port forwarding:

```jsonc
{
  "name": "Cosmo-Doc",
  "build": { "dockerfile": "Dockerfile" },
  "workspaceFolder": "/workspace",
  "mounts": [
    "source=${localWorkspaceFolder},target=/workspace,type=bind,consistency=cached"
  ],
  "remoteUser": "root",
  "forwardPorts": [8000],
  "portsAttributes": {
    "8000": {
      "label": "Sphinx Live Preview",
      "onAutoForward": "openBrowser"
    }
  }
}
```

---

## 🌐 Live Preview

To enable automatic rebuilds and preview in a browser:

```bash
# Inside the container
sphinx-autobuild . _build/html --host 0.0.0.0 --port 8000
```

Then open:

```
http://localhost:8000
```

Thanks to the Devcontainer configuration, VS Code will automatically forward and open this port.

---

## 📂 Repository layout

```
sphinx_runner/
├─ .github/workflows/build-and-deploy.yml
├─ conf/
│  ├─ conf.py
│  ├─ _static/cosmobewi.css
│  └─ _templates/
├─ projects.yml
├─ scripts/
│  ├─ build_all.sh
│  └─ gen_index.py
├─ portal/index.rst
└─ submodules/
   ├─ lambda-usure-temps/
   └─ timescape-notes/
```

---

## ✅ Key features

* **Centralized**: one pipeline, one theme, one portal.
* **Modular**: each article remains in its own repository.
* **Automated**: CI/CD with GitHub Actions and GitHub Pages.
* **Extensible**: easy to add new projects.
* **Portable**: ready-to-use Docker/Devcontainer environment.

---

## 🔗 Access

* Main portal: [https://cosmobewi.github.io](https://cosmobewi.github.io)
* Example sub-site: [https://cosmobewi.github.io/lambda-usure-temps](https://cosmobewi.github.io/lambda-usure-temps)