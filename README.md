# IDSS Seriation Version 2:  Iterative Deterministic Seriation Solutions #

Library and executables which implement the algorithms in:

* https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0124942
* http://github.com/mmadsen/dissertation

for performing various types of deterministic frequency-based seriation.  

## Table of Contents ##

<!--ts-->
   * [IDSS Seriation Version 2:  Iterative Deterministic Seriation Solutions](#idss-seriation-version-2--iterative-deterministic-seriation-solutions)
      * [Table of Contents](#table-of-contents)
      * [Documentation](#documentation)
      * [Setup for Development](#setup-for-development)
         * [Setting Up Virtual Environment with Makefile](#setting-up-virtual-environment-with-makefile)
         * [MANUAL set up a development environment](#manual-set-up-a-development-environment)
      * [Branch Policy](#branch-policy)
      * [Dependency Management](#dependency-management)
      * [Environmental Dependencies:  Other Software Required](#environmental-dependencies--other-software-required)
      * [Support Policy](#support-policy)

<!-- Added by: mark, at: Sun Jun 21 12:58:17 PDT 2020 -->

<!--te-->


## Documentation ##

All documentation is contained in Sphinx format in the `docs` directory, including instructions on using
command line versions, integrating into other projects as a library, and distributed execution on a cloud computing
cluster using the Ray library.

Build documentation:

1.  `cd doc`
1.  `make html`
1.  `open _build/html/index.html`

## Setup for Development ##

The following are instructions on setting up for modifying or adding to this repository.  This library uses:

1.  Python 3.7 -- install with Homebrew `brew install python`.  This you need to have on your system before starting.  Everything else will be installed.
1.  Pytest as the unit testing framework.   https://docs.pytest.org/en/latest/
1.  Pre-commit to install and enforce pre-commit hooks for Git, which run code checks prior to allowing commits and pushes to the repository.  https://pre-commit.com/
1.  Black to automatically format Python code according to PEP8.  A pre-commit hook will run this automatically upon commit, so you don't have to do anything in your editor, just write and let it properly format.   https://github.com/ambv/black
1.  Flake8 to automatically "lint" your Python code and report problems.  Issues need to be fixed prior to committing to the repo.  http://flake8.pycqa.org/en/latest/
1.  Bandit and Safety for automated code security checks -- mainly to keep from doing really dumb things accidentally.
1.  Mypy for static typing.  This can be a pain in the ass but is important for building extensible libraries.

**IMPORTANT NOTE**:  All development occurs within a "virtual environment" to isolate dependencies and ensure repeatable tests.  See next two sections.  Also note that this code uses "pre-commit" hooks to prevent
code from being checked in which:

* Pass all unit tests, period.
* Pass Flake8 "lint" checking for bad coding practices
* Is formatted by the Black code formatter
* Other specific checks including static type checks.


### Setting Up Virtual Environment with Makefile ###

`make setup-dev` will:

* Remove directory `venv` and any subdirectories to create a clean environment
* Sets up `venv/asset_utilization_service` as a virtual environment
* Installs dependencies to the virtual environment, including development dependencies
* Installs pre-commit hooks
* Installs the asset service code in `editable` mode in the virtual environment, so changes you make are instantly runnable
* Runs pytest

At the conclusion of the "make" script, you can just do `source venv/asset_utilization_service/bin/activate` in your shell and you're ready to develop.

`make setup-ec2` will set up the virtual environment as described above,  with some extra flags that turn out to be useful on Ubuntu Linux to manage and isolate the virtual environment.  This is recommended for using AWS EC2 instances for testing.


### MANUAL set up a development environment ###

1.  Create a local virtual environment:  `virtualenv <environment directory name>`.  If you use `venv` or `.venv` (on Unix-like systems) as the name, `.gitignore` is already set up to ignore them.  Activate your virtual environment:  `source <name>/bin/activate`.
1.  Install production dependencies:  `pip install -r requirements.txt`.
1.  Install development-only dependencies:  `pip install -r requirements-dev.txt`.  This is separate because these packages will not be present in the production Docker container image.
1.  Install pre-commit hooks:  `pre-commit install`.  THIS IS A VERY IMPORTANT STEP - DO NOT SKIP IT!
1.  Setup local copy of library for testing without having to `python3 setup.py install` every time you change something:  `pip install -e .`

At this point, you should be able to make changes to the code, test with `pytest`, and when you try to commit, the code will be checked, formatted, and unit tests run.  

NOTE:  Pytest also runs automatically on the pre-commit hook.  You will NOT be able to commit and push if unit tests do not pass.

### Committing Code with Pre-Commit Hooks ###

Pre-commit hooks run some checks and formatters before committing to your local Git repository.  It looks like the
examples below.  The first time you try to commit, you might see an error, or even just the need for the
formatter to reformat things consistently.  There are small hooks for cleaning whitespace in files, checking JSON or
YAML for formatting errors, etc.  Any of them can return an issue, as in this example.  

```shell
(idss-seriation-v2) #>  git add -A .; git commit -m 'updating docs'                                                                                                                                                        (development✱)
black....................................................................Failed
hookid: black

Files were modified by this hook. Additional output:

reformatted test/test_dummy.py
All done! ✨ 🍰 ✨
1 file reformatted.

mypy.....................................................................Passed
Check for added large files..............................................Passed
Check JSON...........................................(no files to check)Skipped
Check Yaml...........................................(no files to check)Skipped
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Failed
hookid: trailing-whitespace

Files were modified by this hook. Additional output:

Fixing README.md

Flake8...................................................................Passed
pytest...................................................................Passed
safety...............................................(no files to check)Skipped
bandit...................................................................Passed
```

When they return an issue, NO CODE HAS BEEN COMMITTED.  You fix whatever is going on -- and try again.
In this particular example, it was just reformatting, but if a unit test failed, for example,
you need to fix the code that is causing the test to fail and then you can try again.

When you try again, you need to `git add` files again too, not just retry the commit.

```
(idss-seriation-v2) #>  git add -A .; git commit -m 'updating docs'                                                                                                                                                        (development✱)
black....................................................................Passed
mypy.....................................................................Passed
Check for added large files..............................................Passed
Check JSON...........................................(no files to check)Skipped
Check Yaml...........................................(no files to check)Skipped
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
Flake8...................................................................Passed
pytest...................................................................Passed
safety...............................................(no files to check)Skipped
bandit...................................................................Passed
[development cfa851d] updating docs
 2 files changed, 13 insertions(+), 10 deletions(-)
 create mode 100644 test/test_dummy.py
```

Your code has not be committed until you see the `files changed` message at the bottom.  Once you see that,
you can also do a `git push` up to Github.  

## Branch Policy ##

By default, the main branch in which development is merged is `development`.  This is the branch you will get if you do a `git clone`
without any other arguments.  Features and major work should be done in feature branches named `feature/XXXXXX` and then
merged into development when complete and tested.

Full releases designed for public usage will be merged into branch `master` and tagged with version numbers, beginning with 2.0.0.  

Only releases in branch `master` should be uploaded to PyPI, Docker Hub, or other public spaces for non-developers to use.


## Dependency Management ##

Library and code dependencies are managed in two files:  `requirements.txt` for dependencies required in the execution environment, and `requirements-dev.txt` for dependencies required only to edit and test code.

All public library dependencies are derived from PyPI, and can be retrieved by `pip3` without any credentials.


## Environmental Dependencies:  Other Software Required ##

<TBD on distributed cloud execution>


## Support Policy ##

This is open-source software, available to the research community for use under the terms of the Apache Public License contained here.

Support is handled through `Issues` on the Github repository, and you are encouraged to open an issue if you have a problem or bug after
carefully using the documentation to set things up for your use case.  Support for normal usage is not available since the authors both have
full time jobs, but we will attempt to answer problems or bugs within a reasonable interval.  We welcome pull requests for enhancements or bug fixes!
