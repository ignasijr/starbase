"""
This would be the code base for filtering in `starbase`. The `fetch_all_rows` method would be then cleaned
and would just return all rows (perhaps paginated results?)

Table instance.

>>> t = c.table('table1')

Using the QuerySet
---------------------

Query by row key, using regex

>>> results = t.filter(pk__eq__regex="^row_1.+")

Query by row key, using equal

>>> results = t.filter(column_1__qualifier_1__eq="john.doe@example.com")

When fireing one after another, joined by "AND". In the example below, both statements shall be satisfied.

>>> results = t.filter(pk__eq__regex="^row_1.+")
>>> results = results.filter(column_1__qualifier_1__eq="john.doe@example.com")

Finally, executing the query.

>>> results = results.fetch()

Using the `Q`
---------------------
Mainly for "OR" joins.

In the example below filters are joined by "OR". One of the two statements shall be satisfied.

>>> q1 = Q(pk__eq__regex="^row_1.+")
>>> q2 = Q(column_1__qualifier_1__eq="john.doe@example.com")
>>> results = t.filter(q1 | q2)

Finally, executing the query.

>>> results = results.fetch()
"""

class QuerySet(object):
    """
    QuerySet class.
    """

    def filter(self, *args, **kwargs):
        """
        Filter options.

        :return `QuerySet`.

        The following syntax examples would be supported (see the comments at the very top of the module).

        >>> results = t.filter(pk__eq__regex="^row_1.+")
        >>> results = t.filter(column_1__qualifier_1__eq="john.doe@example.com")
        
        Always "AND". "OR" filtering can be achieved by using the `Q`.

        >>> q1 = Q(pk__eq__regex="^row_1.+")
        >>> q2 = Q(column_1__qualifier_1__eq="john.doe@example.com")
        >>> results = t.filter(q1 | q2)
        """

    def _filter(self, *args, **kwargs):
        """
        More tunable low level usage filtering.

        See the http://hbase.apache.org/apidocs/org/apache/hadoop/hbase/filter/package-summary.html for the
        full list of filter options.

        The following argument would be acceptable (perhaps moved to some other function as ``_filter``, which
        would do low-level job).

        - `type` (str): Could be "RowFilter", "FamilyFilter", etc. (see the link above for all options).
        - `comparator_type` (str): Could be "BinaryComparator", "RegexStringComparator", etc. (see the link
          above for all options).
        """

    def fetch(self):
        """
        Fires the query. Would not be necessary if filters are lazy, but that's not that important in the
        initial versions of.
        """

class Q(object):
    """
    Q class for complex OR and AND statements (are they possible in HBase or do we have to make 2 separate 
    requests?).
    """
    AND = 'AND'
    OR = 'OR'
    default = AND

    def __init__(self, *args, **kwargs):
        """
        Possibly all the dirty work happens here.
        """
