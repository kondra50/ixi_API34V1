
import pysolr
solr = pysolr.Solr('http://localhost:8983/solr/simple', timeout=10)

#solr.SolrConnection('http://localhost:8983/solr')
#s = solr.SolrConnection('http://localhost:8983/solr')



solr.add([{



      "AccountId": "001a000001jNWoqAAG",
      "C_CommentBody": "Software successfully registered in the field.",
      "C_CreatedById": "005a0000007u7uxAAA",
      "C_CreatedDate": "2016-05-13T11:45:32.000+0000Z",
      "C_Id": "500a0000017PtiuAAC",
      "CaseNumber": "00002882",
      "ClosedDate": "2016-05-13T11:45:32.000+0000Z",
      "ContactId": "003a000002LyCAzAAN",
      "Description": "GM Software not licenced. The information given was not enough to successfully activate the software licence. Additional information was required.",
      "Id": "500a0000017PtiuAAC",
      "S_CreatedById": "005a0000007u7uxAAA",
      "S_CreatedDate": "2016-05-13T11:45:32.000+0000Z",
      "S_SolutionName": "GM software",
      "S_SolutionNote": "Software successfully registered in the field.",
      "S_SolutionNumber": "00000658",
      "S_Status": "Draft",
      "Status": "Closed – resolved by FSE fix",
      "Subject": "GM software",
      "Type": "Field Service"


},])