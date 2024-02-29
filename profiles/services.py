from profiles._db import ProfileCollection
from profiles.models import Profile
from profiles.selectors import ProfileSelector


class ProfileService(ProfileCollection):
    def create_profile(self, profile: Profile) -> Profile | None:
        if ProfileSelector().get_user_by_email(profile.email):
            return
        profile.full_check()
        self.profile_table.insert_one(profile.to_dict())
        return profile
