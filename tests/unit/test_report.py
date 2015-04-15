from __future__ import absolute_import
import httpretty
import unittest
from agms.configuration import Configuration
from agms.report import Report


class ReportTest(unittest.TestCase):

    def setUp(self):
        Configuration.configure('agmsdevdemo', 'nX1m*xa9Id', '1001789', 'b00f57326f8cf34bbb705a74b5fcbaa2b2f3e58076dc81f', 'requests')
        self.report = Report()
        
    def testReportClassAssignment(self):
        self.assertIsInstance(self.report, Report)

    @httpretty.activate
    def testSuccessfulTransactionAPI(self):
        httpretty.register_uri(httpretty.POST, "https://gateway.agms.com/roxapi/agms.asmx",
                                body=self.successful_TransactionAPI_response(),
                                content_type="application/xml")

        params = {
            'start_date': {'value': '2014-09-24'},
            'end_date': {'value': '2014-11-03'},
        }
        self.report_result = self.report.list_transactions(params)
        self.assertIsInstance(self.report_result, list)

    @httpretty.activate
    def testSuccessfulSAFEAPI(self):
        httpretty.register_uri(httpretty.POST, "https://gateway.agms.com/roxapi/AGMS_SAFE_API.asmx",
                                body=self.successful_SAFEAPI_response(),
                                content_type="application/xml")

        params = {
            'start_date': {'value': '2014-09-24'},
            'end_date': {'value': '2014-11-03'},
        }
        self.report_result = self.report.list_SAFEs(params)
        self.assertIsInstance(self.report_result, list)

    def successful_TransactionAPI_response(self):
        return """
            <?xml version=\"1.0\" encoding=\"utf-8\"?><soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"><soap:Body><TransactionAPIResponse xmlns=\"https://gateway.agms.com/roxapi/\"><TransactionAPIResult>&lt;transactions&gt;&lt;transaction&gt;&lt;id&gt;716803&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;716803&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/31/2015 10:08:06 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/31/2015 10:08:06 PM&lt;/createdate&gt;&lt;moddate&gt;3/31/2015 10:08:06 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710036&lt;/id&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;0&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0500&lt;/ccexpdate&gt;&lt;firstname&gt;Joe&lt;/firstname&gt;&lt;lastname&gt;Smith&lt;/lastname&gt;&lt;safeaction&gt;add_safe&lt;/safeaction&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;SAFE Record added successfully. No transaction processed.&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710036&lt;/responsetransid&gt;&lt;responsesafeid&gt;1034226&lt;/responsesafeid&gt;&lt;transactiondate&gt;3/29/2015 3:23:16 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 3:23:16 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 3:23:16 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710035&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710035&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 3:23:07 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 3:23:07 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 3:23:07 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710015&lt;/id&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;0&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0500&lt;/ccexpdate&gt;&lt;firstname&gt;Joe&lt;/firstname&gt;&lt;lastname&gt;Smith&lt;/lastname&gt;&lt;safeaction&gt;add_safe&lt;/safeaction&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;SAFE Record added successfully. No transaction processed.&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710015&lt;/responsetransid&gt;&lt;responsesafeid&gt;1034225&lt;/responsesafeid&gt;&lt;transactiondate&gt;3/29/2015 3:01:24 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 3:01:24 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 3:01:24 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710014&lt;/id&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;0&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0500&lt;/ccexpdate&gt;&lt;firstname&gt;Joe&lt;/firstname&gt;&lt;lastname&gt;Smith&lt;/lastname&gt;&lt;safeaction&gt;add_safe&lt;/safeaction&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;SAFE Record added successfully. No transaction processed.&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710014&lt;/responsetransid&gt;&lt;responsesafeid&gt;1034224&lt;/responsesafeid&gt;&lt;transactiondate&gt;3/29/2015 3:00:54 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 3:00:54 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 3:00:54 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710013&lt;/id&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;0&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0500&lt;/ccexpdate&gt;&lt;firstname&gt;Joe&lt;/firstname&gt;&lt;lastname&gt;Smith&lt;/lastname&gt;&lt;safeaction&gt;add_safe&lt;/safeaction&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;SAFE Record added successfully. No transaction processed.&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710013&lt;/responsetransid&gt;&lt;responsesafeid&gt;1034223&lt;/responsesafeid&gt;&lt;transactiondate&gt;3/29/2015 2:59:33 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:59:33 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:59:33 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710011&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710011&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:52:08 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:52:08 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:52:08 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710010&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710010&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:49:44 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:49:44 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:49:44 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710008&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710008&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:46:52 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:46:52 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:46:52 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710005&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710005&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:45:27 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:45:27 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:45:27 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710003&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710003&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:44:32 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:44:32 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:44:32 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710002&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710002&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:44:09 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:44:09 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:44:09 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;710001&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;710001&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:43:34 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:43:34 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:43:35 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709999&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709999&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:43:19 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:43:19 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:43:19 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709998&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709998&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:42:21 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:42:21 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:42:21 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709997&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709997&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:41:34 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:41:34 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:41:34 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709995&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709995&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:39:59 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:39:59 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:39:59 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709993&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709993&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:39:22 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:39:22 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:39:22 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709991&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709991&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:36:53 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:36:53 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:36:53 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709990&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709990&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:35:47 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:35:47 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:35:47 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709988&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709988&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:35:12 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:35:12 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:35:12 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709984&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709984&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:31:15 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:31:15 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:31:15 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709972&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709972&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:26:16 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:26:16 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:26:17 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709971&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709971&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:25:45 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:25:45 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:25:45 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709970&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709970&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:25:23 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:25:23 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:25:23 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709969&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709969&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:23:47 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:23:47 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:23:48 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709964&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709964&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:22:15 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:22:15 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:22:15 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;(Agms Ruby 0.2.1)&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;transaction&gt;&lt;id&gt;709940&lt;/id&gt;&lt;transactiontype&gt;sale&lt;/transactiontype&gt;&lt;paymenttype&gt;creditcard&lt;/paymenttype&gt;&lt;amount&gt;100&lt;/amount&gt;&lt;cardtype&gt;Visa&lt;/cardtype&gt;&lt;ccnumber&gt;4****1111&lt;/ccnumber&gt;&lt;ccexpdate&gt;0520&lt;/ccexpdate&gt;&lt;responsestatuscode&gt;1&lt;/responsestatuscode&gt;&lt;responsestatusmsg&gt;Approved&lt;/responsestatusmsg&gt;&lt;responsetransid&gt;709940&lt;/responsetransid&gt;&lt;responseauthcode&gt;9999&lt;/responseauthcode&gt;&lt;transactiondate&gt;3/29/2015 2:01:14 PM&lt;/transactiondate&gt;&lt;createdate&gt;3/29/2015 2:01:14 PM&lt;/createdate&gt;&lt;moddate&gt;3/29/2015 2:01:14 PM&lt;/moddate&gt;&lt;createuser&gt;agmsdevdemo&lt;/createuser&gt;&lt;moduser&gt;LogResponse&lt;/moduser&gt;&lt;useragent&gt;curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8| zlib/1.2.5&lt;/useragent&gt;&lt;cardpresent&gt;False&lt;/cardpresent&gt;&lt;/transaction&gt;&lt;/transactions&gt;</TransactionAPIResult></TransactionAPIResponse></soap:Body></soap:Envelope>
            """

    def successful_SAFEAPI_response(self):
        return """
            <?xml version=\"1.0\" encoding=\"utf-8\"?><soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"><soap:Body><QuerySAFEResponse xmlns=\"https://gateway.agms.com/roxapi/\"><QuerySAFEResult>&lt;saferecords&gt;&lt;saferecord&gt;&lt;ID&gt;1034223&lt;/ID&gt;&lt;MerchantID&gt;652&lt;/MerchantID&gt;&lt;CustomerID&gt;&lt;/CustomerID&gt;&lt;Type&gt;True&lt;/Type&gt;&lt;CCNumber&gt;4****1111&lt;/CCNumber&gt;&lt;CCExpDate&gt;0500&lt;/CCExpDate&gt;&lt;CheckName&gt;&lt;/CheckName&gt;&lt;CheckABA&gt;&lt;/CheckABA&gt;&lt;CheckAccount&gt;&lt;/CheckAccount&gt;&lt;AccountHolderType&gt;&lt;/AccountHolderType&gt;&lt;AccountType&gt;&lt;/AccountType&gt;&lt;FirstName&gt;&lt;/FirstName&gt;&lt;FirstName&gt;Joe&lt;/FirstName&gt;&lt;LastName&gt;Smith&lt;/LastName&gt;&lt;Company&gt;&lt;/Company&gt;&lt;Address1&gt;&lt;/Address1&gt;&lt;Address2&gt;&lt;/Address2&gt;&lt;City&gt;&lt;/City&gt;&lt;State&gt;&lt;/State&gt;&lt;Zip&gt;&lt;/Zip&gt;&lt;Country&gt;&lt;/Country&gt;&lt;Phone&gt;&lt;/Phone&gt;&lt;Fax&gt;&lt;/Fax&gt;&lt;Email&gt;&lt;/Email&gt;&lt;Website&gt;&lt;/Website&gt;&lt;Tax&gt;&lt;/Tax&gt;&lt;Shipping&gt;&lt;/Shipping&gt;&lt;OrderID&gt;&lt;/OrderID&gt;&lt;PONumber&gt;&lt;/PONumber&gt;&lt;Active&gt;&lt;/Active&gt;&lt;Internal&gt;8SMYRN0C&lt;/Internal&gt;&lt;CreateDate&gt;3/29/2015 2:59:33 PM&lt;/CreateDate&gt;&lt;ModDate&gt;&lt;/ModDate&gt;&lt;CreateUser&gt;agmsdevdemo&lt;/CreateUser&gt;&lt;ModUser&gt;&lt;/ModUser&gt;&lt;/saferecord&gt;&lt;saferecord&gt;&lt;ID&gt;1034224&lt;/ID&gt;&lt;MerchantID&gt;652&lt;/MerchantID&gt;&lt;CustomerID&gt;&lt;/CustomerID&gt;&lt;Type&gt;True&lt;/Type&gt;&lt;CCNumber&gt;4****1111&lt;/CCNumber&gt;&lt;CCExpDate&gt;0500&lt;/CCExpDate&gt;&lt;CheckName&gt;&lt;/CheckName&gt;&lt;CheckABA&gt;&lt;/CheckABA&gt;&lt;CheckAccount&gt;&lt;/CheckAccount&gt;&lt;AccountHolderType&gt;&lt;/AccountHolderType&gt;&lt;AccountType&gt;&lt;/AccountType&gt;&lt;FirstName&gt;&lt;/FirstName&gt;&lt;FirstName&gt;Joe&lt;/FirstName&gt;&lt;LastName&gt;Smith&lt;/LastName&gt;&lt;Company&gt;&lt;/Company&gt;&lt;Address1&gt;&lt;/Address1&gt;&lt;Address2&gt;&lt;/Address2&gt;&lt;City&gt;&lt;/City&gt;&lt;State&gt;&lt;/State&gt;&lt;Zip&gt;&lt;/Zip&gt;&lt;Country&gt;&lt;/Country&gt;&lt;Phone&gt;&lt;/Phone&gt;&lt;Fax&gt;&lt;/Fax&gt;&lt;Email&gt;&lt;/Email&gt;&lt;Website&gt;&lt;/Website&gt;&lt;Tax&gt;&lt;/Tax&gt;&lt;Shipping&gt;&lt;/Shipping&gt;&lt;OrderID&gt;&lt;/OrderID&gt;&lt;PONumber&gt;&lt;/PONumber&gt;&lt;Active&gt;&lt;/Active&gt;&lt;Internal&gt;5RH2VJ9M&lt;/Internal&gt;&lt;CreateDate&gt;3/29/2015 3:00:54 PM&lt;/CreateDate&gt;&lt;ModDate&gt;&lt;/ModDate&gt;&lt;CreateUser&gt;agmsdevdemo&lt;/CreateUser&gt;&lt;ModUser&gt;&lt;/ModUser&gt;&lt;/saferecord&gt;&lt;saferecord&gt;&lt;ID&gt;1034225&lt;/ID&gt;&lt;MerchantID&gt;652&lt;/MerchantID&gt;&lt;CustomerID&gt;&lt;/CustomerID&gt;&lt;Type&gt;True&lt;/Type&gt;&lt;CCNumber&gt;4****1111&lt;/CCNumber&gt;&lt;CCExpDate&gt;0500&lt;/CCExpDate&gt;&lt;CheckName&gt;&lt;/CheckName&gt;&lt;CheckABA&gt;&lt;/CheckABA&gt;&lt;CheckAccount&gt;&lt;/CheckAccount&gt;&lt;AccountHolderType&gt;&lt;/AccountHolderType&gt;&lt;AccountType&gt;&lt;/AccountType&gt;&lt;FirstName&gt;&lt;/FirstName&gt;&lt;FirstName&gt;Joe&lt;/FirstName&gt;&lt;LastName&gt;Smith&lt;/LastName&gt;&lt;Company&gt;&lt;/Company&gt;&lt;Address1&gt;&lt;/Address1&gt;&lt;Address2&gt;&lt;/Address2&gt;&lt;City&gt;&lt;/City&gt;&lt;State&gt;&lt;/State&gt;&lt;Zip&gt;&lt;/Zip&gt;&lt;Country&gt;&lt;/Country&gt;&lt;Phone&gt;&lt;/Phone&gt;&lt;Fax&gt;&lt;/Fax&gt;&lt;Email&gt;&lt;/Email&gt;&lt;Website&gt;&lt;/Website&gt;&lt;Tax&gt;&lt;/Tax&gt;&lt;Shipping&gt;&lt;/Shipping&gt;&lt;OrderID&gt;&lt;/OrderID&gt;&lt;PONumber&gt;&lt;/PONumber&gt;&lt;Active&gt;&lt;/Active&gt;&lt;Internal&gt;IZD9HHKF&lt;/Internal&gt;&lt;CreateDate&gt;3/29/2015 3:01:24 PM&lt;/CreateDate&gt;&lt;ModDate&gt;&lt;/ModDate&gt;&lt;CreateUser&gt;agmsdevdemo&lt;/CreateUser&gt;&lt;ModUser&gt;&lt;/ModUser&gt;&lt;/saferecord&gt;&lt;saferecord&gt;&lt;ID&gt;1034226&lt;/ID&gt;&lt;MerchantID&gt;652&lt;/MerchantID&gt;&lt;CustomerID&gt;&lt;/CustomerID&gt;&lt;Type&gt;True&lt;/Type&gt;&lt;CCNumber&gt;4****1111&lt;/CCNumber&gt;&lt;CCExpDate&gt;0500&lt;/CCExpDate&gt;&lt;CheckName&gt;&lt;/CheckName&gt;&lt;CheckABA&gt;&lt;/CheckABA&gt;&lt;CheckAccount&gt;&lt;/CheckAccount&gt;&lt;AccountHolderType&gt;&lt;/AccountHolderType&gt;&lt;AccountType&gt;&lt;/AccountType&gt;&lt;FirstName&gt;&lt;/FirstName&gt;&lt;FirstName&gt;Joe&lt;/FirstName&gt;&lt;LastName&gt;Smith&lt;/LastName&gt;&lt;Company&gt;&lt;/Company&gt;&lt;Address1&gt;&lt;/Address1&gt;&lt;Address2&gt;&lt;/Address2&gt;&lt;City&gt;&lt;/City&gt;&lt;State&gt;&lt;/State&gt;&lt;Zip&gt;&lt;/Zip&gt;&lt;Country&gt;&lt;/Country&gt;&lt;Phone&gt;&lt;/Phone&gt;&lt;Fax&gt;&lt;/Fax&gt;&lt;Email&gt;&lt;/Email&gt;&lt;Website&gt;&lt;/Website&gt;&lt;Tax&gt;&lt;/Tax&gt;&lt;Shipping&gt;&lt;/Shipping&gt;&lt;OrderID&gt;&lt;/OrderID&gt;&lt;PONumber&gt;&lt;/PONumber&gt;&lt;Active&gt;&lt;/Active&gt;&lt;Internal&gt;9VHFK5N1&lt;/Internal&gt;&lt;CreateDate&gt;3/29/2015 3:23:16 PM&lt;/CreateDate&gt;&lt;ModDate&gt;&lt;/ModDate&gt;&lt;CreateUser&gt;agmsdevdemo&lt;/CreateUser&gt;&lt;ModUser&gt;&lt;/ModUser&gt;&lt;/saferecord&gt;&lt;/saferecords&gt;</QuerySAFEResult></QuerySAFEResponse></soap:Body></soap:Envelope>
            """
if __name__ == '__main__':
    unittest.main()