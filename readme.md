
# Table of Contents

1.  [About](#org8c9eede)
    1.  [Notes](#orgdc0710f)
    2.  [Coverage](#org345b143)
        1.  [Python Coverage](#orga63d408)
        2.  [Combined Coverage](#orgbf69e97)
    3.  [License](#org906840a)


<a id="org8c9eede"></a>

# About

A repository demonstrating the usage of `pytest` within the `meson-python`
ecosystem. Reproducibility is ensured via `pixi` and the `conda-ecosystem`.


<a id="orgdc0710f"></a>

## Notes

-   `pytest-cov` will not produce coverage for C++ by default
-   To build and locally install an editable variant of the package you will need
    `--no-build-isolation`, however, this means the build dependencies have to be
    present (i.e. `pip install ninja meson meson-python pybind11`)


<a id="org345b143"></a>

## Coverage

First we need to add some tools (already part of the environment):

    pixi add lcov gcovr
    # For editable installation, discussed above
    pip install ninja meson meson-python pybind11


<a id="orga63d408"></a>

### Python Coverage

For starters, consider:

    pip install -e .[test] --no-build-isolation
    # immediate visualization
    pytest --cov=pybtst2024

Or if we want to store it for later:

    pytest --cov=pybtst2024 --cov-report=lcov
    # Written out to coverage.lcov
    lcov --list coverage.lcov


<a id="orgbf69e97"></a>

### Combined Coverage

To generate C++ coverage along with the Python bits, we can use the command line
to invoke `meson` with the appropriate options <sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>:

    python -m pip install -ve . --no-build-isolation -Csetup-args=-Dbuildtype=debug -Csetup-args=-Db_coverage=true -Cbuilddir=bbdir
    pytest --cov=pybtst2024 --cov-report=lcov
    lcov --output-file coverage.cpp --capture --directory bbdir
    lcov --output-file coverage.cpp --extract coverage.cpp $PWD/src/"*"
    cat coverage.lcov coverage.cpp > coverage.combined
    lcov --list coverage.combined

Which will produce the coverage for both C++ and Python sections:

    Reading tracefile coverage.combined
                      |Lines       |Functions  |Branches
    Filename          |Rate     Num|Rate    Num|Rate     Num
    ========================================================
    [/home/rgoswami/Git/Github/sqm_rg/pytest_demo_2024/src/]
    money.hpp         |80.0%      5|80.0%     5|    -      0
    pyb_core.cpp      | 100%      9| 100%     2|    -      0
    
    [src/pybtst2024/]
    __init__.py       | 100%      1|    -     0|    -      0
    _util.py          | 100%      2|    -     0|    -      0
    currency.py       | 0.0%     23|    -     0|    -      0
    ========================================================
                Total:|40.0%     40|85.7%     7|    -      0

Or in a single `pixi` invocation, `pixi run cover`.


<a id="org906840a"></a>

## License

MIT


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> As noted [here](https://github.com/pybind/pybind11/discussions/4141#discussioncomment-7068063)
