VENV=~/software/pants_venv
python3 -m venv "${VENV}"
"${VENV}/bin/pip" install -r <(./pants dependencies :: |
  xargs ./pants filter --target-type=python_requirement |
  xargs ./pants peek |
  jq -r '.[]["requirements"][]')