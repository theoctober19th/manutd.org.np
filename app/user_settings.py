AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = "optional"

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_BLACKLIST = ['united', 'manutd', 'manchester', 'reddevil', 'reddevils', 'manchesterunited', 'mufc']

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
         {
             'SCOPE': ['email', 'user_birthday', 'user_website'],
             # 'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
             'METHOD': 'oauth2',
             # 'LOCALE_FUNC': 'path.to.callable',
             'VERIFIED_EMAIL': False
         }
    }