from django.contrib.admin import AdminSite

from django.contrib.auth.models import User,Group


from  bmmiici.models import Doctor, Patient

class MyAdminSite(AdminSite):
    site_header = 'B-MMIICI administration'

admin_site = MyAdminSite(name='myadmin')
#admin_site.register(User)
#admin_site.register(Group)
admin_site.register(Doctor)
admin_site.register(Patient)

from django.contrib.auth.admin import UserAdmin, GroupAdmin

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
