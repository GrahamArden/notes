# SSH tunnel

A quick and dirty tutorial on how to use  a ssh tunnel to view a web page displayed only on localhost on a remote server. This is useful for setting up Syncthing on a headless box (e.g. a VPS):

Let’s say you have a Linux laptop, and the headless Linux box where you want to run syncthing has a working hostname of “headless”, (within your LAN). The username on the headless box we’ll run Syncthing as is called “admsync”.

On the laptop, in a terminal:

```bash

ssh -L 9988:localhost:8384 admsync@headless
```

Then once ssh’ed in as admsync, run the syncthing command.

Now on your laptop, in a web browser, visit the URL:

```bash
https://localhost:9988
```
…and you should see the Syncthing GUI from the headless box.

Note: on the headless box, in /etc/ssh/sshd_config, “AllowTcpForwarding” must not be “no”, for this tunneling to work.
