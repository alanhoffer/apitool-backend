class EApiaryConfig:
    def __init__(self, 
                 configid,
                 apiaryid,
                 config_array):
        

        
        self.configid = configid
        self.apiaryid = apiaryid
        self.hive_quantity = config_array['hive_quantity']
        self.apiary_food_quantity = config_array['apiary_food_quantity']
        self.apiary_note_record =   config_array['apiary_note_record']
        self.apiary_electric_protection =   config_array['apiary_electric_protection']
        self.apiary_status =  config_array['apiary_status']
        self.health_flumetrine =    config_array['health_flumetrine']
        self.health_amitraz =  config_array['health_amitraz']
        self.health_oxalic = config_array['health_oxalic']
        self.antibiotic_oxytetracycline = config_array['antibiotic_oxytetracycline']
        self.suplements_promotorl = config_array['suplements_promotorl']
        self.suplements_beepower = config_array['suplements_beepower']
        self.apiary_mode = config_array['apiary_mode']


# class EApiaryConfig:
#     def __init__(self, 
#                  configid,
#                  apiaryid, 
#                  hive_quantity, 
#                  apiary_food_quantity,
#                  apiary_note_record, 
#                  apiary_electric_protection, 
#                  apiary_status,
#                  health_flumetrine, 
#                  health_amitraz, 
#                  health_oxalic, 
#                  antibiotic_oxytetracycline,
#                  suplements_promotorl,
#                  suplements_beepower,
#                  apiary_mode):
        

        
#         self.configid = configid
#         self.apiaryid = apiaryid  
#         self.hive_quantity = hive_quantity
#         self.apiary_food_quantity = apiary_food_quantity
#         self.apiary_note_record = apiary_note_record
#         self.apiary_electric_protection = apiary_electric_protection
#         self.apiary_status = apiary_status
#         self.health_flumetrine = health_flumetrine
#         self.health_amitraz = health_amitraz
#         self.health_oxalic = health_oxalic
#         self.antibiotic_oxytetracycline = antibiotic_oxytetracycline
#         self.suplements_promotorl = suplements_promotorl
#         self.suplements_beepower = suplements_beepower
#         self.apiary_mode = apiary_mode
        