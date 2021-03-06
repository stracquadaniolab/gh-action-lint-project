# lint-project
![GitHub release (latest SemVer)](https://img.shields.io/github/v/tag/stracquadaniolab/gh-action-lint-project)

This action controls if a project uses the lab file naming and directory structure. 

## Inputs

### `root_dir`

**Required** The root dir to check. Default: `.`.

### `project_layout`

**Required** URL to a project layout generated by `tree`. Default: `https://github.com/stracquadaniolab/cookiecutter-base-project/blob/master/layout.tree`.

### `naming_standard`

**Required** The regex for the naming standard. Default: `[a-z\._/0-9]*`

## Example usage

``` 
uses: stracquadaniolab/gh-action-lint-project
with:
  root_dir: '.'
```