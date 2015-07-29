[![Circle CI](https://circleci.com/gh/rackspace-orchestration-templates/stackstorm-single/tree/master.png?style=shield)](https://circleci.com/gh/rackspace-orchestration-templates/stackstorm-single)
Description
===========

A template that deploys StackStorm onto a single Linux server.


Instructions
===========

#### Overview
Review the [StackStorm Overview](http://docs.stackstorm.com/overview.html)
to understand the use case for this tool. [StackStorm 101 Video](http://docs.stackstorm.com/video.html).

#### Quick Start
Review the [QuickStart Documentation](http://docs.stackstorm.com/start.html) for help with
getting started with StackStorm.

#### Logging in via SSH
The private key provided in the passwords section can be used to login as
root via SSH.  We have an article on how to use these keys with [Mac OS X and
Linux](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-linuxmac)
as well as [Windows using
PuTTY](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-windows).


Requirements
============
* A Heat provider that supports the following:
  * OS::Heat::SwiftSignal
  * OS::Heat::SwiftSignalHandle
  * OS::Nova::KeyPair
  * OS::Nova::Server
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `flavor`: The size is based on the amount of RAM for the provisioned server.
 (Default: 1 GB General Purpose v1)
* `image`: Server image used for all servers that are created as a part of this
deployment
 (Default: Ubuntu 14.04 LTS (Trusty Tahr) (PVHVM))
* `server_name`: The instance name (Default: StackStorm)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value of a specific output.

* `private_key`: SSH Private Key
* `server_ip`: Server IP
* `server_data`: Data from wait condition to report script status

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.
