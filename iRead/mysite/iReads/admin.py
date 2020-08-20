from django.contrib import admin

# Register your models here.

from iReads.models import StoriesCat
from iReads.models import StoriesThreads
from iReads.models import DiscussionCat
from iReads.models import DiscussionThreads
from iReads.models import Comment,Contact


admin.site.register(StoriesCat)
admin.site.register(StoriesThreads)
admin.site.register(DiscussionCat)
admin.site.register(DiscussionThreads)
admin.site.register(Comment)
admin.site.register(Contact)