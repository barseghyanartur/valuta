__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "LIST_CURRENCIES_OUTPUT",
    "CURRENCY_CHOICES",
    "LIST_GENERATED_CURRENCY_MODULES",
)

LIST_CURRENCIES_OUTPUT = """
┌───────────┬──────────────────────────────────────────┐
│ ISO code  │ Currency                                 │
├───────────┼──────────────────────────────────────────┤
│ AED       │ United Arab Emirates Dirham              │
├───────────┼──────────────────────────────────────────┤
│ AFN       │ Afghan Afghani                           │
├───────────┼──────────────────────────────────────────┤
│ ALL       │ Albanian Lek                             │
├───────────┼──────────────────────────────────────────┤
│ AMD       │ Armenian Dram                            │
├───────────┼──────────────────────────────────────────┤
│ ANG       │ Netherlands Antillean Guilder            │
├───────────┼──────────────────────────────────────────┤
│ AOA       │ Angolan Kwanza                           │
├───────────┼──────────────────────────────────────────┤
│ ARS       │ Argentine Peso                           │
├───────────┼──────────────────────────────────────────┤
│ AUD       │ Australian Dollar                        │
├───────────┼──────────────────────────────────────────┤
│ AWG       │ Aruban Florin                            │
├───────────┼──────────────────────────────────────────┤
│ AZN       │ Azerbaijani Manat                        │
├───────────┼──────────────────────────────────────────┤
│ BAM       │ Bosnia-Herzegovina Convertible Mark      │
├───────────┼──────────────────────────────────────────┤
│ BBD       │ Barbadian Dollar                         │
├───────────┼──────────────────────────────────────────┤
│ BDT       │ Bangladeshi Taka                         │
├───────────┼──────────────────────────────────────────┤
│ BGN       │ Bulgarian Lev                            │
├───────────┼──────────────────────────────────────────┤
│ BHD       │ Bahraini Dinar                           │
├───────────┼──────────────────────────────────────────┤
│ BIF       │ Burundian Franc                          │
├───────────┼──────────────────────────────────────────┤
│ BMD       │ Bermudan Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ BND       │ Brunei Dollar                            │
├───────────┼──────────────────────────────────────────┤
│ BOB       │ Bolivian Boliviano                       │
├───────────┼──────────────────────────────────────────┤
│ BRL       │ Brazilian Real                           │
├───────────┼──────────────────────────────────────────┤
│ BSD       │ Bahamian Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ BTC       │ Bitcoin                                  │
├───────────┼──────────────────────────────────────────┤
│ BTN       │ Bhutanese Ngultrum                       │
├───────────┼──────────────────────────────────────────┤
│ BWP       │ Botswanan Pula                           │
├───────────┼──────────────────────────────────────────┤
│ BYN       │ Belarusian Ruble                         │
├───────────┼──────────────────────────────────────────┤
│ BZD       │ Belize Dollar                            │
├───────────┼──────────────────────────────────────────┤
│ CAD       │ Canadian Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ CDF       │ Congolese Franc                          │
├───────────┼──────────────────────────────────────────┤
│ CHF       │ Swiss Franc                              │
├───────────┼──────────────────────────────────────────┤
│ CKD       │ CKD                                      │
├───────────┼──────────────────────────────────────────┤
│ CLP       │ Chilean Peso                             │
├───────────┼──────────────────────────────────────────┤
│ CNY       │ Chinese Yuan                             │
├───────────┼──────────────────────────────────────────┤
│ COP       │ Colombian Peso                           │
├───────────┼──────────────────────────────────────────┤
│ CRC       │ Costa Rican Colón                        │
├───────────┼──────────────────────────────────────────┤
│ CUP       │ Cuban Peso                               │
├───────────┼──────────────────────────────────────────┤
│ CVE       │ Cape Verdean Escudo                      │
├───────────┼──────────────────────────────────────────┤
│ CZK       │ Czech Koruna                             │
├───────────┼──────────────────────────────────────────┤
│ DJF       │ Djiboutian Franc                         │
├───────────┼──────────────────────────────────────────┤
│ DKK       │ Danish Krone                             │
├───────────┼──────────────────────────────────────────┤
│ DOP       │ Dominican Peso                           │
├───────────┼──────────────────────────────────────────┤
│ DZD       │ Algerian Dinar                           │
├───────────┼──────────────────────────────────────────┤
│ EGP       │ Egyptian Pound                           │
├───────────┼──────────────────────────────────────────┤
│ ERN       │ Eritrean Nakfa                           │
├───────────┼──────────────────────────────────────────┤
│ ETB       │ Ethiopian Birr                           │
├───────────┼──────────────────────────────────────────┤
│ EUR       │ Euro                                     │
├───────────┼──────────────────────────────────────────┤
│ FJD       │ Fijian Dollar                            │
├───────────┼──────────────────────────────────────────┤
│ FKP       │ Falkland Islands Pound                   │
├───────────┼──────────────────────────────────────────┤
│ FOK       │ FOK                                      │
├───────────┼──────────────────────────────────────────┤
│ GBP       │ British Pound                            │
├───────────┼──────────────────────────────────────────┤
│ GEL       │ Georgian Lari                            │
├───────────┼──────────────────────────────────────────┤
│ GGP       │ GGP                                      │
├───────────┼──────────────────────────────────────────┤
│ GHS       │ Ghanaian Cedi                            │
├───────────┼──────────────────────────────────────────┤
│ GIP       │ Gibraltar Pound                          │
├───────────┼──────────────────────────────────────────┤
│ GMD       │ Gambian Dalasi                           │
├───────────┼──────────────────────────────────────────┤
│ GNF       │ Guinean Franc                            │
├───────────┼──────────────────────────────────────────┤
│ GTQ       │ Guatemalan Quetzal                       │
├───────────┼──────────────────────────────────────────┤
│ GYD       │ Guyanaese Dollar                         │
├───────────┼──────────────────────────────────────────┤
│ HKD       │ Hong Kong Dollar                         │
├───────────┼──────────────────────────────────────────┤
│ HNL       │ Honduran Lempira                         │
├───────────┼──────────────────────────────────────────┤
│ HRK       │ Croatian Kuna                            │
├───────────┼──────────────────────────────────────────┤
│ HTG       │ Haitian Gourde                           │
├───────────┼──────────────────────────────────────────┤
│ HUF       │ Hungarian Forint                         │
├───────────┼──────────────────────────────────────────┤
│ IDR       │ Indonesian Rupiah                        │
├───────────┼──────────────────────────────────────────┤
│ ILS       │ Israeli New Shekel                       │
├───────────┼──────────────────────────────────────────┤
│ IMP       │ IMP                                      │
├───────────┼──────────────────────────────────────────┤
│ INR       │ Indian Rupee                             │
├───────────┼──────────────────────────────────────────┤
│ IQD       │ Iraqi Dinar                              │
├───────────┼──────────────────────────────────────────┤
│ IRR       │ Iranian Rial                             │
├───────────┼──────────────────────────────────────────┤
│ ISK       │ Icelandic Króna                          │
├───────────┼──────────────────────────────────────────┤
│ JEP       │ JEP                                      │
├───────────┼──────────────────────────────────────────┤
│ JMD       │ Jamaican Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ JOD       │ Jordanian Dinar                          │
├───────────┼──────────────────────────────────────────┤
│ JPY       │ Japanese Yen                             │
├───────────┼──────────────────────────────────────────┤
│ KES       │ Kenyan Shilling                          │
├───────────┼──────────────────────────────────────────┤
│ KGS       │ Kyrgystani Som                           │
├───────────┼──────────────────────────────────────────┤
│ KHR       │ Cambodian Riel                           │
├───────────┼──────────────────────────────────────────┤
│ KID       │ KID                                      │
├───────────┼──────────────────────────────────────────┤
│ KMF       │ Comorian Franc                           │
├───────────┼──────────────────────────────────────────┤
│ KPW       │ North Korean Won                         │
├───────────┼──────────────────────────────────────────┤
│ KRW       │ South Korean Won                         │
├───────────┼──────────────────────────────────────────┤
│ KWD       │ Kuwaiti Dinar                            │
├───────────┼──────────────────────────────────────────┤
│ KYD       │ Cayman Islands Dollar                    │
├───────────┼──────────────────────────────────────────┤
│ KZT       │ Kazakhstani Tenge                        │
├───────────┼──────────────────────────────────────────┤
│ LAK       │ Laotian Kip                              │
├───────────┼──────────────────────────────────────────┤
│ LBP       │ Lebanese Pound                           │
├───────────┼──────────────────────────────────────────┤
│ LKR       │ Sri Lankan Rupee                         │
├───────────┼──────────────────────────────────────────┤
│ LRD       │ Liberian Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ LSL       │ Lesotho Loti                             │
├───────────┼──────────────────────────────────────────┤
│ LYD       │ Libyan Dinar                             │
├───────────┼──────────────────────────────────────────┤
│ MAD       │ Moroccan Dirham                          │
├───────────┼──────────────────────────────────────────┤
│ MDL       │ Moldovan Leu                             │
├───────────┼──────────────────────────────────────────┤
│ MGA       │ Malagasy Ariary                          │
├───────────┼──────────────────────────────────────────┤
│ MKD       │ Macedonian Denar                         │
├───────────┼──────────────────────────────────────────┤
│ MMK       │ Myanmar Kyat                             │
├───────────┼──────────────────────────────────────────┤
│ MNT       │ Mongolian Tugrik                         │
├───────────┼──────────────────────────────────────────┤
│ MOP       │ Macanese Pataca                          │
├───────────┼──────────────────────────────────────────┤
│ MRU       │ Mauritanian Ouguiya                      │
├───────────┼──────────────────────────────────────────┤
│ MUR       │ Mauritian Rupee                          │
├───────────┼──────────────────────────────────────────┤
│ MVR       │ Maldivian Rufiyaa                        │
├───────────┼──────────────────────────────────────────┤
│ MWK       │ Malawian Kwacha                          │
├───────────┼──────────────────────────────────────────┤
│ MXN       │ Mexican Peso                             │
├───────────┼──────────────────────────────────────────┤
│ MYR       │ Malaysian Ringgit                        │
├───────────┼──────────────────────────────────────────┤
│ MZN       │ Mozambican Metical                       │
├───────────┼──────────────────────────────────────────┤
│ NAD       │ Namibian Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ NGN       │ Nigerian Naira                           │
├───────────┼──────────────────────────────────────────┤
│ NIO       │ Nicaraguan Córdoba                       │
├───────────┼──────────────────────────────────────────┤
│ NOK       │ Norwegian Krone                          │
├───────────┼──────────────────────────────────────────┤
│ NPR       │ Nepalese Rupee                           │
├───────────┼──────────────────────────────────────────┤
│ NZD       │ New Zealand Dollar                       │
├───────────┼──────────────────────────────────────────┤
│ OMR       │ Omani Rial                               │
├───────────┼──────────────────────────────────────────┤
│ PAB       │ Panamanian Balboa                        │
├───────────┼──────────────────────────────────────────┤
│ PEN       │ Peruvian Sol                             │
├───────────┼──────────────────────────────────────────┤
│ PGK       │ Papua New Guinean Kina                   │
├───────────┼──────────────────────────────────────────┤
│ PHP       │ Philippine Piso                          │
├───────────┼──────────────────────────────────────────┤
│ PKR       │ Pakistani Rupee                          │
├───────────┼──────────────────────────────────────────┤
│ PLN       │ Polish Zloty                             │
├───────────┼──────────────────────────────────────────┤
│ PND       │ PND                                      │
├───────────┼──────────────────────────────────────────┤
│ PRB       │ PRB                                      │
├───────────┼──────────────────────────────────────────┤
│ PYG       │ Paraguayan Guarani                       │
├───────────┼──────────────────────────────────────────┤
│ QAR       │ Qatari Rial                              │
├───────────┼──────────────────────────────────────────┤
│ RON       │ Romanian Leu                             │
├───────────┼──────────────────────────────────────────┤
│ RSD       │ Serbian Dinar                            │
├───────────┼──────────────────────────────────────────┤
│ RUB       │ Russian Ruble                            │
├───────────┼──────────────────────────────────────────┤
│ RWF       │ Rwandan Franc                            │
├───────────┼──────────────────────────────────────────┤
│ SAR       │ Saudi Riyal                              │
├───────────┼──────────────────────────────────────────┤
│ SBD       │ Solomon Islands Dollar                   │
├───────────┼──────────────────────────────────────────┤
│ SCR       │ Seychellois Rupee                        │
├───────────┼──────────────────────────────────────────┤
│ SDG       │ Sudanese Pound                           │
├───────────┼──────────────────────────────────────────┤
│ SEK       │ Swedish Krona                            │
├───────────┼──────────────────────────────────────────┤
│ SGD       │ Singapore Dollar                         │
├───────────┼──────────────────────────────────────────┤
│ SHP       │ St. Helena Pound                         │
├───────────┼──────────────────────────────────────────┤
│ SLL       │ Sierra Leonean Leone                     │
├───────────┼──────────────────────────────────────────┤
│ SLS       │ SLS                                      │
├───────────┼──────────────────────────────────────────┤
│ SOS       │ Somali Shilling                          │
├───────────┼──────────────────────────────────────────┤
│ SRD       │ Surinamese Dollar                        │
├───────────┼──────────────────────────────────────────┤
│ SSP       │ South Sudanese Pound                     │
├───────────┼──────────────────────────────────────────┤
│ STN       │ São Tomé & Príncipe Dobra                │
├───────────┼──────────────────────────────────────────┤
│ SYP       │ Syrian Pound                             │
├───────────┼──────────────────────────────────────────┤
│ SZL       │ Swazi Lilangeni                          │
├───────────┼──────────────────────────────────────────┤
│ THB       │ Thai Baht                                │
├───────────┼──────────────────────────────────────────┤
│ TJS       │ Tajikistani Somoni                       │
├───────────┼──────────────────────────────────────────┤
│ TMT       │ Turkmenistani Manat                      │
├───────────┼──────────────────────────────────────────┤
│ TND       │ Tunisian Dinar                           │
├───────────┼──────────────────────────────────────────┤
│ TOP       │ Tongan Paʻanga                           │
├───────────┼──────────────────────────────────────────┤
│ TRY       │ Turkish Lira                             │
├───────────┼──────────────────────────────────────────┤
│ TTD       │ Trinidad & Tobago Dollar                 │
├───────────┼──────────────────────────────────────────┤
│ TVD       │ TVD                                      │
├───────────┼──────────────────────────────────────────┤
│ TWD       │ New Taiwan Dollar                        │
├───────────┼──────────────────────────────────────────┤
│ TZS       │ Tanzanian Shilling                       │
├───────────┼──────────────────────────────────────────┤
│ UAH       │ Ukrainian Hryvnia                        │
├───────────┼──────────────────────────────────────────┤
│ UGX       │ Ugandan Shilling                         │
├───────────┼──────────────────────────────────────────┤
│ USD       │ US Dollar                                │
├───────────┼──────────────────────────────────────────┤
│ UYU       │ Uruguayan Peso                           │
├───────────┼──────────────────────────────────────────┤
│ UZS       │ Uzbekistani Som                          │
├───────────┼──────────────────────────────────────────┤
│ VES       │ Venezuelan Bolívar                       │
├───────────┼──────────────────────────────────────────┤
│ VND       │ Vietnamese Dong                          │
├───────────┼──────────────────────────────────────────┤
│ VUV       │ Vanuatu Vatu                             │
├───────────┼──────────────────────────────────────────┤
│ WST       │ Samoan Tala                              │
├───────────┼──────────────────────────────────────────┤
│ XAF       │ Central African CFA Franc                │
├───────────┼──────────────────────────────────────────┤
│ XCD       │ East Caribbean Dollar                    │
├───────────┼──────────────────────────────────────────┤
│ XOF       │ West African CFA Franc                   │
├───────────┼──────────────────────────────────────────┤
│ XPF       │ CFP Franc                                │
├───────────┼──────────────────────────────────────────┤
│ YER       │ Yemeni Rial                              │
├───────────┼──────────────────────────────────────────┤
│ ZAR       │ South African Rand                       │
├───────────┼──────────────────────────────────────────┤
│ ZMW       │ Zambian Kwacha                           │
├───────────┼──────────────────────────────────────────┤
│ ZWB       │ ZWB                                      │
└───────────┴──────────────────────────────────────────┘
""".strip().encode()


