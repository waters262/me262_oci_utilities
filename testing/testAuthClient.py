import oci
import sys
# appending the directory for modules
# Example:  python3 testAuthClient.py target_profile
# in the sys.path list
sys.path.append('../pyUtils/')       
 
# now we can import mod
from auth_client  import *

if __name__ == "__main__":

    print ('Number of arguments:', len(sys.argv), 'arguments.')
    args = sys.argv
    targetTenant = args[1]


    try:
        tenancyProfile = oci.config.from_file()[targetTenant]
        tenancyConfig = oci.config.from_file(profile_name=tenancyProfile)
    except:
        print(tenancyProfile + ' Profile not found in config file.  Using Default Profile')
        tenancyProfile = 'DEFAULT'
        tenancyConfig = oci.config.from_file()

    try:
        if tenancyConfig['auth_type'] == 'security_token' :
            config = ' --profile ' + tenancyConfig['auth_profile'] +  ' --auth security_token'
        else:
            config = ' --profile ' + tenancyConfig['auth_profile'] 
        print('CLI Auth config string is: ', config)
    except:
        config = ' --profile ' + tenancyProfile
        print('CLI config string is: ', config)
    #     print("Auth Profile"   ,tenancyConfig['auth_profile']) 

    print("Authentication Type is: ", tenancyConfig['auth_type'] )

    object_storage_client = get_client( client_type='ObjectStorageClient',    tenancyConfig=tenancyConfig)
    get_namespace_response = object_storage_client.get_namespace()
    print("\nChecking Authentication ....")
    print("Namespace is: ",  get_namespace_response.data)


    client = get_client( client_type='IdentityClient',    tenancyConfig=tenancyConfig)
    compts = client.list_compartments(compartment_id=tenancyConfig['tenancy']\
                                    ,compartment_id_in_subtree=True)

    network = get_client(client_type='VirtualNetworkClient',    tenancyConfig=tenancyConfig)
    database_client = get_client(client_type='DatabaseClient',    tenancyConfig=tenancyConfig)
    compute_client = get_client(client_type='ComputeClient',    tenancyConfig=tenancyConfig)

    # network = oci.core.VirtualNetworkClient({'region': ssoRegion}, signer=signer)

    print("Network var type: ", type(network))
    print("Compute var type: ", type(compute_client))
    print("Database var type: ", type(database_client))
    print(network)


#    signer =  oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

#    healthchecks_client = oci.healthchecks.HealthChecksClient({}, signer=signer)

#    apigateway_client = oci.apigateway.GatewayClient({}, signer=signer)
    print('Running on Tenant: ' + tenancyProfile )


