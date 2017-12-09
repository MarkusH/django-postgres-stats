from django.contrib.admin.views.main import ORDER_VAR
from django.contrib.auth.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render

from .metrics import registry as metrics_registry


@staff_member_required
def metrics_view(request, name):

    try:
        Metric = metrics_registry[name]
    except KeyError:
        raise Http404

    ordering = request.GET.get(ORDER_VAR)
    metric = Metric(ordering)

    return render(request, 'postgres_metrics/table.html', {
        'metric': metric,
        'results': metric.get_data(),
    })
