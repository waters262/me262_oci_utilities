import oci
def get_client(client_type='IdentityClient',auth_type='auth_token',tenancyConfig=" "):

    if client_type == 'MonitoringClient':
        if auth_type == 'security_token':  # Typical web browser authentication
            return oci.monitoring.MonitoringClient(
                            {'region':oci.config.from_file(profile_name=tenancyProfile)['region']},
                            signer=token_signer(tenancyConfig['auth_profile'])  )
        elif auth_type == 'auth_token':   # Set up with authenti cation token
            return oci.monitoring.MonitoringClient(tenancyConfig)
        elif auth_type == 'instance_principal': # Instance principal
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.monitoring.MonitoringClient({},signer=signer)
        elif auth_type == 'obo':  # Cloud Shell
            delegation_token = open('/etc/oci/delegation_token', 'r').read()
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
               delegation_token=delegation_token)
            return oci.monitoring.MonitoringClient({},signer=signer)
        
    if client_type == 'IdentityClient':
        if auth_type == 'security_token':  # Typical web browser authentication
            return oci.identity.IdentityClient(
                            {'region':oci.config.from_file(profile_name=tenancyProfile)['region']},
                            signer=token_signer(tenancyConfig['auth_profile'])  )
        elif auth_type == 'auth_token':   # Set up with authentication token
            return oci.identity.IdentityClient(tenancyConfig)
        elif auth_type == 'instance_principal': # Instance principal
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.identity.IdentityClient({},signer=signer)
        elif auth_type == 'obo':  # Cloud Shell
            delegation_token = open('/etc/oci/delegation_token', 'r').read()
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
               delegation_token=delegation_token)
            return oci.identity.IdentityClient({},signer=signer)
            
    if client_type == 'ObjectStorageClient':
        if auth_type == 'security_token':  # Typical web browser authentication
            return oci.object_storage.ObjectStorageClient(
                            {'region':oci.config.from_file(profile_name=tenancyProfile)['region']},
                            signer=token_signer(tenancyConfig['auth_profile'])  )
        elif auth_type == 'auth_token':   # Set up with authentication token
            return oci.object_storage.ObjectStorageClient(tenancyConfig)
        elif auth_type == 'instance_principal': # Instance principal
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.object_storage.ObjectStorageClient({},signer=signer)
        elif auth_type == 'obo':  # Cloud Shell
            delegation_token = open('/etc/oci/delegation_token', 'r').read()
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
               delegation_token=delegation_token)
            return oci.object_storage.ObjectStorageClient({},signer=signer)
                        
            
                
    return ['MonitoringClient','ObjectStorageClient','IdentityClient']
