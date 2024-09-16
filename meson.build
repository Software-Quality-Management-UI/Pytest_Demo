project('pybtst2024', 'cpp', version: '0.1.0')
deps = []
py = import('python').find_installation('python')
deps += py.dependency()
deps += dependency('pybind11')

# For the bindings
py.extension_module(
  '_core',
  sources : [
    'src/pyb_core.cpp'
  ],
  dependencies: deps,
  install: true,
  subdir: 'pybtst2024',
)

# python packages
py.install_sources([
    'src/pybtst2024/__init__.py',
    'src/pybtst2024/_util.py',
  ],
  pure: false, # install next to compiled extension
  subdir: 'pybtst2024'
)
