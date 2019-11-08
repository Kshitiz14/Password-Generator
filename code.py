import random
import string

strength = input("How do you want your password? Strong or Weak.").lower()
                 
if strength == 'strong':
    def pw_generator(size=7, chars=string.ascii_letters+string.digits+string.punctuation):
        return ''.join(random.SystemRandom().choice(chars) for n in range(size))

else:
    def pw_generator(size=3, chars=string.ascii_letters+string.digits+string.punctuation):
        return ''.join(random.SystemRandom().choice(chars) for n in range(size))

pw_generator()
