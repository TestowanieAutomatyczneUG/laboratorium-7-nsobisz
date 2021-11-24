from main import Zad3

import unittest

class Zad3Test(unittest.TestCase):

    def setUp(self):
        self.temp = Zad3()

    def test_correct_1(self):
        self.assertEqual(self.temp.statement({
  "customer": "BigCo",
  "performances": [
    {
      "playID": "hamlet",
      "audience": 55
    },
    {
      "playID": "as-like",
      "audience": 35
    },
    {
      "playID": "othello",
      "audience": 40
    }
  ]
},
{
  "hamlet": {"name": "Hamlet", "type": "tragedy"},
  "as-like": {"name": "As You Like It", "type": "comedy"},
  "othello": {"name": "Othello", "type": "tragedy"}
}),"Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n")

    def test_correct_2(self):
            self.assertEqual(self.temp.statement({
  "customer": "aaaa",
  "performances": [
    {
      "playID": "www",
      "audience": 525
    },
    {
      "playID": "ok",
      "audience": 5
    },
    {
      "playID": "hmm",
      "audience": 90
    }
  ]
},{
  "www": {"name": "WWW", "type": "tragedy"},
  "ok": {"name": "OK", "type": "comedy"},
  "hmm": {"name": "Hmm", "type": "tragedy"}
}),
                "Statement for aaaa\n WWW: $5,350.00 (525 seats)\n OK: $315.00 (5 seats)\n Hmm: $1,000.00 (90 seats)\nAmount owed is $6,665.00\nYou earned 556 credits\n")

    def test_correct_3_with_zeros(self):
        self.assertEqual(self.temp.statement({
  "customer": "K",
  "performances": [
    {
      "playID": "www",
      "audience": 0
    },
    {
      "playID": "ok",
      "audience": 0
    },
    {
      "playID": "hmm",
      "audience": 0
    }
  ]
},{
  "www": {"name": "WWW", "type": "tragedy"},
  "ok": {"name": "OK", "type": "comedy"},
  "hmm": {"name": "Hmm", "type": "tragedy"}
}),
            "Statement for K\n WWW: $400.00 (0 seats)\n OK: $300.00 (0 seats)\n Hmm: $400.00 (0 seats)\nAmount owed is $1,100.00\nYou earned 0 credits\n")

    def test_wrong_type(self):
            self.assertRaises(ValueError, self.temp.statement,{
                "customer": "K",
                "performances": [
                    {
                        "playID": "www",
                        "audience": 0
                    },
                    {
                        "playID": "ok",
                        "audience": 0
                    },
                    {
                        "playID": "hmm",
                        "audience": 0
                    }
                ]
            }, {
                "www": {"name": "WWW", "type": "ok"},
                "ok": {"name": "OK", "type": "comedy"},
                "hmm": {"name": "Hmm", "type": "tragedy"}
            })

    def test_wrong_2_types(self):
        self.assertRaises(ValueError, self.temp.statement, {
            "customer": "K",
            "performances": [
                {
                    "playID": "www",
                    "audience": 0
                },
                {
                    "playID": "ok",
                    "audience": 0
                },
                {
                    "playID": "hmm",
                    "audience": 0
                }
            ]
        }, {
                              "www": {"name": "WWW", "type": "ok"},
                              "ok": {"name": "OK", "type": "not ok"},
                              "hmm": {"name": "Hmm", "type": "tragedy"}
                          })

    def test_wrong_3_types(self):
            self.assertRaises(ValueError, self.temp.statement, {
                "customer": "K",
                "performances": [
                    {
                        "playID": "www",
                        "audience": 0
                    },
                    {
                        "playID": "ok",
                        "audience": 0
                    },
                    {
                        "playID": "hmm",
                        "audience": 0
                    }
                ]
            }, {
                                  "www": {"name": "WWW", "type": "ok"},
                                  "ok": {"name": "OK", "type": "not ok"},
                                  "hmm": {"name": "Hmm", "type": "maybe ok"}
                              })

    def tearDown(self):
        self.temp = None


