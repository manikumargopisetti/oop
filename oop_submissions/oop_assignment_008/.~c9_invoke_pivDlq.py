class Animals:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months !=1:
            raise ValueError('Invalid vlaue for field age_in_months: {}'.format(age_in_months))
        if required_food_in_kgs <= 0:
            raise ValueError('Invalid vlaue for field required_food_in_kgs: {}'.format(required_food_in_kgs))
        self._age_in_months= age_in_months
        self._breed= breed
        self._required_food_in_kgs=required_food_in_kgs
        
    @property
    def age_in_months(self):
            return self._age_in_months
            