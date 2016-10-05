from fabric.api import env, task
from envassert import detect, package, process, service, user
from hot.utils.test import get_artifacts


@task
def check():
    env.platform_family = detect.detect()

    packages = ['st2',
                'st2chatops',
                'st2mistral',
                'st2web',
                'rabbitmq-server',
                'mongodb-org-server',
                'postgresql'
                ]

    services = ['st2api',
                'st2sensorcontainer',
                'mistral',
                'st2resultstracker',
                'rabbitmq-server',
                'mongod',
                'postgresql'
                ]

    for pkg in packages:
        assert package.installed(pkg),\
            "package {0} is not installed".format(pkg)

    for srv in services:
        assert service.is_enabled(srv),\
            "service {0} is not enabled".format(srv)

    assert user.exists("stanley"), "user stanley does not exist"


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
