import datetime

from django.conf import settings
from django.shortcuts import render
from django.views import View

class TasksTimes(View):

    def get(self, request):
        data = dict((("%s" % s['_id'], s['total']) for s in self.stats))

        return render(request, 'monitor/prometheus_data.html', {"data": data})

    
    @property
    def stats(self):
        
        stats = settings.MONGOANALYTICSDB.nbanalytics.feed_fetches.aggregate([{
            "$match": {
                "date": {
                    "$gt": datetime.datetime.now() - datetime.timedelta(minutes=5),
                },
            },
        }, {
            "$group": {
                "_id"   : "$server",
                "total" : {"$avg": "$total"},
            },
        }])
        
        return list(stats)