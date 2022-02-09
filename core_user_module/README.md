#### Install the core user module using the following command

```
pip install --force-reinstall 'git+https://github.com/rajatmishraintntra/monorepo.git@main#egg=core_user_module&subdirectory=core_user_module'
```

##### format of the source:

`REPO_URL=https://github.com/rajatmishraintntra/monorepo.git`

`BRANCH=main`

`EGG=core_user_module`

`SUBDIRECTORY=core_user_module`

```
pip install --force-reinstall 'git+{$REPO_URL}@{$BRANCH}#egg={$EGG}&{$SUBDIRECTORY}
```
