#
# ociutils/token_signer
#
import oci
def token_signer(securityProfile):
    securityConfig = oci.config.from_file(profile_name=securityProfile)
    token_file = securityConfig['security_token_file']
    token = None
    with open(token_file, 'r') as f:
         token = f.read()    
    private_key = oci.signer.load_private_key_from_file(securityConfig['key_file'])
    return oci.auth.signers.SecurityTokenSigner(token, private_key) 
#
