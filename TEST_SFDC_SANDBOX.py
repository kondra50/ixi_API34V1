from simple_salesforce import Salesforce
sf = Salesforce(instance='test.salesforce.com', username='customerservice@integenx.com.dev', password='password12345' , security_token='TwR2D8h7bi09zIKsDeLtXZXPx' , sandbox=True)
#sf = Salesforce(instance='login.salesforce.com', username='customerservice@integenx.com', password='password12345' , security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
list=sf.query("SELECT ESI__SO_ID__c,ESI__PRODUCT_LINE__c,ESI__SO_LINE_NO__c,ESI__SO_LINE_STATUS__c,ESI__REV_SHIP_DATE__c,ESI__LAST_SHIP_NO__c,ESI__REV_ORDER_QTY__c,ESI__AMOUNT__c from ESI__Sales_Order_Detail__c")
dict=list["records"]
prs_as_dict=[]
for record in  dict:
    rp_as_dict = {
                   'Sales Order Number':  record['ESI__SO_ID__c'],
                   'Prod Line':  record['ESI__PRODUCT_LINE__c'],
                   'Sales Order Line':  record['ESI__SO_LINE_NO__c'],
                   'Line St':  record['ESI__SO_LINE_STATUS__c'],
                   'Rev Ship':  record['ESI__REV_SHIP_DATE__c'],
                   'Last Shipment':  record['ESI__LAST_SHIP_NO__c'],
                   'Rev Ord Qty':  record['ESI__REV_ORDER_QTY__c'],
                   'Amount':  record['ESI__AMOUNT__c']
                   #'Opportunity Owner' :  record[15],
            }

    print(rp_as_dict)
