#!/usr/bin/env python
'''
    intersight_example.py is a stepping stone for anyone who wants to get started with the
    Cisco Intersight API. What it does in its simplest form is just to present a brief list of
    the hardware you've claimed in Intersight, and some useful information.

    To get started you need to configure environment variables pointing out files carrying your
    credentials to intersight.

    In a bash environment, this can be done like this:
        export INTERSIGHT_PRIVATE_KEY_PATH="./intersight/secret_key"
        export INTERSIGHT_PUBLIC_KEY_PATH="./intersight/api_key"

    After that ha been completed, fire up the program by issuing `python intersight_example.py`

    If you have any other intersight operation that you would like to see demonstrated in this
    program, don't hesitate to contact me and I'll see what I can do about it.

    Also, this program has only been tested in python3.

    sample output:
        C220-WXY12345PZB
            Number of cpus: 2
            Available memory: 131072
            System serial number: WXY12345PZB
            tag: TIME-MACHEENE
            Power state: on
            Mgmt ip: 192.168.1.5


'''
__author__ = 'Rickard Ostman'
__copyright__ = 'Copyright 2020, Miradot AB'
__license__ = 'MIT'
__version__ = '1.0'
__maintainer__ = 'Rickard Ostman'
__email__ = 'rickard.ostman@miradot.se'
__status__ = 'Prototype'

import intersight_rest
import traceback
import os

def query_intersight(options):
    '''
        This method queries intersight using supplied parameters

        Args:
            options (dict): Holding the parameters needed to perform an intersight query
        Returns:
            Whatever intersight_rest.intersight_call does
        Raises:
            Nothing. It will just inform the user there was an error and terminate the program
    '''
    try:
        query_results = intersight_rest.intersight_call(**options)
        return query_results.json()
    except Exception as e:
        print('unknown error from intersight_rest - exiting: {}'.format(traceback.format_exc()))
        exit()

def get_data_from_intersight(apipath, query_params={}):
    '''
        This method retrieves data from intersight using a query_method

        Args:
            intersight_conn (intersight_rest): a reference to the intersight_rest module
            apipath (string): a path to a resource in the intersight REST api
            query_params (dict): additional parameters supported by intersight_rest
        Returns:
            List of Dicts holding information from the intersight api
    '''
    options = {
        "http_method": "get",
        "resource_path": apipath,
        "query_params": query_params
    }

    return query_intersight(options)

def main():

    # Gather our credentials for intersight
    private_key_path = os.environ.get('INTERSIGHT_PRIVATE_KEY_PATH', None)
    public_key_path = os.environ.get('INTERSIGHT_PUBLIC_KEY_PATH', None)

    # check that theyre set, or remind the user
    if not(private_key_path and public_key_path):
        print('Please set a path to your intersight credential files using environment variables:')
        print('\t- INTERSIGHT_PRIVATE_KEY_PATH')
        print('\t- INTERSIGHT_PUBLIC_KEY_PATH')
        exit()

    # try applying our credentials to intersight_rest
    try:
        private_key = open(private_key_path, "r") .read()
        intersight_rest.set_private_key(private_key)

        public_key = open(public_key_path, "r") .read()
        intersight_rest.set_public_key(public_key)
    except FileNotFoundError:
        print('There was a problem reading your credentials - please verify their paths')
        exit()
    except Exception as e:
        print('There was an error using your credentials: {}'.format(str(e)))

    # now that we're good to go, get the data we want to present to our user
    compute_physicalsummery = get_data_from_intersight('/compute/PhysicalSummaries', query_params={})

    # now present it
    for entry in compute_physicalsummery['Results']:
        print('{}'.format(entry['Name'].lstrip()))
        print('\tNumber of cpus: {}'.format(entry['NumCpus']))
        print('\tAvailable memory: {}'.format(entry['AvailableMemory']))
        print('\tSystem serial number: {}'.format(entry['Serial']))
        print('\ttag: {}'.format(entry['AssetTag']))
        print('\tPower state: {}'.format(entry['OperPowerState']))
        print('\tMgmt ip: {}'.format(entry['MgmtIpAddress']))
        print('')


if __name__ == '__main__':
    main()
