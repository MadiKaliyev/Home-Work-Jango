from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    phone_regex = re.compile(
        r'(\+?\d{1,3})?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
    )
    if not phone_regex.fullmatch(value):
        raise ValidationError(f'{value} не является допустимым номером телефона')

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)
ALLOWED_DOMAINS = ['example.com', 'example.org']

def validate_email(value):
    if not EMAIL_REGEX.fullmatch(value):
        raise ValidationError(f'{value} не является допустимым email адресом')
    
    domain = value.split('@')[1]
    if domain not in ALLOWED_DOMAINS:
        raise ValidationError(f'Email домен {domain} не допустим. Допустимые домены: {", ".join(ALLOWED_DOMAINS)}')

def validate_hashtag(value):
    hashtag_regex = re.compile(r'^#\w+$')
    if not hashtag_regex.fullmatch(value):
        raise ValidationError(f'{value} не является допустимым хештегом')
