"""The main Space in the :mod:`~basiclife.BasicTerm_S` model.

:mod:`~basiclife.BasicTerm_S.Projection` is the only Space defined
in the :mod:`~basiclife.BasicTerm_S` model, and it contains
all the logic and data used in the model.

.. rubric:: Parameters and References

(In all the sample code below,
the global variable ``Projection`` refers to the
:mod:`~basiclife.BasicTerm_S.Projection` Space.)

Attributes:

    point_id: The ID of the selected model point.
        ``point_id`` is defined as a Reference, and its value
        is used for determining the selected model point.
        By default, ``1`` is assigned. To select another model point,
        assign its model point ID to it::

            >>> Projection.point_id = 2

        ``point_id`` is also defined as the parameter of the
        :mod:`~basiclife.BasicTerm_S.Projection` Space,
        which makes it possible to create dynamic child space
        for multiple model points::

            >>> Projection.parameters
            ('point_id',)

            >>> Projection[1]
            <ItemSpace BasicTerm_S.Projection[1]>

            >>> Projection[2]
            <ItemSpace BasicTerm_S.Projection[2]>

        .. seealso::

           * :attr:`model_point_table`
           * :func:`model_point`

    model_point_table: All model point data as a DataFrame.
        The sample model point data was generated by
        *generate_model_points.ipynb* included in the library.
        The DataFrame has an index named ``point_id``,
        and :func:`model_point` returns a record as a Series
        whose index value matches :attr:`point_id`.
        The DataFrame has columns labeled ``age_at_entry``,
        ``sex``, ``policy_term``, ``policy_count``
        and ``sum_assured``.
        Cells defined in :mod:`~basiclife.BasicTerm_S.Projection`
        with the same names as these columns return
        the corresponding column's values for the selected model point.
        (``policy_count`` is not used by default.)

        .. code-block::

            >>> Projection.model_poit_table
                       age_at_entry sex  policy_term  policy_count  sum_assured
            point_id
            1                    47   M           10             1       622000
            2                    29   M           20             1       752000
            3                    51   F           10             1       799000
            4                    32   F           20             1       422000
            5                    28   M           15             1       605000
                            ...  ..          ...           ...          ...
            9996                 47   M           20             1       827000
            9997                 30   M           15             1       826000
            9998                 45   F           20             1       783000
            9999                 39   M           20             1       302000
            10000                22   F           15             1       576000

            [10000 rows x 5 columns]

        The DataFrame is saved in the Excel file *model_point_table.xlsx*
        placed in the model folder.
        :attr:`model_point_table` is created by
        Projection's `new_pandas`_ method,
        so that the DataFrame is saved in the separate file.
        The DataFrame has the injected attribute
        of ``_mx_dataclident``::

            >>> Projection.model_point_table._mx_dataclient
            <PandasData path='model_point_table.xlsx' filetype='excel'>

        .. seealso::

           * :attr:`point_id`
           * :func:`model_point`
           * :func:`age_at_entry`
           * :func:`sex`
           * :func:`policy_term`
           * :func:`sum_assured`


    disc_rate_ann: Annual discount rates by duration as a pandas Series.

        .. code-block::

            >>> Projection.disc_rate_ann
            year
            0      0.00000
            1      0.00555
            2      0.00684
            3      0.00788
            4      0.00866

            146    0.03025
            147    0.03033
            148    0.03041
            149    0.03049
            150    0.03056
            Name: disc_rate_ann, Length: 151, dtype: float64

        The Series is saved in the Excel file *disc_rate_ann.xlsx*
        placed in the model folder.
        :attr:`disc_rate_ann` is created by
        Projection's `new_pandas`_ method,
        so that the Series is saved in the separate file.
        The Series has the injected attribute
        of ``_mx_dataclident``::

            >>> Projection.disc_rate_ann._mx_dataclient
            <PandasData path='disc_rate_ann.xlsx' filetype='excel'>

        .. seealso::

           * :func:`disc_rate_mth`
           * :func:`disc_factors`

    mort_table: Mortality table by age and duration as a DataFrame.
        See *basic_term_sample.xlsx* included in this library
        for how the sample mortality rates are created.

        .. code-block::

            >>> Projection.mort_table
                        0         1         2         3         4         5
            Age
            18   0.000231  0.000254  0.000280  0.000308  0.000338  0.000372
            19   0.000235  0.000259  0.000285  0.000313  0.000345  0.000379
            20   0.000240  0.000264  0.000290  0.000319  0.000351  0.000386
            21   0.000245  0.000269  0.000296  0.000326  0.000359  0.000394
            22   0.000250  0.000275  0.000303  0.000333  0.000367  0.000403
            ..        ...       ...       ...       ...       ...       ...
            116  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
            117  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
            118  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
            119  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
            120  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000

            [103 rows x 6 columns]

        The DataFrame is saved in the Excel file *mort_table.xlsx*
        placed in the model folder.
        :attr:`mort_table` is created by
        Projection's `new_pandas`_ method,
        so that the DataFrame is saved in the separate file.
        The DataFrame has the injected attribute
        of ``_mx_dataclident``::

            >>> Projection.mort_table._mx_dataclient
            <PandasData path='mort_table.xlsx' filetype='excel'>

        .. seealso::

           * :func:`mort_rate`
           * :func:`mort_rate_mth`

    np: The `numpy`_ module.
    pd: The `pandas`_ module.

.. _numpy:
   https://numpy.org/

.. _pandas:
   https://pandas.pydata.org/

.. _new_pandas:
   https://docs.modelx.io/en/latest/reference/space/generated/modelx.core.space.UserSpace.new_pandas.html

"""