CURRENCY_CHOICES = [
    ("AFN", "Afghan Afghani"),
    ("ALL", "Albanian Lek"),
    ("DZD", "Algerian Dinar"),
    ("AOA", "Angolan Kwanza"),
    ("ARS", "Argentine Peso"),
    ("AMD", "Armenian Dram"),
    ("AWG", "Aruban Florin"),
    ("AUD", "Australian Dollar"),
    ("AZN", "Azerbaijani Manat"),
    ("BSD", "Bahamian Dollar"),
    ("BHD", "Bahraini Dinar"),
    ("BDT", "Bangladeshi Taka"),
    ("BBD", "Barbadian Dollar"),
    ("BYN", "Belarusian Ruble"),
    ("BZD", "Belize Dollar"),
    ("BMD", "Bermudan Dollar"),
    ("BTN", "Bhutanese Ngultrum"),
    ("BTC", "Bitcoin"),
    ("BOB", "Bolivian Boliviano"),
    ("BAM", "Bosnia-Herzegovina Convertible Mark"),
    ("BWP", "Botswanan Pula"),
    ("BRL", "Brazilian Real"),
    ("GBP", "British Pound"),
    ("BND", "Brunei Dollar"),
    ("BGN", "Bulgarian Lev"),
    ("BIF", "Burundian Franc"),
    ("XPF", "CFP Franc"),
    ("CKD", "CKD"),
    ("KHR", "Cambodian Riel"),
    ("CAD", "Canadian Dollar"),
    ("CVE", "Cape Verdean Escudo"),
    ("KYD", "Cayman Islands Dollar"),
    ("XAF", "Central African CFA Franc"),
    ("CLP", "Chilean Peso"),
    ("CNY", "Chinese Yuan"),
    ("COP", "Colombian Peso"),
    ("KMF", "Comorian Franc"),
    ("CDF", "Congolese Franc"),
    ("CRC", "Costa Rican Colón"),
    ("HRK", "Croatian Kuna"),
    ("CUP", "Cuban Peso"),
    ("CZK", "Czech Koruna"),
    ("DKK", "Danish Krone"),
    ("DJF", "Djiboutian Franc"),
    ("DOP", "Dominican Peso"),
    ("XCD", "East Caribbean Dollar"),
    ("EGP", "Egyptian Pound"),
    ("ERN", "Eritrean Nakfa"),
    ("ETB", "Ethiopian Birr"),
    ("EUR", "Euro"),
    ("FOK", "FOK"),
    ("FKP", "Falkland Islands Pound"),
    ("FJD", "Fijian Dollar"),
    ("GGP", "GGP"),
    ("GMD", "Gambian Dalasi"),
    ("GEL", "Georgian Lari"),
    ("GHS", "Ghanaian Cedi"),
    ("GIP", "Gibraltar Pound"),
    ("GTQ", "Guatemalan Quetzal"),
    ("GNF", "Guinean Franc"),
    ("GYD", "Guyanaese Dollar"),
    ("HTG", "Haitian Gourde"),
    ("HNL", "Honduran Lempira"),
    ("HKD", "Hong Kong Dollar"),
    ("HUF", "Hungarian Forint"),
    ("IMP", "IMP"),
    ("ISK", "Icelandic Króna"),
    ("INR", "Indian Rupee"),
    ("IDR", "Indonesian Rupiah"),
    ("IRR", "Iranian Rial"),
    ("IQD", "Iraqi Dinar"),
    ("ILS", "Israeli New Shekel"),
    ("JEP", "JEP"),
    ("JMD", "Jamaican Dollar"),
    ("JPY", "Japanese Yen"),
    ("JOD", "Jordanian Dinar"),
    ("KID", "KID"),
    ("KZT", "Kazakhstani Tenge"),
    ("KES", "Kenyan Shilling"),
    ("KWD", "Kuwaiti Dinar"),
    ("KGS", "Kyrgystani Som"),
    ("LAK", "Laotian Kip"),
    ("LBP", "Lebanese Pound"),
    ("LSL", "Lesotho Loti"),
    ("LRD", "Liberian Dollar"),
    ("LYD", "Libyan Dinar"),
    ("MOP", "Macanese Pataca"),
    ("MKD", "Macedonian Denar"),
    ("MGA", "Malagasy Ariary"),
    ("MWK", "Malawian Kwacha"),
    ("MYR", "Malaysian Ringgit"),
    ("MVR", "Maldivian Rufiyaa"),
    ("MRU", "Mauritanian Ouguiya"),
    ("MUR", "Mauritian Rupee"),
    ("MXN", "Mexican Peso"),
    ("MDL", "Moldovan Leu"),
    ("MNT", "Mongolian Tugrik"),
    ("MAD", "Moroccan Dirham"),
    ("MZN", "Mozambican Metical"),
    ("MMK", "Myanmar Kyat"),
    ("NAD", "Namibian Dollar"),
    ("NPR", "Nepalese Rupee"),
    ("ANG", "Netherlands Antillean Guilder"),
    ("TWD", "New Taiwan Dollar"),
    ("NZD", "New Zealand Dollar"),
    ("NIO", "Nicaraguan Córdoba"),
    ("NGN", "Nigerian Naira"),
    ("KPW", "North Korean Won"),
    ("NOK", "Norwegian Krone"),
    ("OMR", "Omani Rial"),
    ("PND", "PND"),
    ("PRB", "PRB"),
    ("PKR", "Pakistani Rupee"),
    ("PAB", "Panamanian Balboa"),
    ("PGK", "Papua New Guinean Kina"),
    ("PYG", "Paraguayan Guarani"),
    ("PEN", "Peruvian Sol"),
    ("PHP", "Philippine Piso"),
    ("PLN", "Polish Zloty"),
    ("QAR", "Qatari Rial"),
    ("RON", "Romanian Leu"),
    ("RUB", "Russian Ruble"),
    ("RWF", "Rwandan Franc"),
    ("SLS", "SLS"),
    ("WST", "Samoan Tala"),
    ("SAR", "Saudi Riyal"),
    ("RSD", "Serbian Dinar"),
    ("SCR", "Seychellois Rupee"),
    ("SLL", "Sierra Leonean Leone"),
    ("SGD", "Singapore Dollar"),
    ("SBD", "Solomon Islands Dollar"),
    ("SOS", "Somali Shilling"),
    ("ZAR", "South African Rand"),
    ("KRW", "South Korean Won"),
    ("SSP", "South Sudanese Pound"),
    ("LKR", "Sri Lankan Rupee"),
    ("SHP", "St. Helena Pound"),
    ("SDG", "Sudanese Pound"),
    ("SRD", "Surinamese Dollar"),
    ("SZL", "Swazi Lilangeni"),
    ("SEK", "Swedish Krona"),
    ("CHF", "Swiss Franc"),
    ("SYP", "Syrian Pound"),
    ("STN", "São Tomé & Príncipe Dobra"),
    ("TVD", "TVD"),
    ("TJS", "Tajikistani Somoni"),
    ("TZS", "Tanzanian Shilling"),
    ("THB", "Thai Baht"),
    ("TOP", "Tongan Paʻanga"),
    ("TTD", "Trinidad & Tobago Dollar"),
    ("TND", "Tunisian Dinar"),
    ("TRY", "Turkish Lira"),
    ("TMT", "Turkmenistani Manat"),
    ("USD", "US Dollar"),
    ("UGX", "Ugandan Shilling"),
    ("UAH", "Ukrainian Hryvnia"),
    ("AED", "United Arab Emirates Dirham"),
    ("UYU", "Uruguayan Peso"),
    ("UZS", "Uzbekistani Som"),
    ("VUV", "Vanuatu Vatu"),
    ("VES", "Venezuelan Bolívar"),
    ("VND", "Vietnamese Dong"),
    ("XOF", "West African CFA Franc"),
    ("YER", "Yemeni Rial"),
    ("ZWB", "ZWB"),
    ("ZMW", "Zambian Kwacha"),
]

