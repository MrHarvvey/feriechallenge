from password_generator import PasswordGenerator

import clipboard

def get_random_pas(max_len):
    pwo = PasswordGenerator()
    # All properties are optional
    pwo.maxlen = max_len  # (Optional)
    pwo.minuchars = 1  # (Optional)
    pwo.minlchars = 1  # (Optional)
    pwo.minnumbers = 1  # (Optional)
    pwo.minschars = 1  # (Optional)
    return pwo.generate()

clipboard.copy(get_random_pas(10))




