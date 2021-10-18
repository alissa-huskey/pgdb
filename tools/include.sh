#!/usr/bin/env bash
#
# python and poetry utility functions
#

typeset -gx venv="$(poetry env info -p)"

# tell Python about the pgdb package
#   adds the current directory to your PYTHONPATH
setup_python_path() {
  if ! [[ "$PYTHONPATH" =~ [.][/] ]] && \
     ! [[ "$PYTHONPATH" =~ "$PWD" ]]; then

        typeset -gx PYTHONPATH="$PYTHONPATH:./"
  fi
}

# so tools installed by modules will be available at the command line
#   add the poetry executable directory to your path
setup_poetry_exes() {
  local exe_path

  for d in bin Scripts; do
    exe_path="${venv}/${d}"
    if [[ -d "${exe_path}" ]] && \
       ! [[ "$PATH" =~ "${exe_path}" ]]; then

        typeset -gx PATH="${PATH}:${exe_path}"
        break
    fi
  done
}

auto_start_poetry_shell() {
  # vscode does something equilivent to this already
  if [[ ${TERM_PROGRAM} == "vscode" ]]; then
      return
  fi

  # start if VIRTUAL_ENV is blank
  if [[ -z "${VIRTUAL_ENV}" ]]; then
      typeset -gx VIRTUAL_ENV="${venv}"
      poetry shell
  fi

  # warn if you're already in a virtual env
  if [[ "${VIRTUAL_ENV}" != "${venv}" ]]; then
      echo "Warning: You seem to virtual env active for another project." >&2
      echo "         You may want to leave it." >&2
  fi
}
