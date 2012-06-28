import string
import random
import autofixture

def compare(self, other):
    if not(isinstance(other, self.__class__) and self._get_pk_val() == other._get_pk_val()) : return False
    old, new      = {}, {}
    dt_1, dt_2    = self.__dict__, other.__dict__
    excluded_keys = 'created', '_state', 'timestamp', 'user', 'uid', 'changed'
    for k,v in dt_1.items():
        try:
            if k in excluded_keys: continue
            if v != dt_2[k]:
                if type(v) is float:
                    return abs(v-dt_2[k]) < 1e-4
                else:
                    return False
        except KeyError: pass
    return True

def generate(self, instance):
    for field in instance._meta.fields:
        self.process_field(instance, field)
    return self.post_process_instance(instance)

autofixture.AutoFixture.generate = generate