# Installing and Running MSSP-CNC


The easiest way to run the mssp application is to pull the docker container:

    docker run -p 8888:80 scotchoaf/mssp-cnc

Then access the UI via http://localhost:8888

The default username and password is: `mssp` and `mssp`

**Note**: The example uses port 8888 to run and access the application. Modify to an open port as needed


Building PanHandler
-------------------

If you want to build mssp-cnc from source (which is not recommended). You will need to update the git submodules,
install the pip python requirements for both the app and also CNC, create the local db, and create a local user.


    git submodule init
    git submodule update
    pip install -r requirements.txt
    pip install -r cnc/requirements.txt
    ./cnc/manage.py migrate
    ./cnc/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('mssp', 'admin@example.com', 'mssp')"