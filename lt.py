#!/usr/bin/python

#--------
# imports
#--------

import cgi
import cgitb
import os
import re
import socket
import sys

# partial imports
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory


print ("here...")
