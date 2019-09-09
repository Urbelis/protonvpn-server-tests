[![Link](https://protonvpn.com/assets/img/media/protonvpn-logo-grey.png)](https://protonvpn.com/)


# ProtonVPN server tests
[![Actions Status](https://github.com/Urbelis/protonvpn-server-tests/workflows/Proton%20VPN%20Server%20tests/badge.svg)](https://github.com/Urbelis/protonvpn-server-tests/actions)

API tests for ProtonVPN services written in Python using requests lib. 


## Prerequisites

You will need to install [Python 3.7](https://www.python.org/downloads/) 

## Installation

Get the repository:
```
$ git clone https://github.com/Urbelis/protonvpn-server-tests.git
```

Install the dependancies:
```
$ pip install -r requirements.txt
```

## Running the tests

Launch tests:
```
$ pytest
```

Run the server status check:
```
$ python server_status.py
```

Server status check will generate log files in ```~/logs``` directory listing servers that are offline or under high load

## Developing new tests

1. Create a test file under ```/tests``` directory in the following format: ```test_*.py``` otherwise pytest runner will ignore it
2. If the endpoint is new, add a new endpoint class under ```~/endpoints``` 
3. Create a new service class under ```~/services```

The current project structure is:

```
├───.github
│   └───workflows
|       └───pythonapp.yml
├───endpoints
│   └───vpn.py
├───logs
|   └───20190909-080528
├───schemas
|   └───logical_servers.json
├───services
│   └───vpn.py
├───tests
│   └───test_servers.py
├───utils
|    └───helpers.py
├── config.py
├── requirements.txt
├── server_status.py
├── .gitignore
└── README.md
```


## Configuring automatic builds

Automatic nightly builds are currently configured to run via [Github Actions](https://github.com/Urbelis/protonvpn-server-tests/actions)

If you want to make changes to the workflow, check this [page](https://help.github.com/en/articles/configuring-a-workflow#triggering-a-workflow-with-events)










