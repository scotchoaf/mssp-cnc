# Activating the CNC Environment

* Click on the lock image (upper right corner)

* Enter the master passphrase

* If an existing environment, choose ```Load``` to activate

### Creating a New Environment

* Choose an existing Environment and select ```Clone```

* Enter a name and description

* Edit values by adding the existing Key name and associcated Value

* Submit and new the updated secrets list for the Key value

* When all values updated, you can ```Load``` as an active enviroment


### Viewing the Environments

* Click on the username (upper right of window)

* Select ```Environments```

* Configure or Load as required


# Loading a Configuration

* Activate the CNC environment to define which device is used for configuration

* Choose the menu option

    - Basic Internet Gateway: Loads G-S-B configuration to Panorama

    - Basic Internet Gateway PAN-OS: Loads G-S-B config to a firewall

    - GSB SET commands: Text render of set commands for copy/paste to a firewall

    - Global Protect Cloud Service: config new cloud instance or new remote network

    - GPCS CPE Helper Configs: text render for CPE-side device configs

* Enter form values and step through the config panels

* Submit of the environment API config device will initiate an API config push

