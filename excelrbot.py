import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") == "user.query":

        a = req.get("result").get("parameters").get("course")
        print(a+"3")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        x = {"DATA SCIENCE": sheet.range('B2:J2'), "TABLEAU": sheet.range('B3:J3'),"BIG DATA HADOOP":sheet.range('B4:J4'),"ADVANCED ANALYTICS":sheet.range('B5:J5'),
             "PROJECT MANAGEMENT PROFESSIONAL":sheet.range('B6:J6'),"AGILE CERTIFIED PROFESSIONAL":sheet.range('B7:J7'),"ITIL FOUNDATION":sheet.range('B8:J8'),
            "ITIL INTERMEDIATE":sheet.range('B9:J9'),"PRINCE 2 FOUNDATION": sheet.range('B10:J10'),"PRINCE 2 PRACTITIONER":sheet.range('B11:J11'),
            "LEAN SIX SIGMA GREEN BELT":sheet.range('B12:J12'),"LEAN SIX SIGMA BLACK BELT": sheet.range('B13:J13'),"CAPM": sheet.range('B14:J14'),
            "MSP":sheet.range('B15:J15'),"Internet of Things":sheet.range('B16:J16'),"Amazon Web Servies": sheet.range('B17:J17')}
        list1 = []
        for cell in x[a]:
            list1.append(cell.value)

        speech = "We offer " +list1[0]+ " course at a cost of Rs. "+list1[1]+" (excluding taxes). The training duaration is "+list1[7]+" hours. We provide "+list1[8]+" mode of training for this course."

    elif req.get("result").get("action") == "what.price":
        b = req.get("result").get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        y = {"DATA SCIENCE": sheet.acell("F2").value,"TABLEAU":sheet.acell("F3").value,"BIG DATA HADOOP":sheet.acell("F4").value,
             "ADVANCED ANALYTICS":sheet.acell("F5").value,"PROJECT MANAGEMENT PROFESSIONAL":sheet.acell("F6").value,"AGILE CERTIFIED PROFESSIONAL":sheet.acell("F7").value,
             "ITIL FOUNDATION":sheet.acell("F8").value,"ITIL INTERMEDIATE":sheet.acell("F9").value,"PRINCE 2 FOUNDATION":sheet.acell("F10").value,"PRINCE 2 PRACTITIONER":sheet.acell("F11").value,
             "LEAN SIX SIGMA GREEN BELT":sheet.acell("F12").value,"LEAN SIX SIGMA BLACK BELT":sheet.acell("F13").value,"CAPM":sheet.acell("F14").value,
             "MSP":sheet.acell("F15").value,"Internet of Things":sheet.acell("F16").value,"Amazon Web Servies":sheet.acell("F17").value}


        speech = "Its Rs. "+y[b]+ " plus taxes(18% GST)"







    elif req.get("result").get("action") == "followup.trainer":
        d = req.get("result").get("contexts")[0].get("parameters").get("course")
        print(d)
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        y = {"DATA SCIENCE": sheet.acell("T2").value, "TABLEAU": sheet.acell("T3").value,
             "BIG DATA HADOOP": sheet.acell("T4").value,
             "ADVANCED ANALYTICS": sheet.acell("T5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("T6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("T7").value,
             "ITIL FOUNDATION": sheet.acell("T8").value, "ITIL INTERMEDIATE": sheet.acell("T9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("T10").value, "PRINCE 2 PRACTITIONER": sheet.acell("T11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("T12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("T13").value, "CAPM": sheet.acell("T14").value,
             "MSP": sheet.acell("T15").value, "Internet of Things": sheet.acell("T16").value,
             "Amazon Web Servies": sheet.acell("T17").value}

        speech = " "+y[d]

    elif req.get("result").get("action") == "followup.discount":
        d = req.get("result").get("contexts")[0].get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        y = {"DATA SCIENCE": sheet.acell("N2").value, "TABLEAU": sheet.acell("N3").value,
             "BIG DATA HADOOP": sheet.acell("N4").value,
             "ADVANCED ANALYTICS": sheet.acell("N5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("N6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("N7").value,
             "ITIL FOUNDATION": sheet.acell("N8").value, "ITIL INTERMEDIATE": sheet.acell("N9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("N10").value, "PRINCE 2 PRACTITIONER": sheet.acell("N11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("N12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("N13").value, "CAPM": sheet.acell("N14").value,
             "MSP": sheet.acell("N15").value, "Internet of Things": sheet.acell("N16").value,
             "Amazon Web Servies": sheet.acell("N17").value}

        speech = " " +y[d]

    elif req.get("result").get("action") == "user.query.eligibility":
        d = req.get("result").get("contexts")[0].get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        y = {"DATA SCIENCE": sheet.acell("O2").value, "TABLEAU": sheet.acell("O3").value,
             "BIG DATA HADOOP": sheet.acell("O4").value,
             "ADVANCED ANALYTICS": sheet.acell("O5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("O6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("O7").value,
             "ITIL FOUNDATION": sheet.acell("O8").value, "ITIL INTERMEDIATE": sheet.acell("O9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("O10").value, "PRINCE 2 PRACTITIONER": sheet.acell("O11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("O12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("O13").value, "CAPM": sheet.acell("O14").value,
             "MSP": sheet.acell("O15").value, "Internet of Things": sheet.acell("O16").value,
             "Amazon Web Servies": sheet.acell("O17").value}

        speech = y[d]

    elif req.get("result").get("action") == "followup.starting.date":
        d = req.get("result").get("contexts")[0].get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")
        z = {"DATA SCIENCE": sheet.acell("K2").value, "TABLEAU": sheet.acell("K3").value,
             "BIG DATA HADOOP": sheet.acell("K4").value,
             "ADVANCED ANALYTICS": sheet.acell("K5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("K6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("K7").value,
             "ITIL FOUNDATION": sheet.acell("K8").value, "ITIL INTERMEDIATE": sheet.acell("K9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("K10").value, "PRINCE 2 PRACTITIONER": sheet.acell("K11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("K12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("K13").value, "CAPM": sheet.acell("K14").value,
             "MSP": sheet.acell("K15").value, "Internet of Things": sheet.acell("K16").value,
             "Amazon Web Servies": sheet.acell("K17").value}

        speech = "Our next starting dates at different locations are " +z[d]+ " ."

    elif req.get("result").get("action") == "followup.course.details":
        d = req.get("result").get("contexts")[0].get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")
        z = {"DATA SCIENCE": sheet.acell("L2").value, "TABLEAU": sheet.acell("L3").value,
             "BIG DATA HADOOP": sheet.acell("L4").value,
             "ADVANCED ANALYTICS": sheet.acell("L5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("L6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("L7").value,
             "ITIL FOUNDATION": sheet.acell("L8").value, "ITIL INTERMEDIATE": sheet.acell("L9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("L10").value, "PRINCE 2 PRACTITIONER": sheet.acell("L11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("L12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("L13").value, "CAPM": sheet.acell("L14").value,
             "MSP": sheet.acell("L15").value, "Internet of Things": sheet.acell("L16").value,
             "Amazon Web Servies": sheet.acell("L17").value}

        speech = "" +z[d]

    elif req.get("result").get("action") == "followup.certification":
        d = req.get("result").get("contexts")[0].get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")
        z = {"DATA SCIENCE": sheet.acell("G2").value, "TABLEAU": sheet.acell("G3").value,
             "BIG DATA HADOOP": sheet.acell("G4").value,
             "ADVANCED ANALYTICS": sheet.acell("G5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("G6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("G7").value,
             "ITIL FOUNDATION": sheet.acell("G8").value, "ITIL INTERMEDIATE": sheet.acell("G9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("G10").value, "PRINCE 2 PRACTITIONER": sheet.acell("G11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("G12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("G13").value, "CAPM": sheet.acell("G14").value,
             "MSP": sheet.acell("G15").value, "Internet of Things": sheet.acell("G16").value,
             "Amazon Web Servies": sheet.acell("G17").value}

        speech = "" +z[d]

    elif req.get("result").get("action") == "followup.prerequisites":
        d = req.get("result").get("contexts")[0].get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")
        z = {"DATA SCIENCE": sheet.acell("S2").value, "TABLEAU": sheet.acell("S3").value,
             "BIG DATA HADOOP": sheet.acell("S4").value,
             "ADVANCED ANALYTICS": sheet.acell("S5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("S6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("S7").value,
             "ITIL FOUNDATION": sheet.acell("S8").value, "ITIL INTERMEDIATE": sheet.acell("S9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("S10").value, "PRINCE 2 PRACTITIONER": sheet.acell("S11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("S12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("S13").value, "CAPM": sheet.acell("S14").value,
             "MSP": sheet.acell("S15").value, "Internet of Things": sheet.acell("S16").value,
             "Amazon Web Servies": sheet.acell("S17").value}

        speech =  ""+z[d]

    elif req.get("result").get("action") == "certification.provided":
        b = req.get("result").get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        z = {"DATA SCIENCE": sheet.acell("G2").value, "TABLEAU": sheet.acell("G3").value,
             "BIG DATA HADOOP": sheet.acell("G4").value,
             "ADVANCED ANALYTICS": sheet.acell("G5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("G6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("G7").value,
             "ITIL FOUNDATION": sheet.acell("G8").value, "ITIL INTERMEDIATE": sheet.acell("G9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("G10").value, "PRINCE 2 PRACTITIONER": sheet.acell("G11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("G12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("G13").value, "CAPM": sheet.acell("G14").value,
             "MSP": sheet.acell("G15").value, "Internet of Things": sheet.acell("G16").value,
             "Amazon Web Servies": sheet.acell("G17").value}

        speech = "" +z[b]

    elif req.get("result").get("action") == "course.details":
        b = req.get("result").get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        z = {"DATA SCIENCE": sheet.acell("L2").value, "TABLEAU": sheet.acell("L3").value,
             "BIG DATA HADOOP": sheet.acell("L4").value,
             "ADVANCED ANALYTICS": sheet.acell("L5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("L6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("L7").value,
             "ITIL FOUNDATION": sheet.acell("L8").value, "ITIL INTERMEDIATE": sheet.acell("L9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("L10").value, "PRINCE 2 PRACTITIONER": sheet.acell("L11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("L12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("L13").value, "CAPM": sheet.acell("L14").value,
             "MSP": sheet.acell("L15").value, "Internet of Things": sheet.acell("L16").value,
             "Amazon Web Servies": sheet.acell("L17").value}

        speech = "" +z[b]

    elif req.get("result").get("action") == "any.discount":
        b = req.get("result").get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        y = {"DATA SCIENCE": sheet.acell("N2").value, "TABLEAU": sheet.acell("N3").value,
             "BIG DATA HADOOP": sheet.acell("N4").value,
             "ADVANCED ANALYTICS": sheet.acell("N5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("N6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("N7").value,
             "ITIL FOUNDATION": sheet.acell("N8").value, "ITIL INTERMEDIATE": sheet.acell("N9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("N10").value, "PRINCE 2 PRACTITIONER": sheet.acell("N11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("N12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("N13").value, "CAPM": sheet.acell("N14").value,
             "MSP": sheet.acell("N15").value, "Internet of Things": sheet.acell("N16").value,
             "Amazon Web Servies": sheet.acell("N17").value}

        speech = " " + y[b]
    elif req.get("result").get("action") == "any.prerequisites":
        b = req.get("result").get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        z = {"DATA SCIENCE": sheet.acell("S2").value, "TABLEAU": sheet.acell("S3").value,
             "BIG DATA HADOOP": sheet.acell("S4").value,
             "ADVANCED ANALYTICS": sheet.acell("S5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("S6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("S7").value,
             "ITIL FOUNDATION": sheet.acell("S8").value, "ITIL INTERMEDIATE": sheet.acell("S9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("S10").value, "PRINCE 2 PRACTITIONER": sheet.acell("S11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("S12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("S13").value, "CAPM": sheet.acell("S14").value,
             "MSP": sheet.acell("S15").value, "Internet of Things": sheet.acell("S16").value,
             "Amazon Web Servies": sheet.acell("S17").value}

        speech = "" + z[b]

    elif req.get("result").get("action") == "trainer":
        b = req.get("result").get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        y = {"DATA SCIENCE": sheet.acell("T2").value, "TABLEAU": sheet.acell("T3").value,
             "BIG DATA HADOOP": sheet.acell("T4").value,
             "ADVANCED ANALYTICS": sheet.acell("T5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("T6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("T7").value,
             "ITIL FOUNDATION": sheet.acell("T8").value, "ITIL INTERMEDIATE": sheet.acell("T9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("T10").value, "PRINCE 2 PRACTITIONER": sheet.acell("T11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("T12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("T13").value, "CAPM": sheet.acell("T14").value,
             "MSP": sheet.acell("T15").value, "Internet of Things": sheet.acell("T16").value,
             "Amazon Web Servies": sheet.acell("T17").value}

        speech = " " + y[b]

    elif req.get("result").get("action") == "starting.date":
        b = req.get("result").get("parameters").get("course")
        sheet = client.open("sheetdemo").worksheet("Sheet1")

        z = {"DATA SCIENCE": sheet.acell("K2").value, "TABLEAU": sheet.acell("K3").value,
             "BIG DATA HADOOP": sheet.acell("K4").value,
             "ADVANCED ANALYTICS": sheet.acell("K5").value, "PROJECT MANAGEMENT PROFESSIONAL": sheet.acell("K6").value,
             "AGILE CERTIFIED PROFESSIONAL": sheet.acell("K7").value,
             "ITIL FOUNDATION": sheet.acell("K8").value, "ITIL INTERMEDIATE": sheet.acell("K9").value,
             "PRINCE 2 FOUNDATION": sheet.acell("K10").value, "PRINCE 2 PRACTITIONER": sheet.acell("K11").value,
             "LEAN SIX SIGMA GREEN BELT": sheet.acell("K12").value,
             "LEAN SIX SIGMA BLACK BELT": sheet.acell("K13").value, "CAPM": sheet.acell("K14").value,
             "MSP": sheet.acell("K15").value, "Internet of Things": sheet.acell("K16").value,
             "Amazon Web Servies": sheet.acell("K17").value}

        speech = "Our next starting dates at different locations are " + z[b] + " ."












    return {
        "speech": speech,
        "displayText": speech,
        # "data": {},
        # "contextOut": [],
         "source": "nothing"
    }







if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')