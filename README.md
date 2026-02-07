# data_warehouse – Developer Setup Guide (venv or conda)

This project can be set up using either:

- a standard Python virtual environment (venv), or
- a conda environment

Choose **ONE** approach per project.  
**Do NOT mix an active conda environment and a venv at the same time.**

This project depends on an internal Git-over-SSH package:

git@github.com:jonathanwilsonami/test_python_package.git

You must have SSH access configured.

---

## General rules for this repository

- This repository is installed in editable mode.
- Runtime dependencies are installed automatically.
- Test tools (pytest) are **not** installed by default.
- Install pytest only if you intend to run tests.

If anything looks odd with imports, always verify:

python -c "import sys; print(sys.executable)"

---

## Prerequisite (all users)

Verify SSH access before continuing:

git clone git@github.com:jonathanwilsonami/test_python_package.git /tmp/ssh_test_pkg  
rm -rf /tmp/ssh_test_pkg

---

# Option A – Recommended for most users (venv only)

**Important**

If you normally use conda, disable auto-activation of conda base first.

Run once:

conda config --set auto_activate_base false

Open a new terminal after running the command above.

---

## Setup

git clone <DATA_WAREHOUSE_REPO_URL>  
cd data_warehouse

python -m venv .venv  
source .venv/bin/activate

python -m pip install --upgrade pip  
pip install -e .

---

## Run the demo

python -m data_warehouse

(or, if provided)

dwh-demo

---

## Install test tools and run tests

pip install pytest  
pytest -m my_test_suite

(or simply)

pytest

---

# Option B – Conda environment (no venv)

Use this option if you prefer conda for Python management.

Do not create or activate a venv when using this option.

---

## Setup

conda create -n data-warehouse python=3.12 -y  
conda activate data-warehouse

python -m pip install --upgrade pip  
pip install -e .

---

## Run the demo

python -m data_warehouse

(or, if provided)

dwh-demo

---

## Install test tools and run tests

pip install pytest  
pytest -m my_test_suite

(or simply)

pytest

---

# Important notes

1. Do not mix conda and venv

You should see either:

(.venv)

or:

(data-warehouse)

in your shell prompt — not both.

2. If you see both "(base)" and ".venv" active, your PATH may resolve tools from the wrong environment.

In that case either:

- deactivate conda, or
- use the conda-only workflow above.

3. If imports fail but installation succeeded, verify:

python -c "import data_warehouse; print(data_warehouse.__file__)"

---

# Recommended daily workflow (copy / paste)

## venv users

git clone <DATA_WAREHOUSE_REPO_URL>  
cd data_warehouse  
python -m venv .venv  
source .venv/bin/activate  
pip install -e .  
pip install pytest  
pytest  
python -m data_warehouse

## conda users

git clone <DATA_WAREHOUSE_REPO_URL>  
cd data_warehouse  
conda create -n data-warehouse python=3.12 -y  
conda activate data-warehouse  
pip install -e .  
pip install pytest  
pytest  
python -m data_warehouse
