## uv
uv can be used to manage dependencies for python projects.

### pyproject.toml

uv uses a pyproject.toml file to define dependencies for the project (along with other information). By default, dependencies will be installed from PyPI, but custom indexes (i.e. for PyTorch cuda binaries) can be defined and configured like the following:

```
[[tool.uv.index]]
name="pytorch-cu128"
url="https://download.pytorch.org/whl/cu128"

[tool.uv.sources]
torch = { index = "pytorch-cu128" }
torchvision = { index = "pytorch-cu128" }
torchaudio = { index = "pytorch-cu128" }
```

## Importing

When running `import foo`, python checks every entry in `sys.path` in order to find the module corresponding to `foo`.

By default `sys.path` includes the python file path, `.venv/Lib/site-packages`, etc.

In `site-packages`, if there are any .pth files, python will add each line of these to `sys.path`.

When you use a build-system with `uv`, i.e. hatchling (which is usually included by default):
```pyproject.toml
[build-system]
requires = ["hatchling"]
build-backend="hatchling.build"

[tool.hatch.build.targets.wheel]
packages=[...]
```
it will install your packages in editable mode, thus creating .pth files in site-packages automatically.

If the package is root, i.e. `"."`, then the path of the root of the project is added to the pth file, otherwise, it adds the directory the package is a child of to the pth. 
