Summary Statistics for Utilization
==================================

At the time we process primary power consumption data to determine usage epsides, we also pre-calculate simple
summary statistics in the database.  This is meant to speed rendering of common graphs and visualizations in the
user interface, so that long lists of episode start and end times do not have to be further processes to display a
simple statistic like, "asset X was used for 22 minutes total today", or "asset Y was used 2.5% of business hours
during the last 7 days".

Such statistics are certainly not complex analytics, and exclude trending and pattern analysis over time.  Those kinds
of analyses need to be done outside the context of primary utilization analysis, because at any given moment we will
typically only have a small window of data in the services that employ this library code.


.. toctree::
    :maxdepth: 4

    utilization_statistics
    statistics_processor
    statistics_implementations
    statistics_utilities
