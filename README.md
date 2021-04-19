# py_api_assignment

This is a Python API designed for inventory management of equipments. It can be accessed by student and a manager. Both have different level of access. A student can see all the available equipments, file a request for one or return the issued equipment.

## Installation

Use the package manager [pip](https://pypi.org/project/Flask/) to install Flask.

```bash
pip install flask
```
The sqlite3 is available by default in python 2.5.x version and above.

## Usage
To run the api run the following after clowning

```python
python app.py
```


Key is set as 1234 for the moment. The data contains 4 files [id, name, status, request_id]

For viewing all the equipments available to the student [id,name]
```curl
curl -i http://127.0.0.1:5000/student?key=<enter_key>
```
For requesting and returning the equipment, following can be used (changes status to requested and available respectively, the request_id stores the token when the status changes to requested and reverts back to none when the equipment is returned)
```curl
curl -i http://127.0.0.1:5000/student/request/<id>?key=<enter_key>

curl -i http://127.0.0.1:5000/student/return/<id>?key=<enter_key>
```

For viewing all the equipments available to the manager [id, name, status, request_id]
```curl
curl -i http://127.0.0.1:5000/manager?key=<enter_key>
```

For inserting new equipment as a manager

```curl
curl -i http://127.0.0.1:5000/manager/<name_of_the_equipment>?key=<enter_key>
```

Similarly, for approving requests (changes status to issued) and deleting values
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