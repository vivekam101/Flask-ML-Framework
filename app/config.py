import json

# *
# * LEAD RANKING *
# *

def _map_lead_ranking_data(data):
    _mapping ={
            '_id':'Id',
            '_no_of_visits':'Visits__c',
            '_page_views':'Page_Views__c',
            '_submissions':'Submissions__c',
             'annual_revenue':'Annual_Revenue_in_USD__c',
             'annual_sales_volume':'Annual_Sales_Volume__c',
             '_no_of_rejects':'No_of_rejected_items__c',
    }
    _out = {}
    for _key in _mapping.keys():
        _out[_key] = data.get(_mapping[_key])

    return _out

LEAD_RANKING_API_CONFIG = {
    "data_map":_map_lead_ranking_data,
    "model_dump_file_path":"model_dumps/decision_tree.pkl",
    "true_status":"Y",
    "category_cols":"",
}


# *
# * LEAD RANKING ENDS HERE *
# *

# *
# * LEAD CONVERSION *
# *

def _map_lead_conversion_rate(data):
    _mapping ={
            '_id':'Id',
            '_no_of_visits':'Visits__c',
            '_page_views':'Page_Views__c',
            '_submissions':'Submissions__c',
             'annual_revenue':'Annual_Revenue_in_USD__c',
             'annual_sales_volume':'Annual_Sales_Volume__c',
             '_no_of_rejects':'No_of_rejected_items__c',
             'lead_category':'LeadCategory__c',
             'lead_source':'Lead_Source__c'
    }
    _out = {}
    for _key in _mapping.keys():
        _out[_key] = data.get(_mapping[_key])

    return _out

LEAD_CONVERSION_API_CONFIG = {
    "data_map":_map_lead_conversion_rate,
    "model_dump_file_path":"model_dumps/decision_tree.pkl",
    "true_status":"Y",
    "category_cols":{"lead_category":['Affiliate', 'Aggregate', 'Field'],\
            "lead_source":['Data.com', 'ESamples', 'Other', 'SOPS', 'Trade Shows', 'Web']},
}

# *
# * LEAD CONVERSION ENDS HERE *
# *
