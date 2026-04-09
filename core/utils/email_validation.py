from email_validator import validate_email, EmailNotValidError

def email_validation(email: str) -> bool:
    if email is not None:
        try:
            validate_email(email, check_deliverability = False)
            return True
        except EmailNotValidError:
            return False
    raise ValueError("No email has been provided !")