# Workshop: Building a Serverless Django Application

## Requirements

Python 3.5+ on your path.

## The Application

The application in `app/` is a simple Django application without a database
that has one page that shows a random quote by Henri Poincaré.

Most of the logic is in its `views.py` and `templates/index.html`.

## (Optional) Runnning the Application Locally

We use vanilla venv, pip, and Django to run:

```
cd app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Open it at http://127.0.0.1:8000/

## Deploying the Application

Best done in a separate terminal session, since there's a second venv.

First, you'll need to get a ticket by entering the Workshop password at
[workshops.adamj.eu](https://workshops.adamj.eu). Once you have one, it will
give some vars to fill into `deployment/playbook.yml`.

After you've done that, create a deployment venv, install Ansible and other
requirements into it, and run the deployment playbook:

```
cd deployment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ansible-playbook playbook.yml
```

Ansible should complete with a `PLAY RECAP` at the end like:

```
PLAY RECAP ********************************************************************
localhost                  : ok=14   changed=9    unreachable=0    failed=0
```

Check that `failed=0` - if not, see the preceding output for error messages.

Also in the output there is a final `debug` task displayaing the URL your
deployment can be accessed at in production - open it in a web browser to check
it out!

(To deploy after the workshop, you can remove the explicit AWS key
variables and relevant checks. Then you'll be able to deploy it as any suitably
privileged user on an AWS account.)

## Making a Change

Change the local version and deploy by rerunning the Ansible playbook. For
example, try changing the font, or the CSS, or the quotes! Be unique, so you
know it's not a trick and it's really your serverless Application being
deployed.

## Deploying to your own AWS Account

To deploy the application on your own AWS account, configure your AWS
credentials as an admin on that account (use the AWS CLI's `aws configure`),
check out the branch `deploy_as_admin_on_own_aws_account`, change its
`workshop_id` variable, and run the playbook as above.
