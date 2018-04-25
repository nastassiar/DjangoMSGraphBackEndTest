# The client ID (register app in Azure AD to get this value)
id = '9ccd7934-3aa2-4763-b4e4-261d443d47bb'
# The client secret (register app in Azure AD to get this value)
secret = 'T8louT5Xsb44B3Op6lpNEEIPhT7Uu1Yfa5v6XTzIXKk='

class client_registration:
    @staticmethod
    def client_id():
        return id
        
    @staticmethod
    def client_secret():
        return secret