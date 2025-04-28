{ mkShell
, python314
, basedpyright
, pyright
}:

let
  # CHANGEME define the list of Python packages to pull from nixpkgs
  python-env = python314.withPackages (pp: with pp;
    # for example
    # [ pyspark numpy ]
    [ ]
  );
in
mkShell {
  # CHANGEME add other requirements
  buildInputs =
    # for example
    []
    # injects the Python base
    ++ [ python-env pyright basedpyright ];

  NIX_PYTHONPATH = "${python-env}/${python-env.sitePackages}";

  shellHook = ''
    if [[ ! -d .venv ]]; then
      echo "No virtual env found at ./.venv, creating a new virtual env linked to the Python site defined with Nix"
      ${python-env}/bin/python -m venv .venv
      cp ${builtins.toString ./sitecustomize.py} .venv/lib/python*/site-packages/
    fi
    source .venv/bin/activate
    echo "Nix development shell loaded."
  '';
}
