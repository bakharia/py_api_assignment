# py_api_assignment

Foobar is a Python API designed for inventory management of softwares. It can be accessed by student and a manager. Both have different level of access. A student can see all the available softwares, file a request for one or return the issued software.

## Installation

Use the package manager [pip](https://pypi.org/project/Flask/) to install Flask.

```bash
pip install flask
```
The sqlite3 is available by default in python 2.5.x version onwards.

## Usage
Key is set as 1234 for the moment.


```curl
curl -i http://http://127.0.0.1:5000//student?key=<enter_key>
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)