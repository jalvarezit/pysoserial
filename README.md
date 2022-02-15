<h1 align="center">Welcome to pysoserial 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/jusepe\_it" target="_blank">
    <img alt="Twitter: jusepe_it" src="https://img.shields.io/twitter/follow/jusepe_it.svg?style=social" />
  </a>
</p>

> Python deserialization payload generator

### 🏠 [Homepage](https://github.com/itasahobby/pysoserial)

## Install

### PyPI

```sh
pip install pysoserial
```

### Github

```
pip install git+https://github.com/itasahobby/pysoserial.git
```

## Usage
```
usage: pysoserial.py [-h] -p PAYLOAD -l {os,subprocess} -s {pickle,json,yaml} [--plaintext]

optional arguments:
  -h, --help            show this help message and exit
  -p PAYLOAD, --payload PAYLOAD
                        payload to execute
  -l {os,subprocess}, --library {os,subprocess}
                        library to execute the payload with
  -s {pickle,json,yaml}, --serializer {pickle,json,yaml}
                        serializer to generate the payload for
  --plaintext           print result in plain text (default is base64)
```

## Author

👤 **ITasahobby**

* Website: https://blog.itasahobby.com
* Twitter: [@jusepe_it](https://twitter.com/jusepe_it)
* Github: [@itasahobby](https://github.com/itasahobby)

## Mentions

👤 **KlezVirus**

Idea inspired by [KlezVirus](https://twitter.com/KlezVirus)' [deser-py](https://github.com/klezVirus/deser-py) project

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/itasahobby/pysoserial/issues). 

## Show your support

Give a ⭐️ if this project helped you!
