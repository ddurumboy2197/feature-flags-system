class FeatureFlags:
    def __init__(self):
        self.flags = {}

    def add_flag(self, name, value):
        self.flags[name] = value

    def get_flag(self, name):
        return self.flags.get(name)

    def set_flag(self, name, value):
        self.flags[name] = value

    def delete_flag(self, name):
        if name in self.flags:
            del self.flags[name]


class FeatureFlagsSystem:
    def __init__(self):
        self.feature_flags = FeatureFlags()

    def enable_feature(self, name):
        self.feature_flags.set_flag(name, True)

    def disable_feature(self, name):
        self.feature_flags.set_flag(name, False)

    def is_feature_enabled(self, name):
        return self.feature_flags.get_flag(name) or False

    def get_feature_status(self, name):
        return self.feature_flags.get_flag(name)


# Misol
feature_flags_system = FeatureFlagsSystem()

# Funksiyani qo'shish
feature_flags_system.enable_feature('funktsiya1')
feature_flags_system.enable_feature('funktsiya2')

# Funksiyani o'chirish
feature_flags_system.disable_feature('funktsiya1')

# Funksiya holati
print(feature_flags_system.is_feature_enabled('funktsiya1'))  # True
print(feature_flags_system.is_feature_enabled('funktsiya2'))  # True
print(feature_flags_system.is_feature_enabled('funktsiya3'))  # False
