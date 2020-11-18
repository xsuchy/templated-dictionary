# templated-dictionary

This module provides dictionary where every item is evaluated as a Jinja2 expression.

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


## Sponsor

This project is sponsored by [Red Hat](https://www.redhat.com/). [Buy](https://www.redhat.com/en/store) Red Hat subscription to sponsor this project.

## License

GPLv2+
