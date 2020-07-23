from django.contrib import admin
from .models import Post, Timeline, Homepic, Member, Committee

admin.site.register(Post)
admin.site.register(Timeline)
admin.site.register(Member)
admin.site.register(Homepic)
admin.site.register(Committee)
