# Oapy

A simple Python client for playing Gomoku on Aoire.

Full details of the Aoire protocol here: https://github.com/paul-nechifor/aoire

A publicly-hosted server is running here: http://hub.nechifor.net:8443

## Connecting

Run bootstrap to set up a virtualenv and install the required package.

To play a game, agree on a room name with the other player, and run something similar to the following:

```bash
> $ python gomoku.py --hostname hub.nechifor.net:8443 --user "Dumbot (by David)" --room funroom --ngames 1
```