from modelx.serialize.jsonvalues import *

_formula = lambda point_id: None

_bases = []

_allow_none = None

_spaces = []

# ---------------------------------------------------------------------------
# Cells

def age(t):
    """The attained age at time t.

    Defined as::

        age_at_entry() + duration(t)

    .. seealso::

        * :func:`age_at_entry`
        * :func:`duration`

    """
    return age_at_entry() + duration(t)


def age_at_entry():
    """The age at entry of the selected model point

    The element labeled ``age_at_entry`` of the Series returned by
    :func:`model_point`.
    """
    return model_point()["age_at_entry"]


def check_pv_net_cf():
    """Check present value summation

    Check if the present value of :func:`net_cf` matches the
    sum of the present values each cashflows.
    Returns the check result as :obj:`True` or :obj:`False`.

     .. seealso::

        * :func:`net_cf`
        * :func:`pv_net_cf`

    """

    import math
    res = sum(list(net_cf(t) for t in range(proj_len())) * disc_factors()[:proj_len()])

    return math.isclose(res, pv_net_cf())


def claim_pp(t):
    """Claim per policy

    The claim amount per plicy. Defaults to :func:`sum_assured`.
    """
    return sum_assured()


def claims(t):
    """Claims

    Claims during the period from ``t`` to ``t+1`` defined as::

        claim_pp(t) * pols_death(t)

    .. seealso::

        * :func:`claim_pp`
        * :func:`pols_death`

    """
    return claim_pp(t) * pols_death(t)


def commissions(t): 
    """Commissions

    By default, 100% premiums for the first year, 0 otherwise.

    .. seealso::

        * :func:`premiums`
        * :func:`duration`

    """
    return premiums(t) if duration(t) == 0 else 0


def disc_factors():
    """Discount factors.

    Vector of the discount factors as a Numpy array. Used for calculating
    the present values of cashflows.

    .. seealso::

        :func:`disc_rate_mth`
    """
    return np.array(list((1 + disc_rate_mth()[t])**(-t) for t in range(proj_len())))


