from fabric.api import env, task
from envassert import detect, package, process, service, user
from hot.utils.test import get_artifacts


@task
def check():
    env.platform_family = detect.detect()

    packages = ['st2common',
                'st2reactor',
                'st2actions',
                'st2api',
                'st2auth',
                'st2debug',
                'python-st2client',
                'rabbitmq-server',
                'mongodb-server',
                'postgresql'
                ]

    services = ['actionrunner',
                'st2api',
                'sensor_container',
                'rules_engine',
                'mistral',
                'st2resultstracker',
                'rabbitmq-server',
                'mongodb',
                'postgres'
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
