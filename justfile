# with hook, is going to push to pypi
push-tag num: 
  git tag -a "v0.1.{{num}}" -m "v0.1.{{num}}"
  git push --tags
