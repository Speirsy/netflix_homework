class Account:
    def __init__(self, name_first, name_last, email):

        self.name_first = name_first
        self.name_last =  name_last
        self.email = email
        self.profiles = []




    def number_of_profiles(self): 
        return len(self.profiles)

    def add_profile(self, profile):
        self.profiles.append(profile)  

    def remove_profile(self, profile_to_remove):
        self.profiles.remove(profile_to_remove)    

#   def list_of_profiles(self.profiles_to_list):
#         return self.profiles  
