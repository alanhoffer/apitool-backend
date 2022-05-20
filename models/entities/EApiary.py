class EApiary():
    def __init__(self,
                 id,
                 userid,
                 name,
                 profile_img="https://img.freepik.com/vector-gratis/apicultor-traje-proteccion-panales-abejas-voladoras-jardin-abejas_313242-149.jpg?w=2000",
                 note_text="",
                 created_at="0",
                 updated_at="0",
                 hives_quantity=0,
                 food_quantity=0,
                 eprotection_status=False,
                 status=0,
                 flumetrine_quantity=0,
                 amitraz_quantity=0,
                 oxalic_quantity=0,
                 oxytetracycline_quantity=0,
                 suplements_promotorl=0,
                 suplements_beepower=0,
                 ):
        
        self.id = id
        self.name = name
        self.userid = userid
        self.profile_img = profile_img
        self.note_text = note_text
        self.created_at = created_at
        self.updated_at = updated_at
        self.hives_quantity = hives_quantity
        self.food_quantity = food_quantity
        self.eprotection_status = eprotection_status
        self.status = status
        self.flumetrine_quantity = flumetrine_quantity
        self.amitraz_quantity = amitraz_quantity
        self.oxalic_quantity = oxalic_quantity
        self.oxytetracycline_quantity = oxytetracycline_quantity
        self.suplements_promotorl = suplements_promotorl
        self.suplements_beepower = suplements_beepower
