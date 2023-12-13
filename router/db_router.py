# class AdminRouter:
#     route_app_labels = {'contenttypes', 'auth', 'admin', 'sessions'}
        
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'admin_db'
#         return None
    
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'admin_db'
#         return None
    
#     def allow_relation(self, obj1, obj2, **hints):
#         if obj1._meta.app_label in self.route_app_labels and obj2._meta.app_label in self.route_app_labels:
#             return True
#         return None
    
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'admin_db'
#         return None
    
class UserRouter:
    route_app_labels = {'userapp'}
    # exclude_app_labels = {'contenttypes', 'auth', 'admin', 'sessions'}
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user_db'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app_labels and obj2._meta.app_label in self.route_app_labels:
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'admin':
            return False
        elif app_label == 'auth' or app_label == 'contenttypes' or app_label == 'sessions':
            return False
        return db == 'user_db'