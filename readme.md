
# Table of Contents

1.  [About](#org5fb9279)
    1.  [Notes](#orgc8b26d9)
    2.  [Coverage basics](#org1a6f156)
        1.  [Python Coverage](#org3dff7e9)
    3.  [License](#org4e26491)


<a id="org5fb9279"></a>

# About

A repository demonstrating the usage of `pytest` within the `meson-python`
ecosystem. Reproducibility is ensured via `pixi` and the `conda-ecosystem`.


<a id="orgc8b26d9"></a>

## Notes

-   `pytest-cov` will not produce coverage for C++ by default
-   To build and locally install an editable variant of the package you will need
    `--no-build-isolation`, however, this means the build dependencies have to be
    present (i.e. `pip install ninja meson meson-python pybind11`)


<a id="org1a6f156"></a>

## Coverage basics

First we need to add some tools (already part of the environment):

    pixi add lcov gcovr


<a id="org3dff7e9"></a>

### Python Coverage

For starters, consider:

    pip install -e .[test] --no-build-isolation
    # immediate visualization
    pytest --cov=pybtst2024

Or if we want to store it for later:

    pytest --cov=pybtst2024 --cov-report=lcov
    # Written out to coverage.lcov
    lcov --list coverage.lcov


<a id="org4e26491"></a>

## License

MIT

