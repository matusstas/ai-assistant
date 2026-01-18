# Set the desired local pyenv version for the project
PYENV_LOCAL_VERSION=3.11.0

# Check if the local version is in the pyenv installed versions
if pyenv versions --bare | grep -qx "$PYENV_LOCAL_VERSION"; then
    echo "Pyenv version $PYENV_LOCAL_VERSION is available"
else
    echo "Pyenv version $PYENV_LOCAL_VERSION is not available. Here is a list of all installed versions:"
    pyenv versions --bare
    exit 1
fi

# Set the project's local python version to PYENV_LOCAL_VERSION
# This writes the version to .python-version in the project directory
pyenv local "$PYENV_LOCAL_VERSION"

# Configure poetry to create virtual environments inside the project directory
poetry config virtualenvs.in-project true

# Tell poetry to use the Python version provided by pyenv
poetry env use $(pyenv which python)

# Install the dependencies listed in pyproject.toml
poetry install
