# templated-dictionary

This module provides dictionary where every item is evaluated as a Jinja2 expression.

[![PyPI version](https://badge.fury.io/py/templated-dictionary.svg)](https://pypi.org/project/templated-dictionary/)
[![PyPI - License](https://img.shields.io/pypi/l/templated-dictionary)](https://opensource.org/licenses/)

## Packaging status

![templated-dictionary versions](https://repology.org/badge/vertical-allrepos/python:templated-dictionary.svg?exclude_unsupported=1&header=python:templated-dictionary)

## Usage

```
>>> from templated_dictionary import TemplatedDictionary

>>> td = TemplatedDictionary()

>>> td['owner'] = "foo"
>>> td['message'] = "say hello to {{owner}}"
>>> td['message']
'say hello to {{owner}}'

>>> td['__jinja_expand']=True

>>> td['message']
'say hello to foo'
>>> td['owner']="bar"
>>> td['message']
'say hello to bar'


>>> td = TemplatedDictionary( { "path": "/{{dist}}/{{arch}}", "dist": "rhel", "arch": "x86_64" })
>>> td['__jinja_expand']=True
>>> td['path']
'/rhel/x86_64'

>>> td = TemplatedDictionary(alias_spec={"dist": ["distribution", "distrib"], "arch": ["architecture"]})
>>> td['__jinja_expand']=True
>>> td["distribution"] = "fedora"
>>> td["architecture"] = "aarch64"
>>> td["path"] = "/{{dist}}/{{arch}}"

>>> td["path"]
'/fedora/aarch64'
>>> td["distribution"]
'fedora'
>>> td["dist"]
'fedora'

# Jinja will not actually expand `distribution` even when it exists, because it is aliased to `dist`
>>> td["path2"] = "/{{distribution}}/{{arch}}"
>>> td["path2"]
'//aarch64'


```

## Enabling expansion

Expansion is disabled at the beggining. This is because you may want to read the content unexpanded. You can enable and disable the expansion as you want

```
>>> from templated_dictionary import TemplatedDictionary
>>> td = TemplatedDictionary()
>>> td["dist"] = "rhel"
>>> td["arch"] = "x86_64"
>>> td["base_path"] = "/{{dist}}/{{arch}}"

# if expanded we would loose the flexibility of changing the variables later
>>> td["full_path"] = "/opt" + td["base_path"]

>>> td["full_path"]
'/opt/{{dist}}/{{arch}}'

>>> td['__jinja_expand']=True
>>> td["full_path"]
'/opt/rhel/x86_64'

>>> td['__jinja_expand']=False
>>> td["full_path"]
'/opt/{{dist}}/{{arch}}'
```


## Exceptions

The class `TemplatedDictionary` is based on [`collections.abc.MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping). Beside its exceptions it can return `ValueError` when recursion is too deep. Default is set to 5 and can be changed using:

```
>>> td = TemplatedDictionary()
>>> td['jinja_max_recursion'] = 10
```

## Sources

The upstream is https://github.com/xsuchy/templated-dictionary

To get the tarball run:

```
git clone https://github.com/xsuchy/templated-dictionary
cd templated-dictionary
tito build --tgz
```

To get an RPM run:

```
tito build --rpm
```

To get an RPM from latest commit and to install it run:

```
tito build --rpm --test -i
```

## History

This library has been created for the [Mock](https://github.com/rpm-software-management/mock/) where various authors contributed to this. I extrected the code and spint it off as separate project.

## Sponsor

This project is sponsored by [Red Hat](https://www.redhat.com/). [Buy](https://www.redhat.com/en/store) Red Hat subscription to sponsor this project.

## License

GPLv2+
