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
                        
    if client_type == 'VirtualNetworkClient':
        if auth_type == 'security_token':  # Typical web browser authentication
            return oci.core.VirtualNetworkClient(
                            {'region':oci.config.from_file(profile_name=tenancyProfile)['region']},
                            signer=token_signer(tenancyConfig['auth_profile'])  )
        elif auth_type == 'auth_token':   # Set up with authentication token
            return oci.core.VirtualNetworkClient(tenancyConfig)
        elif auth_type == 'instance_principal': # Instance principal
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.core.VirtualNetworkClient({},signer=signer)
        elif auth_type == 'obo':  # Cloud Shell
            delegation_token = open('/etc/oci/delegation_token', 'r').read()
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
               delegation_token=delegation_token)
            return oci.core.VirtualNetworkClient({},signer=signer)
              
    if client_type == 'ComputeClient':
        if auth_type == 'security_token':  # Typical web browser authentication
            return oci.core.ComputeClient(
                            {'region':oci.config.from_file(profile_name=tenancyProfile)['region']},
                            signer=token_signer(tenancyConfig['auth_profile'])  )
        elif auth_type == 'auth_token':   # Set up with authentication token
            return oci.core.ComputeClient(tenancyConfig)
        elif auth_type == 'instance_principal': # Instance principal
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.core.ComputeClient({},signer=signer)
        elif auth_type == 'obo':  # Cloud Shell
            delegation_token = open('/etc/oci/delegation_token', 'r').read()
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
               delegation_token=delegation_token)
            return oci.core.ComputeClient({},signer=signer)
              
    if client_type == 'DatabaseClient':
        if auth_type == 'security_token':  # Typical web browser authentication
            return oci.database.DatabaseClient(
                            {'region':oci.config.from_file(profile_name=tenancyProfile)['region']},
                            signer=token_signer(tenancyConfig['auth_profile'])  )
        elif auth_type == 'auth_token':   # Set up with authentication token
            return oci.database.DatabaseClient(tenancyConfig)
        elif auth_type == 'instance_principal': # Instance principal
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.database.DatabaseClient({},signer=signer)
        elif auth_type == 'obo':  # Cloud Shell
            delegation_token = open('/etc/oci/delegation_token', 'r').read()
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
               delegation_token=delegation_token)
            return oci.database.DatabaseClient({},signer=signer)
              
    if client_type == 'FileStorageClient':
        if auth_type == 'security_token':  # Typical web browser authentication
            return oci.file_storage.FileStorageClient(
                            {'region':oci.config.from_file(profile_name=tenancyProfile)['region']},
                            signer=token_signer(tenancyConfig['auth_profile'])  )
        elif auth_type == 'auth_token':   # Set up with authentication token
            return oci.file_storage.FileStorageClient(tenancyConfig)
        elif auth_type == 'instance_principal': # Instance principal
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.file_storage.FileStorageClient({},signer=signer)
        elif auth_type == 'obo':  # Cloud Shell
            delegation_token = open('/etc/oci/delegation_token', 'r').read()
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
               delegation_token=delegation_token)
            return oci.file_storage.FileStorageClient({},signer=signer)
              
              
    if client_type == 'BlockStorageClient':
        if auth_type == 'security_token':  # Typical web browser authentication
            return oci.core.BlockstorageClient(
                            {'region':oci.config.from_file(profile_name=tenancyProfile)['region']},
                            signer=token_signer(tenancyConfig['auth_profile'])  )
        elif auth_type == 'auth_token':   # Set up with authentication token
            return oci.core.BlockstorageClient(tenancyConfig)
        elif auth_type == 'instance_principal': # Instance principal
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.core.BlockstorageClient({},signer=signer)
        elif auth_type == 'obo':  # Cloud Shell
            delegation_token = open('/etc/oci/delegation_token', 'r').read()
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
               delegation_token=delegation_token)
            return oci.core.BlockstorageClient({},signer=signer)

              
    if client_type == 'BastionClient':
        if auth_type == 'security_token':  # Typical web browser authentication
            return oci.bastion.BastionClient(
                            {'region':oci.config.from_file(profile_name=tenancyProfile)['region']},
                            signer=token_signer(tenancyConfig['auth_profile'])  )
        elif auth_type == 'auth_token':   # Set up with authentication token
            return oci.bastion.BastionClient(tenancyConfig)
        elif auth_type == 'instance_principal': # Instance principal
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.bastion.BastionClient({},signer=signer)
        elif auth_type == 'obo':  # Cloud Shell
            delegation_token = open('/etc/oci/delegation_token', 'r').read()
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
               delegation_token=delegation_token)
            return oci.bastion.BastionClient({},signer=signer)

    return ['MonitoringClient','ObjectStorageClient','IdentityClient','VirtualNetworkClient','ComputeClient','DatabaseClient','FileStorageClient','BlockStorageClient','BastionClient']