LIST_GENERATED_CURRENCY_MODULES = [
    "aed.py",
    "afn.py",
    "all.py",
    "amd.py",
    "ang.py",
    "aoa.py",
    "ars.py",
    "aud.py",
    "awg.py",
    "azn.py",
    "bam.py",
    "bbd.py",
    "bdt.py",
    "bgn.py",
    "bhd.py",
    "bif.py",
    "bmd.py",
    "bnd.py",
    "bob.py",
    "brl.py",
    "bsd.py",
    "btn.py",
    "bwp.py",
    "byn.py",
    "bzd.py",
    "cad.py",
    "cdf.py",
    "chf.py",
    "ckd.py",
    "clp.py",
    "cny.py",
    "cop.py",
    "crc.py",
    "cup.py",
    "cve.py",
    "czk.py",
    "djf.py",
    "dkk.py",
    "dop.py",
    "dzd.py",
    "egp.py",
    "ern.py",
    "etb.py",
    "eur.py",
    "fjd.py",
    "fkp.py",
    "fok.py",
    "gbp.py",
    "gel.py",
    "ggp.py",
    "ghs.py",
    "gip.py",
    "gmd.py",
    "gnf.py",
    "gtq.py",
    "gyd.py",
    "hkd.py",
    "hnl.py",
    "hrk.py",
    "htg.py",
    "huf.py",
    "idr.py",
    "ils.py",
    "imp.py",
    "inr.py",
    "iqd.py",
    "irr.py",
    "isk.py",
    "jep.py",
    "jmd.py",
    "jod.py",
    "jpy.py",
    "kes.py",
    "kgs.py",
    "khr.py",
    "kid.py",
    "kmf.py",
    "kpw.py",
    "krw.py",
    "kwd.py",
    "kyd.py",
    "kzt.py",
    "lak.py",
    "lbp.py",
    "lkr.py",
    "lrd.py",
    "lsl.py",
    "lyd.py",
    "mad.py",
    "mdl.py",
    "mga.py",
    "mkd.py",
    "mmk.py",
    "mnt.py",
    "mop.py",
    "mru.py",
    "mur.py",
    "mvr.py",
    "mwk.py",
    "mxn.py",
    "myr.py",
    "mzn.py",
    "nad.py",
    "ngn.py",
    "nio.py",
    "nok.py",
    "npr.py",
    "nzd.py",
    "omr.py",
    "pab.py",
    "pen.py",
    "pgk.py",
    "php.py",
    "pkr.py",
    "pln.py",
    "pnd.py",
    "prb.py",
    "pyg.py",
    "qar.py",
    "ron.py",
    "rsd.py",
    "rub.py",
    "rwf.py",
    "sar.py",
    "sbd.py",
    "scr.py",
    "sdg.py",
    "sek.py",
    "sgd.py",
    "shp.py",
    "sll.py",
    "sls.py",
    "sos.py",
    "srd.py",
    "ssp.py",
    "stn.py",
    "syp.py",
    "szl.py",
    "thb.py",
    "tjs.py",
    "tmt.py",
    "tnd.py",
    "top.py",
    "try.py",
    "ttd.py",
    "tvd.py",
    "twd.py",
    "tzs.py",
    "uah.py",
    "ugx.py",
    "usd.py",
    "uyu.py",
    "uzs.py",
    "ves.py",
    "vnd.py",
    "vuv.py",
    "wst.py",
    "xaf.py",
    "xcd.py",
    "xof.py",
    "xpf.py",
    "yer.py",
    "zar.py",
    "zmw.py",
    "zwb.py",
]
