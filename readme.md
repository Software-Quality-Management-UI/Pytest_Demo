
# Table of Contents

1.  [About](#orgfdef4d6)
    1.  [Notes](#org7f11320)
    2.  [Coverage](#org8f564bb)
        1.  [Python Coverage](#org3f11ade)
        2.  [Combined Coverage](#org1c81242)
        3.  [Pretty view](#org5435ab6)
    3.  [License](#orgc6e8d8a)


<a id="orgfdef4d6"></a>

# About

[![img](https://gitlab.com/tolvunarfraedi/hbv505m_2024/pytest_demo_2024/badges/cidemo/pipeline.svg?ignore_skipped=true)](https://gitlab.com/tolvunarfraedi/hbv505m_2024/pytest_demo_2024/-/tree/cidemo)
[![img](https://gitlab.com/tolvunarfraedi/hbv505m_2024/pytest_demo_2024/badges/cidemo/coverage.svg?job=mycompile)](https://gitlab.com/tolvunarfraedi/hbv505m_2024/pytest_demo_2024/-/tree/cidemo)

A repository demonstrating the usage of `pytest` within the `meson-python`
ecosystem. Reproducibility is ensured via `pixi` and the `conda-ecosystem`.
Includes Continuous Integration.

The coverage report is [here](https://pytest-demo-2024-d84111.gitlab.io/): <https://pytest-demo-2024-d84111.gitlab.io//>


<a id="org7f11320"></a>

## Notes

-   `pytest-cov` will not produce coverage for C++ by default
-   To build and locally install an editable variant of the package you will need
    `--no-build-isolation`, however, this means the build dependencies have to be
    present (i.e. `pip install ninja meson meson-python pybind11`)


<a id="org8f564bb"></a>

## Coverage

First we need to add some tools (already part of the environment):

    pixi add lcov gcovr
    # For editable installation, discussed above
    pip install ninja meson meson-python pybind11


<a id="org3f11ade"></a>

### Python Coverage

For starters, consider:

    pip install -e .[test] --no-build-isolation
    # immediate visualization
    pytest --cov=pybtst2024

Or if we want to store it for later:

    pytest --cov=pybtst2024 --cov-report=lcov
    # Written out to coverage.lcov
    lcov --list coverage.lcov


<a id="org1c81242"></a>

### Combined Coverage

To generate C++ coverage along with the Python bits, we can use the command line
to invoke `meson` with the appropriate options <sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>:

    python -m pip install -ve .[test] --no-build-isolation -Csetup-args=-Dbuildtype=debug -Csetup-args=-Db_coverage=true -Cbuilddir=bbdir
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


<a id="org5435ab6"></a>

### Pretty view

It is possible to get a better understanding of what is covered by using `genhtml`.

    pixi run cover
    genhtml -o covHTML coverage.combined
    python -m http.server -d covHTML

Where a much more visual depiction can be experienced at `localhost:8000`, and
the steps above can also be encapsulated into a `pixi run covhttp` task.


<a id="orgc6e8d8a"></a>

## License

MIT


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> As noted [here](https://github.com/pybind/pybind11/discussions/4141#discussioncomment-7068063)
