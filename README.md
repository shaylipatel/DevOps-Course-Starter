# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Setting up Trello and configuring API token

Trello’s API to fetch and save to-do tasks. In order to use their API, you need to first create an account (https://trello.com/signup), then generate an API key and token by following the instructions (https://trello.com/app-key).

In the .env file, set the Trello API key and token as environment variables.
Ensure that the .env file is added to the .gitignore to prevent credentials from being made public.

Once the account has been set up, create a Trello board. 

You will need to get the Board ID by making the following GET request to the 1/members/{memberId}/boards resource and list all of the boards associated with you.
Make the below request and remember to replace the {yourKey} and {yourToken} parameters with the key and token values.

'''bash
curl 'https://api.trello.com/1/members/me/boards?key={yourKey}&token={yourToken}'
'''

In the response you will get the list of boards associates with you, set a new environment variable in .env file with the relavent board ID. This will allow for development/testing board ID and prod board ID's to be changed easily. 

To access these environment variables in the python code, use os.getenv('YOUR_ENV_VAR_NAME').
## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the tests
In order to run the tests, run the following in the terminal.
```bash
$ poetry run pytest
```

Ensure that the test files have a name of the format of test_*.py or *_test.py.
'*' refers to the original name of the file you want to test.
You can store the test file alongside the file you want to test.

## Provisioning VM's
### SSH into Control Node and check Ansible installation
SSH into the Control Node using a command in the below format.
```bash
$ ssh USERNAME@IP-ADDRESS
```

Check that Ansible is installed by connecting to the control node and running the command 
```bash
$ ansible --version
```
If this prints out some info including a version number, then Ansible is installed. 
Don’t worry if it says messages that include “[DEPRECATION WARNING]” etc.

If Ansible isn’t installed, then install it with 
```bash
$ sudo pip install ansible
```
This might take a minute to run and might show a warning/error message at the end.
Even if it does, run ansible --version to check if installation succeeded.

### Set up SSH between your Control and Managed Nodes
On the Control Node, create an SSH key pair with the ssh-keygen command line tool. 
This will generate the key pair in an .ssh directory in the home directory.
```bash
$ ssh-keygen
```

Copy the public key to the Managed nodes by running this command.
```bash
$ ssh-copy-id ec2-user@managed-host-ip
```


### Run the Ansible Playbook
In order to provision a VM from an Ansible Control Node, ensure the host names for the Managed Control Nodes are listed 
in the my-ansible-inventory.ini file.
On the Ansible Control Node, run the following command to run it in the interactive mode.

```bash
$ ansible-playbook my-ansible-playbook.yml -i my-ansible-playbook.ini
```
When prompted, enter the TRELLO_KEY and TRELLO_TOKEN.
