from google.auth.credentials import Credentials


class FirebaseCredentials(Credentials):
    """Firebase Credentials, stores the authentication tokens"""
    token = None
    refresh_token = None

    def __init__(self, token, refresh_token):
        super().__init__()
        self.token = token
        self.refresh_token = refresh_token

    def apply(self, headers, token=None):
        """Apply the token to the authentication header.

        Args:
            headers (Mapping): The HTTP request headers.
            token (Optional[str]): If specified, overrides the current access
                token.
        """

        headers['authorization'] = 'Bearer {}'.format(self.token)

    def refresh(self, request):
        pass
