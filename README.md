# py_api_assignment

This is a Python API designed for inventory management of softwares. It can be accessed by student and a manager. Both have different level of access. A student can see all the available softwares, file a request for one or return the issued software.

## Installation

Use the package manager [pip](https://pypi.org/project/Flask/) to install Flask.

```bash
pip install flask
```
The sqlite3 is available by default in python 2.5.x version onwards.

## Usage
Key is set as 1234 for the moment.

For viewing all the softwares available to the student [id,name]
```curl
curl -i http://127.0.0.1:5000/student?key=<enter_key>
```
For requesting and returning the software, following can be used
```curl
curl -i http://127.0.0.1:5000/student/request/<id>?key=<enter_key>

curl -i http://127.0.0.1:5000/student/return/<id>?key=<enter_key>
```

For viewing all the softwares available to the manager [id, name, status, request_id]
```curl
curl -i http://127.0.0.1:5000/manager?key=<enter_key>
```
For inserting new software as a manager
```curl
curl -i http://127.0.0.1:5000/manager/<name_of_the_software>?key=<enter_key>
```
Similarly, for approving requests and deleting values
```curl
curl -i http://127.0.0.1:5000/manager/request/<id>?key=<enter_key>

curl -i http://127.0.0.1:5000/delete/<id>?key=<enter_key>
```

For accessing any value by its id
```curl
curl -i http://127.0.0.1:5000/<id>?key=<enter_key>
```




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.