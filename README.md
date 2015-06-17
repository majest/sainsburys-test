To set up the environment it's best to use virtualenv

```
$>virtualenv venv
$>. ./venv/bin/activate
```

Install application dependencies
```
$>pip install -r requirements.txt
```

Install dependencies required for the unit testing and development please run
```
$>pip install -r development.txt
```

To run the application
```
$>python main.py
```

To run the tests
```
$>py.test tests.py
```