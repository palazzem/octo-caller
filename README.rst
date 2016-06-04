===========
octo-caller
===========

Proof of concept that uses `Kafka`_ to dispatch messages between crawlers and executors.

**The current state of the project is not so interesting, so please come here later**

.. _Kafka: http://kafka.apache.org/

Getting started
---------------

Without worring about creating a `Kafka`_ cluster, you can launch a working (oversimplified)
single node that executes Zookeeper with a broker. To keep things easier, the ``Vagrantfile``
available in the repository will download a Centos 7.2 box and will use Ansible for the
provisioning::

    $ vagrant up

Without doing anything else, you have Kafka up and running in your system with the IP address
``10.0.30.10``.

Python producer and consumer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the ``octo/`` folder you can find a ``fake_crawler.py`` and a ``fake_processor.py`` scripts
that launches a producer and a consumer. They both use ``MsgPack`` as a transmission format
so that complex data may be moved quickly from one node to another.

To launch the producer, create a virtualenv with the proper requirements::

    $ mktmpenv && cd -
    $ pip install -r requirements/requirements.txt
    $ python octo/fake_crawler.py

    # launch the following in another shell
    $ python octo/fake_processor.py
