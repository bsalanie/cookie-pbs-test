# cookie-pbs-test

[![Release](https://img.shields.io/github/v/release/bsalanie/cookie-pbs-test)](https://img.shields.io/github/v/release/bsalanie/cookie-pbs-test)
[![Build status](https://img.shields.io/github/actions/workflow/status/bsalanie/cookie-pbs-test/main.yml?branch=main)](https://github.com/bsalanie/cookie-pbs-test/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/bsalanie/cookie-pbs-test/branch/main/graph/badge.svg)](https://codecov.io/gh/bsalanie/cookie-pbs-test)
[![Commit activity](https://img.shields.io/github/commit-activity/m/bsalanie/cookie-pbs-test)](https://img.shields.io/github/commit-activity/m/bsalanie/cookie-pbs-test)
[![License](https://img.shields.io/github/license/bsalanie/cookie-pbs-test)](https://img.shields.io/github/license/bsalanie/cookie-pbs-test)

testing my cookiecutter 

- **Github repository**: <https://github.com/bsalanie/cookie-pbs-test/>
- **Documentation** <https://bsalanie.github.io/cookie-pbs-test/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

``` bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:bsalanie/cookie-pbs-test.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with 

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.


## Releasing a new version

<!-- - Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting 
[this page](https://github.com/bsalanie/cookie-pbs-test/settings/secrets/actions/new). -->
- Create a [new release](https://github.com/bsalanie/cookie-pbs-test/releases/new) on Github. 
Create a new tag in the form ``*.*.*``.

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).