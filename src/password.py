from passlib.context import CryptContext

hash_ = '$pbkdf2-sha256$30000$79279z7nnNNaSynlHCOkVA$89iOmuu.uwwyiG6oGMSEgnENvri88cAWqk6/pFYQ5Ew'

pwd_context = CryptContext(
    schemes = ['pbkdf2_sha256'],
    default = 'pbkdf2_sha256',
    pbkdf2_sha256__default_rounds = 30000
)

def encrypt_pwd(pwd):
    return pwd_context.hash(pwd)

def verify_pwd(pwd, hash_):
    return pwd_context.verify(pwd, hash_)