def disc_rate_mth():
    """Monthly discount rate

    Nummpy array of monthly discount rates from time 0 to :func:`proj_len` - 1
    defined as::

        (1 + disc_rate_ann)**(1/12) - 1

    .. seealso::

        :func:`disc_rate_ann`

    """
    return np.array(list((1 + disc_rate_ann[t//12])**(1/12) - 1 for t in range(proj_len())))


def duration(t):
    """Duration in force in years"""
    return t//12


def expense_acq():
    """Acquisition expense per policy

    ``300`` by default.
    """
    return 300


def expense_maint():
    """Annual maintenance expense per policy

    ``60`` by default.
    """
    return 60


def expenses(t):
    """Acquisition and maintenance expenses

    Expense cashflow during the period from ``t`` to ``t+1``.
    For any ``t``, the maintenance expense is recognized,
    which is defined as::

        pols_if(t) * expense_maint()/12 * inflation_factor(t)

    At ``t=0`` only, the acquisition expense,
    defined as :func:`expense_acq`, is recognized.

    .. seealso::

        * :func:`pols_if`
        * :func:`expense_maint`
        * :func:`inflation_factor`

    .. versionchanged:: 0.2.0
       The maintenance expense is also recognized for ``t=0``.

    """
    maint = pols_if(t) * expense_maint()/12 * inflation_factor(t)

    if t == 0:
        return expense_acq() + maint
    else:
        return maint


def inflation_factor(t):
    """The inflation factor at time t

    .. seealso::

        * :func:`inflation_rate`

    """
    return (1 + inflation_rate)**(t//12)


def inflation_rate():
    """Inflation rate"""
    return 0.01


def lapse_rate(t):
    """Lapse rate

    By default, the lapse rate assumption is defined by duration as::

        max(0.1 - 0.02 * duration(t), 0.02)

    .. seealso::

        :func:`duration`

    """
    return max(0.1 - 0.02 * duration(t), 0.02)


def loading_prem():
    """Loading per premium

    ``0.5`` by default.

    .. seealso::

        * :func:`premium_pp`

    """
    return 0.50


def model_point():
    """The selected model point as a Series

    :func:`model_point` looks up :attr:`model_point_table`, and
    returns as a Series the row whose label is the value of
    :attr:`point_id`.

    Example:
        In the code below ``Projection`` refers to
        the :mod:`~basiclife.BasicTerm_S.Projection` space::

            >>> Projection.point_id
            1

            >>> Projection.model_point()
            age_at_entry        47
            sex                  M
            policy_term         10
            policy_count         1
            sum_assured     622000
            Name: 1, dtype: object

            >>> Projection.point_id = 2

            >>> Projection.model_point()
            age_at_entry        29
            sex                  M
            policy_term         20
            policy_count         1
            sum_assured     752000
            Name: 2, dtype: object

    """
    return model_point_table.loc[point_id]


def mort_rate(t):
    """Mortality rate to be applied at time t

    .. seealso::

       * :attr:`mort_table`
       * :func:`mort_rate_mth`

    """
    return mort_table[str(max(min(5, duration(t)),0))][age(t)]


def mort_rate_mth(t):
    """Monthly mortality rate to be applied at time t

    .. seealso::

       * :attr:`mort_table`
       * :func:`mort_rate`

    """
    return 1-(1- mort_rate(t))**(1/12)


def net_cf(t):
    """Net cashflow

    Net cashflow for the period from ``t`` to ``t+1`` defined as::

        premiums(t) - claims(t) - expenses(t) - commissions(t)

    .. seealso::

        * :func:`premiums`
        * :func:`claims`
        * :func:`expenses`
        * :func:`commissions`

    """
    return premiums(t) - claims(t) - expenses(t) - commissions(t)


def net_premium_pp():
    """Net premium per policy

    The net premium per policy is defined so that
    the present value of net premiums equates to the present value of
    claims::

        pv_claims() / pv_pols_if()

    .. seealso::

        * :func:`pv_claims`
        * :func:`pv_pols_if`

    """
    return pv_claims() / pv_pols_if()


def policy_term():
    """The policy term of the selected model point.

    The element labeled ``policy_term`` of the Series returned by
    :func:`model_point`.
    """

    return model_point()["policy_term"]


def pols_death(t):
    """Number of death occurring at time t"""
    return pols_if(t) * mort_rate_mth(t)


def pols_if(t):
    """Number of policies in-force

    Number of in-force policies calculated recursively.
    The initial value is read from :func:`pols_if_init`.
    Subsequent values are defined recursively as::

        pols_if(t-1) - pols_lapse(t-1) - pols_death(t-1) - pols_maturity(t)

    .. seealso::
        * :func:`pols_lapse`
        * :func:`pols_death`
        * :func:`pols_maturity`

    """
    if t==0:
        return pols_if_init()
    elif t > policy_term() * 12:
        return 0
    else:
        return pols_if(t-1) - pols_lapse(t-1) - pols_death(t-1) - pols_maturity(t)


def pols_if_init(): 
    """Initial Number of Policies In-force

    Number of in-force policies at time 0 referenced from :func:`pols_if`.
    Defaults to 1.
    """
    return 1


def pols_lapse(t):
    """Number of lapse occurring at time t

    .. seealso::
        * :func:`pols_if`
        * :func:`lapse_rate`

    """
    return pols_if(t) * (1-(1 - lapse_rate(t))**(1/12))


def pols_maturity(t):
    """Number of maturing policies

    The policy maturity occurs at ``t == 12 * policy_term()``,
    after death and lapse during the last period::

        pols_if(t-1) - pols_lapse(t-1) - pols_death(t-1)

    otherwise ``0``.
    """
    if t == policy_term() * 12:
        return pols_if(t-1) - pols_lapse(t-1) - pols_death(t-1)
    else:
        return 0


def premium_pp(t):
    """Monthly premium per policy

    Monthly premium amount per policy defined as::

        round((1 + loading_prem()) * net_premium(), 2)

    .. seealso::

        * :func:`loading_prem`
        * :func:`net_premium_pp`

    """
    return round((1 + loading_prem()) * net_premium_pp(), 2)


def premiums(t):
    """Premium income

    Premium income during the period from ``t`` to ``t+1`` defined as::

        premium_pp(t) * pols_if(t)

    .. seealso::

        * :func:`premium_pp`
        * :func:`pols_if`

    """
    return premium_pp(t) * pols_if(t)


def proj_len():
    """Projection length in months

    Projection length in months defined as::

        12 * policy_term() + 1

    .. seealso::

        :func:`policy_term`

    """
    return 12 * policy_term() + 1


def pv_claims():
    """Present value of claims

    .. seealso::

        * :func:`claims`

    """
    return sum(list(claims(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def pv_commissions():
    """Present value of commissions

    .. seealso::

        * :func:`expenses`

    """
    return sum(list(commissions(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def pv_expenses():
    """Present value of expenses

    .. seealso::

        * :func:`expenses`

    """
    return sum(list(expenses(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def pv_net_cf():
    """Present value of net cashflows.

    Defined as::

        pv_premiums() - pv_claims() - pv_expenses() - pv_commissions()

    .. seealso::

        * :func:`pv_premiums`
        * :func:`pv_claims`
        * :func:`pv_expenses`
        * :func:`pv_commissions`

    """

    return pv_premiums() - pv_claims() - pv_expenses() - pv_commissions()


def pv_pols_if():
    """Present value of policies in-force

    The discounted sum of the number of in-force policies at each month.
    It is used as the annuity factor for calculating :func:`net_premium_pp`.

    """
    return sum(list(pols_if(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def pv_premiums():
    """Present value of premiums

    .. seealso::

        * :func:`premiums`

    """
    return sum(list(premiums(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def result_cf():
    """Result table of cashflows

    .. seealso::

       * :func:`premiums`
       * :func:`claims`
       * :func:`expenses`
       * :func:`commissions`
       * :func:`net_cf`

    """

    t_len = range(proj_len())

    data = {
        "Premiums": [premiums(t) for t in t_len],
        "Claims": [claims(t) for t in t_len],
        "Expenses": [expenses(t) for t in t_len],
        "Commissions": [commissions(t) for t in t_len],
        "Net Cashflow": [net_cf(t) for t in t_len]
    }
    return pd.DataFrame.from_dict(data)


def result_pv():
    """Result table of present value of cashflows

    .. seealso::

       * :func:`pv_premiums`
       * :func:`pv_claims`
       * :func:`pv_expenses`
       * :func:`pv_commissions`
       * :func:`pv_net_cf`

    """

    cols = ["Premiums", "Claims", "Expenses", "Commissions", "Net Cashflow"]
    pvs = [pv_premiums(), pv_claims(), pv_expenses(), pv_commissions(), pv_net_cf()]
    per_prem = [x / pv_premiums() for x in pvs]

    return pd.DataFrame.from_dict(
            data={"PV": pvs, "% Premium": per_prem},
            columns=cols,
            orient='index')


def sex(): 
    """The sex of the selected model point

    The element labeled ``sex`` of the Series returned by
    :func:`model_point`.
    """
    return model_point()["sex"]


def sum_assured():
    """The sum assured of the selected model point

    The element labeled ``sum_assured`` of the Series returned by
    :func:`model_point`.
    """
    return model_point()["sum_assured"]


# ---------------------------------------------------------------------------
# References

disc_rate_ann = ("DataClient", 2180220040776)

model_point_table = ("DataClient", 2180211700488)

mort_table = ("DataClient", 2180225433416)

pd = ("Module", "pandas")

point_id = 1

np = ("Module", "numpy")