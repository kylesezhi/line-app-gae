import webapp2
from google.appengine.ext import ndb
import db_definitions
import json
from datetime import datetime

class User(webapp2.RequestHandler):
    def get(self):
        q = db_definitions.User.query()
        keys = q.fetch(keys_only = True)
        results = {'ids': [x.id() for x in keys]}
        self.response.write(json.dumps(results))
        
    def post(self):
        """ Creates User
        
        POST variables:
            first_name - required
            last_name - required
            email - required
            password - required
            user_type - required: 'admin' or 'user' TODO
            classes
            """
        k = ndb.Key(db_definitions.User, self.app.config.get('admin-group'))
        u = db_definitions.User(parent=k)

        u.first_name = self.request.get('first_name', default_value=None)
        u.last_name = self.request.get('last_name', default_value=None)
        u.email = self.request.get('email', default_value=None)
        u.password = self.request.get('password', default_value=None)
        if None in (u.first_name, u.last_name, u.email, u.password):
            self.response.status = 400
            self.response.message = "Invalid request. Must provide all info for new user."
            return
        key = u.put()
        out = u.return_dict()
        self.response.write(json.dumps(out))
        return
        
    def delete(self, **kwargs):
        print('__DELETE__')
        print kwargs['user']
        if 'user' in kwargs:
            user_key = ndb.Key(db_definitions.User, self.app.config.get('user-group'), db_definitions.User, int(kwargs['user']))
            admin_key = ndb.Key(db_definitions.User, self.app.config.get('admin-group'), db_definitions.User, int(kwargs['user']))
            # print user_key
            # user = user_key.get()
            # TODO check for places in line!
            user_key.delete()
            admin_key.delete()
            # print admin_key
        return
        
class UserClass(webapp2.RequestHandler):
    def get(self):
        q = db_definitions.UserClass.query()
        keys = q.fetch(keys_only = True)
        results = {'ids': [x.id() for x in keys]}
        self.response.write(json.dumps(results))

class LineEntry(webapp2.RequestHandler):
    def get(self):
        q = db_definitions.LineEntry.query()
        keys = q.fetch(keys_only = True)
        results = {'ids': [x.id() for x in keys]}
        self.response.write(json.dumps(results))
        return
        
    def put(self, **kwargs):
        # Creates LineEntry
        
        # POST variables:
            # user = ndb.KeyProperty(required=True)
            # problem = ndb.StringProperty(required=True) # TODO
        
        # GET KEY FROM ID
        if 'user' in kwargs:
            user_key = ndb.Key(db_definitions.User, self.app.config.get('user-group'), db_definitions.User, int(kwargs['user']))
            print('__DEBUG__')
            print user_key
            
            line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))
            line = db_definitions.LineEntry(parent=line_key)
            line.user = user_key
            line.put()
            out = line.to_dict()
            self.response.write(json.dumps(out))
            return


            # line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))
            # line = db_definitions.LineEntry(parent=line_key)
            # line.user = user_key
            # line.put()
            # out = line.return_dict()
            # self.response.write(json.dumps(out))
        return

    def post(self):
        # Creates LineEntry
        
        # POST variables:
            # user = ndb.KeyProperty(required=True)
            # problem = ndb.StringProperty(required=True) # TODO
        
        # GET KEY FROM ID
        user_key = ndb.Key(db_definitions.User, int(self.request.get('user')))
        # user_id = self.request.get('user') # TODO this must be easier
        # q = db_definitions.User.query()
        # keys = q.fetch(keys_only = True)
        # user_key = ''
        # for key in keys:
        #     if int(key.id()) == int(user_id):
        #         user_key = key
        #         break
        
        print('__DEBUG__')
        print user_key

        line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))
        line = db_definitions.LineEntry(parent=line_key)
        line.user = user_key
        line.put()
        out = line.return_dict()
        self.response.write(json.dumps(out))
        return
                
        # INTERNET IDEAS
        # user_id = int(self.request.get('user'))
        # # key_parent = ndb.Key(db_definitions.User, self.app.config.get('default-group'))
        # resource = db_definitions.User.get_by_id(user_id)
        # print('__DEBUG__')
        # print resource
        
        # user_id = int(self.request.get('user'))
        # key_parent = ndb.Key(db_definitions.User, self.app.config.get('default-group'))
        # resource = db_definitions.User.get_by_id(user_id, parent = key_parent)
        # print('__DEBUG__')
        # print resource
        
        # results = [x.id() for x in keys if x.id() == user_id]
        # u = User()
        # x = db_definitions.User.get_by_id(5629499534213120)
        # q = db_definitions.User.all()
        # q.filter('__key__ =', 5629499534213120)
        # q.filter('__id__ =', 5629499534213120)
        # x = ndb.Key(db_definitions.User, 5629499534213120).get()
        
        # MIMIC API ABOVE
        # l = db_definitions.LineEntry()
        # u.first_name = self.request.get('first_name', default_value=None)
        # u.last_name = self.request.get('last_name', default_value=None)
        # u.email = self.request.get('email', default_value=None)
        # u.password = self.request.get('password', default_value=None)
        # if None in (u.first_name, u.last_name, u.email, u.password):
        #     self.response.status = 400
        #     self.response.message = "Invalid request. Must provide all info for new user."
        #     return
        # key = u.put()
        # out = u.return_dict()
        # self.response.write(json.dumps(out))
        # return
    
        # MIMIC ADMIN PAGE
        # user = user_key.get()
        # line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))
        # line = db_definitions.LineEntry(parent=line_key)
        # line.user = user_key
        # line.put()

        
        
        