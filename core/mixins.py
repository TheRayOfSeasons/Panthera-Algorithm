from .panthera_core import Gender


class NameMapperMixin(object):
    """
    A mixin for handling custom fragments
    for specific pairs of panthera.
    """

    self_with_male_map = {} # for male partner and female offspring
    self_with_female_map = {} # for female partner and male offspring

    _mappings = {
        # if self is female and partner is male
        Gender.MALE: self_with_male_map,
        # if self is male and partner is female
        Gender.FEMALE: self_with_female_map
    }

    def get_name_fragments(self, partner):
        fragments = super().get_name_fragments(partner)
        data_map = self._mappings[partner.gender]
        partner_name = partner.name
        custom_fragments = data_map[partner_name]
        if custom_fragments:
            if custom_fragments.get('prefix'):
                fragments['prefix'] = custom_fragments.get('prefix')
            if custom_fragments.get('suffix'):
                fragments['suffix'] = custom_fragments.get('suffix')
        return fragments