# REGEX VARIABLES

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

PASSWORD_REGEX =  r'^[A-Za-z0-9@#$%^&+=]{8,}$'


USERNAME_REGEX =  r'^[a-zA-Z0-9_.-]+$'


NAMESURNAME_REGEX =  r'([A-Z]\w+(?=[\s\-][A-Z])(?:[\s\-][A-Z]\w+)+)'


PHONE_REGEX =  r'^(\([0-9]{1,4}$\) ?|[0-9]{1,4}-)[0-9]{6,10}$'


CITY_REGEX =  r"^([a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$"
